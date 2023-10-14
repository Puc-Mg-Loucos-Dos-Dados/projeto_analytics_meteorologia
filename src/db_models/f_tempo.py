from .d_data import D_Data
from .d_dia_noite import D_DiaNoite
from .d_estacao_ano import D_EstacaoAno
from .d_hora import D_Hora


class F_Tempo:
	def __init__(self, data: D_Data, hora: D_Hora,
				 dia_noite: D_DiaNoite, estacao_ano: D_EstacaoAno):
		self.data = data
		self.hora = hora
		self.dia_noite = dia_noite
		self.estacao_ano = estacao_ano

	def to_json(self):
		pass
