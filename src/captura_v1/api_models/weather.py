from datetime import datetime, date, time

class Weather_Item:
    def __init__(self, dt: datetime, d: date, t: time, v: int, measure_name: str):
        self.dt = dt
        self.d = d
        self.t = t
        self.v = v
        self.measure_name = measure_name

    def to_json(self):
        return {
            'measure': self.measure_name,
            'date_time': self.dt,
            'date': self.d,
            'value': self.v
        }

class Weather:
    def __init__(self, measure: str, dt_ref: date, values: list = []):
        self.measure = measure
        self.values = values or []
        self.dt_ref = dt_ref

    def to_json(self):
        return {
            'measure': self.measure,
            'dt_ref': self.dt_ref,
            'values': [x.to_json() for x in self.values]
        }

    @classmethod
    def get_from_json(cls, json_data: dict, dt):
        print('Weather.get_from_json: Passando!!')
        # Aqui vou usar dt como referência de ano e nada mais
        if 'cols' not in json_data or 'rows' not in json_data:
            raise Exception('Dados inválidos')

        if not isinstance(json_data['rows'], list) or len(json_data['rows']) == 0:
            raise Exception('Não há medidas a serem capturadas')

        measure_name = None
        for c in json_data['cols']:
            if c['label'] != 'Fecha':
                measure_name = c['label']

        year = dt.year
        measures = []
        dt_ref = None
        for r in json_data['rows']:
            measure = r['c']
            dt_time_ref = None
            time_ref = None
            measured_value = None

            for v in measure:
                # Aqui assumo que a medição em si é sempre numérica
                if isinstance(v['v'], str):
                    # Aqui temos a data e/ou hora
                    if ' ' in v['v']:
                        # Primeiro registro, possui a data no formato dia/mês
                        dt_ref = datetime(
                            year=dt.year,
                            month=int(v['v'].split(' ')[0].split('/')[1]),
                            day=int(v['v'].split(' ')[0].split('/')[0])).date()
                    else:
                        dt_time_ref = datetime(
                            year=dt_ref.year,
                            month=dt_ref.month,
                            day=dt_ref.day,
                            hour=int(v['v'].split(':')[0]),
                            minute=int(v['v'].split(':')[1]),
                            second=0)
                        time_ref = dt_time_ref.time()
                else:
                    # Aqui temos a medição em si
                    measured_value = v['v']

            measure_item = Weather_Item(
                dt=dt_time_ref,
                d=dt_ref,
                t=time_ref,
                v=measured_value,
                measure_name = measure_name)
            measures.append(measure_item)

        return cls(
            measure=measure_name,
            values=measures,
            dt_ref=dt_ref)
