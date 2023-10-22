#! /usr/bin/env python

from .db_models import (
    SA_D_Data,
    SA_D_EstacaoAno,
    SA_D_Hora,
    SA_F_Tempo)
from adapters_apis import WeatherAdapter
from api_models import Weather
from datetime import datetime, timedelta
from sqlalchemy import (
    create_engine,
    select)
from sqlalchemy.orm import Session, sessionmaker

import requests
import os

if 'src' in os.getcwd():
    from config import Config, Action
else:
    from src.config import Config, Action


mapa_dia_semana = {
    1: 'segunda-feira',
    2: 'terça-feira',
    3: 'quarta-feira',
    4: 'quinta-feira',
    5: 'sexta-feira',
    6: 'sábado',
    7: 'domingo'
}


class CollectHistory:
    # Para conexão com o banco
    engine = None
    db_user = 'app'
    db_psw = 'app123'
    db_host = '127.0.0.1'
    db_port = '3306'
    db_name = 'analytics_weather_db'

    # Para testes coloquei no começo do mês
    inicio_periodo = datetime(2023, 10, 13, 0, 0, 0)
    fim_periodo = None

    medidas_dia_hora = {}

    # Aqui vem as URLs das APIs a serem atualizadas durante todo o processo
    url_vento = None
    url_pressao = None
    url_umidade = None
    url_temperatura = None
    url_sol = None

    def __init__(self):
        print('Instanciando config')
        self.cfg = Config()
        print('Realizando a coleta')
        self.collects()
        print('Criando conexão com o banco')
        self.engine = create_engine(f'mysql+pymysql://{self.db_user}:{self.db_psw}@{self.db_host}:{self.db_port}/{self.db_name}')
        self.medidas_dia_hora = {}

    def collects(self):
        self.fim_periodo = datetime.now()
        dt_controle = self.inicio_periodo
        continua = True

        while continua:
            # Zerando as medições do dia
            self.medidas_dia_hora = {}
            # A cada rodada irei instanciar novamente os adapters pq irei trocar as URLs
            print(f'Coletando dia {dt_controle.strftime("%d/%m/%Y")}')
            print('\t- Coletando dados de vento')
            wind_data = self.collect_wind(dt_controle)
            print('\t- Coletando dados de pressão atmosférica')
            pressure_data = self.collect_pressure(dt_controle)
            print('\t- Coletando dados de umidade relativa do ar')
            humidity_data = self.collect_humidity(dt_controle)
            print('\t- Coletando dados de temperatura')
            temperature_data = self.collect_temperature(dt_controle)

            print('\t- Agrupando os dados de um dia e salvando')
            self.process_save_day(
                wind=wind_data,
                pressure=pressure_data,
                humidity=humidity_data,
                temperature=temperature_data,
                dt_controle=dt_controle)

            print('\n')
            dt_controle = dt_controle + timedelta(days=1)
            if dt_controle.date() == self.fim_periodo.date():
                continua = False

    def process_save_day(self, wind, pressure, humidity, temperature, dt_controle):
        lista_medidas = [wind, pressure, humidity, temperature]
        with Session(self.engine) as ss:
            # Para agrupar as medidas por hora
            medidas_hora = {}

            stmt_1 = select(SA_D_Data).filter_by(data=dt_controle.date())
            dt = ss.scalars(stmt_1).first()

            if dt is None:
                # A data ainda não foi registrada
                dt = SA_D_Data(
                    data=dt_controle.date(),
                    dia_semana=mapa_dia_semana[dt_controle.date().isoweekday()])
                ss.add(dt)
                print('Persistindo data')
                ss.commit()

            for medida in lista_medidas:
                print(f'\t\t+ Processando {medida.measure}')
                for v in medida.values:
                    hr_str = v.dt.time().strftime('%H:%M')

                    if hr_str not in medidas_hora:
                        # Checando se o registro de hora existe
                        stmt_2 = select(SA_D_Hora).filter_by(
                            id_data=dt.id,
                            hora=v.dt.time())
                        hora = ss.scalars(stmt_2).first()

                        if hora is None:
                            hora = SA_D_Hora(
                                hora=v.dt.time(),
                                data=dt)
                            ss.add(hora)

                        print('Persistindo hora, se necessário')
                        ss.commit()

                        # Adicionando a hora como chave no dicionário
                        if hr_str not in medidas_hora:
                            medidas_hora[hr_str] = {
                                'hora': hora,
                                'medida': None
                            }
                    else:
                        hora = medidas_hora[hr_str]['hora']

                    if medidas_hora[hr_str]['medida'] is None:
                        # Checando se o registro de medida existe
                        stmt_3 = select(SA_F_Tempo).filter_by(
                            id_data=dt.id,
                            id_hora=hora.id)
                        med_db = ss.scalars(stmt_3).first()

                        if med_db is None:
                            med_db = SA_F_Tempo(
                                data=dt, hora=hora)
                            medidas_hora[hr_str]['medida'] = med_db

                            if medida.measure == 'Umidade':
                                medidas_hora[hr_str]['medida'].umidade = v.v
                            elif medida.measure == 'Temperatura':
                                medidas_hora[hr_str]['medida'].temperatura = v.v
                            elif medida.measure == 'Pressão':
                                medidas_hora[hr_str]['medida'].pressao_atmosferica = v.v
                            elif medida.measure == 'Vento':
                                medidas_hora[hr_str]['medida'].umidade = v.v
                        else:
                            # Sim, já tem algo no banco
                            # Nem mexo, passo reto
                            medidas_hora[hr_str]['medida'] = None
                            continue

            # Só depois que capturo todas as medidas é que salvo no banco
            # Para não dar zica na linha 151
            for k in medidas_hora:
                ## Agora sim ponho todas as medidas na sessão
                if medidas_hora[k]['medida'] is not None:
                    ss.add(medidas_hora[k]['medida'])

            ss.commit()

    def collect_wind(self, dt: datetime):
        print(f'\t+ Coletando Vento')
        url = self.cfg.get_weather_url('sao_paulo', dt, Action.WIND)
        adapter = WeatherAdapter(url, dt)
        wind_data = adapter.get_data()

    def collect_temperature(self, dt: datetime):
        print('\t+ Coletando Temperatura')
        url = self.cfg.get_weather_url('sao_paulo', dt, Action.TEMPERATURE)
        adapter = WeatherAdapter(url, dt)
        temperature_data = adapter.get_data()

    def collect_humidity(self, dt: datetime):
        print('\t+ Coletando Umidade')
        url = self.cfg.get_weather_url('sao_paulo', dt, Action.HUMIDITY)
        adapter = WeatherAdapter(url, dt)
        humidity_data = adapter.get_data()

    def collect_pressure(self, dt: datetime):
        print('\t+ Coletando Pressão')
        url = self.cfg.get_weather_url('sao_paulo', dt, Action.PRESSURE)
        adapter = WeatherAdapter(url, dt)
        pressure_data = adapter.get_data()

    def collect_sunset_sunrise(self, dt: datetime):
        headers = {}
        response = requests.request('GET', self.url_sol, headers=headers)

        if response.status_code != 200:
            raise Exception(f'Ocorreu um erro de status {response.status_code}')

        return response.json()


if __name__ == '__main__':
    coleta = CollectHistory()
    coleta.collects()
