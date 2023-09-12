#! /usr/bin/env python

from adapters_apis import WeatherAdapter
from api_models import Weather
from datetime import datetime, timedelta
import requests
import os

if 'src' in os.getcwd():
    from config import Config, Action
else:
    from src.config import Config, Action


class CollectHistory:
    # Para testes coloquei no começo do mês
    inicio_periodo = datetime(2023, 9, 1, 0, 0, 0)
    fim_periodo = None

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

    def collects(self):
        self.fim_periodo = datetime.now()
        dt_controle = self.inicio_periodo
        continua = True

        while continua:
            # A cada rodada irei instanciar novamente os adapters pq irei trocar as URLs
            print(f'Coletando dia {dt_controle.strftime("%d/%m/%Y")}')
            wind_data = self.collect_wind(dt_controle)
            pressure_data = self.collect_pressure(dt_controle)
            humidity_data = self.collect_humidity(dt_controle)
            temperature_data = self.collect_temperature(dt_controle)

            dt_controle = dt_controle + timedelta(days=1)
            if dt_controle.date() == self.fim_periodo.date():
                continua = False

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
        print(temperature_data.to_json())

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
