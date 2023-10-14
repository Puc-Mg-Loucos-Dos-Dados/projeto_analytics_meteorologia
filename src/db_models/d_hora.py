from .d_data import D_Data


class D_Hora:
	def __init__(self, data: D_Data, hora: int, minuto: int):
		self.data = data
		self.hora = hora
		self.minuto = minuto
