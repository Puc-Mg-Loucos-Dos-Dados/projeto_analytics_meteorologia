from datetime import date, datetime
from decouple import config
from enum import Enum


class Action(Enum):
	TEMPERATURE = 'T'
	PRESSURE = 'P'
	HUMIDITY = 'H'
	WIND = 'V'


class Config:
	DEBUG = True
	ENVIRONMENT = config('FLASK_CONFIG', 'development')
	FLASK_APP = config('FLASK_APP', None)
	FLASK_DEBUG = config('FLASK_DEBUG', 1)

	LOCATIONS = {
		'sao_paulo': {
			'latitude': -23.511298,
			'longitude': -46.629908,
			'id_estacao_meteorologica': '571e07b8c76c49177837d4e1',
			'id_localidade': '12996'
		}
	}

	URL_API_WEATHER = 'https://www.tempo.com/peticiones/datosgrafica_sactual_16.php'
	URL_API_SUNSET_SUNRISE = 'https://api.sunrise-sunset.org'

	def get_weather_url(self, city: str, dt, action: Action):
		if city not in self.LOCATIONS:
			raise Exception('Cidade não permitida')

		if type(dt) not in (date, datetime):
			raise Exception('Data de busca inválida')

		loc_data = self.LOCATIONS[city]
		station_part = f'id_estacion={loc_data["id_estacao_meteorologica"]}'
		action_part = f'accion={action.value}'
		location_part = f'id_localidad={loc_data["id_localidade"]}'
		dt_part = f'anno={dt.year}&mes={dt.month}&dia={dt.day}'
		return f'{self.URL_API_WEATHER}?{station_part}&{action_part}&{location_part}&{dt_part}'

	def get_sunset_sunrise_url(self, city: str, dt):
		if city not in self.LOCATIONS:
			raise Exception('Cidade não permitida')

		if type(dt) not in (date, datetime):
			raise Exception('Data de busca inválida')

		loc_data = self.LOCATIONS[city]
		dt_part = f'date={dt.year}-{dt.month}-{dt_day}'
		lat_part = f'lat={loc_data["latitude"]}'
		long_part = f'lng={loc_data["longitude"]}'
		return f'{self.URL_API_SUNSET_SUNRISE}/json?{lat_part}&{long_part}&{date_part}'
