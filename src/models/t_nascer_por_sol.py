from datetime import datetime, date


class NascerPorSol:
	def __init__(self, data: date = None,
				 nascer_sol: time = None,
				 por_sol: time = None,
				 meio_dia: time = None,
				 tempo_claridade: time = None,
				 crepusculo_civil_comeco: time = None,
				 crepusculo_civil_fim: time = None,
				 crepusculo_nautico_comeco: time = None,
				 crepusculo_nautico_fim: time = None,
				 crepusculo_astronomico_comeco: time = None,
				 crepusculo_astronomico_fim: time = None):
		self.data = data
		self.nascer_sol = nascer_sol
		self.por_sol = por_sol
		self.meio_dia = meio_dia
		self.tempo_claridade = tempo_claridade
		self.crepusculo_civil_comeco = crepusculo_civil_comeco
		self.crepusculo_civil_fim = crepusculo_civil_fim
		self.crepusculo_nautico_comeco = crepusculo_nautico_comeco
		self.crepusculo_nautico_fim = crepusculo_nautico_fim
		self.crepusculo_astronomico_comeco = crepusculo_astronomico_comeco
		self.crepusculo_astronomico_fim = crepusculo_astronomico_fim

	@classmethod
	def get_from_json(cls, json_data, data: date):
		dados = json_data['results']
		return cls(
			data=data,
			)