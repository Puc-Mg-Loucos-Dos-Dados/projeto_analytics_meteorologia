from datetime import datetime
import requests


class AdapterBase:
	def __init__(self, url: str, model_class, dt_ref: datetime):
		self.url = url
		self.model_class = model_class
		self.dt_ref = dt_ref

	def get_data(self):
		print('Chamando o get_data do AdapterBase')
		payload = {}
		headers = {'Content-Type': 'application/json'}
		print(f'+ URL: {self.url}')
		response = requests.request('GET', self.url, headers=headers, data=payload)

		if response.status_code < 200 or response.status_code >= 300:
			raise Exception(f'Status retornado {response.status_code} inesperado')

		print('Chamando o get_from_json da model')
		response_data = self.model_class.get_from_json(response.json(), self.dt_ref)
		return response_data
