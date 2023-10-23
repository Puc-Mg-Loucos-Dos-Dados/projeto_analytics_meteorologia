from datetime import datetime, date, time


class T_PrevisaoDia:
	def __init__(self, data: date,
				 nascer_sol: time = None,
				 por_sol: time = None,
				 primeira_luz_dia: time = None,
				 ultima_luz_dia: time = None,
				 nascer_lua: time = None,
				 por_lua: time = None,
				 temperatura_maxima_prevista: float = None,
				 temperatura_maxima_medida: float = None,
				 temperatura_minima_prevista: float = None,
				 temperatura_minima_medida: float = None,
				 pressao_prevista: float = None,
				 nuvens_prevista: float = None,
				 umidade_prevista: float = None,
				 uv_nublado_previsto: float = None,
				 uv_limpo_previsto: float = None,
				 previsoes_horarias: list = []):
		self.data = data
		self.nascer_sol = nascer_sol
		self.por_sol = por_sol
		self.primeira_luz_dia = primeira_luz_dia
		self.ultima_luz_dia = ultima_luz_dia
		self.nascer_lua = nascer_lua
		self.por_lua = por_lua
		self.temperatura_maxima_prevista = temperatura_maxima_prevista
		self.temperatura_maxima_medida = temperatura_maxima_medida
		self.temperatura_minima_prevista = temperatura_minima_prevista
		self.temperatura_minima_medida = temperatura_minima_medida
		self.pressao_prevista = pressao_prevista
		self.nuvens_prevista = nuvens_prevista
		self.umidade_prevista = umidade_prevista
		self.uv_nublado_previsto = uv_nublado_previsto
		self.uv_limpo_previsto = uv_limpo_previsto
		self.previsoes_horarias = previsoes_horarias or []
