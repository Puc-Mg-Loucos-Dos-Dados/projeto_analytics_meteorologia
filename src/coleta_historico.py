from datetime import datetime, timedelta
import requests


SAO_PAULO_LAT = -23.511298
SAO_PAULO_LONG = -46.629908

API_NASCER_POR_SOL = 'https://api.sunrise-sunset.org/json'


# Configurações API histórica
API_HISTORICO = 'https://www.tempo.com/peticiones/datosgrafica_sactual_16.php'
SAO_PAULO_HISTORIC_ID = '571e07b8c76c49177837d4e1'


# Configurações API tempo hj
SAO_PAULO_ID = '12996'


class ColetaHistorico:
    inicio_periodo = datetime(1, 1, 2015, 0, 0, 0)
    fim_periodo = None

    # Aqui vem as URLs das APIs a serem atualizadas durante todo o processo
    url_vento = None
    url_pressao = None
    url_umidade = None
    url_temperatura = None
    url_sol = None

    def __init__(self):
        self.realiza_coleta()

    def realiza_coleta(self):
        fim_periodo_temp = datetime.now()
        self.fim_periodo = fim_periodo_temp - timedelta(days=1)
        dt_controle = inicio_periodo
        continua = True

        while continua:
            self.monta_urls_historico()
            dados_vento = self.coleta_vento()
            dados_pressao = self.coleta_pressao()
            dados_umidade = self.coleta_umidade()
            dados_temperatura = self.coleta_temperatura()

            dt_controle = dt_controle + timedelta(days=1)
            if dt_controle.date() == self.fim_periodo.date():
                continua = False

    def monta_urls_historico(self, data: date):
        param_estacao = f'id_estacion={SAO_PAULO_HISTORIC_ID}'
        param_localidade = f'id_localidad={SAO_PAULO_ID}'
        param_ano = str(data.year)
        param_mes = str(data.month)
        param_dia = str(data.day)

        self.url_vento = f'{API_HISTORICO}?{param_estacao}&accion=V&{param_localidade}&anno={param_ano}&mes={param_mes}&dia={param_dia}'
        self.url_pressao = f'{API_HISTORICO}?{param_estacao}&accion=P&{param_localidade}&anno={param_ano}&mes={param_mes}&dia={param_dia}'
        self.url_temperatura = f'{API_HISTORICO}?{param_estacao}&accion=T&{param_localidade}&anno={param_ano}&mes={param_mes}&dia={param_dia}'
        self.url_umidade = f'{API_HISTORICO}?{param_estacao}&accion=H&{param_localidade}&anno={param_ano}&mes={param_mes}&dia={param_dia}'
        self.url_sol = f'{API_NASCER_POR_SOL}&lat={SAO_PAULO_LAT}&lng={SAO_PAULO_LONG}'

    def coleta_vento(self):
        pass

    def coleta_temperatura(self):
        pass

    def coleta_umidade(self):
        pass

    def coleta_pressao(self):
        pass

    def coleta_nascer_por_sol(self):
        headers = {}
        response = requests.request('GET', self.url_sol, headers=headers)

        if response.status_code != 200:
            raise Exception(f'Ocorreu um erro de status {response.status_code}')

        return response.json()
