from .d_data import D_Data


class D_Hora:
	def __init__(self, d_id: int, data: D_Data, hora: int, minuto: int):
		self.d_id = d_id
		self.data = data
		self.hora = hora
		self.minuto = minuto
