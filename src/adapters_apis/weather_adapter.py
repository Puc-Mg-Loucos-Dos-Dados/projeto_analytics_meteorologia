from api_models import Weather
from datetime import datetime
from .adapter_base import AdapterBase


class WeatherAdapter(AdapterBase):
    def __init__(self, url: str, dt_ref: datetime, model_class=Weather):
        super(WeatherAdapter, self).__init__(
            url=url,
            model_class=model_class,
            dt_ref=dt_ref)
