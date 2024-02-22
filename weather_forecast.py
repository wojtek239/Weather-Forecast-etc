.from file_mixin import FileMixin
from connection_mixin import ConnectionMixin


class WeatherForecast(FileMixin, ConnectionMixin):
    def __init__(self, filename, url, api_key):
        super().__init__(filename)
        self.url = url
        self.api_key = api_key

    def get_weather_forecast(self, location, datetime_str):
        data = self.read_file()
        if data and location in data and datetime_str in data[location]:
            print("Fetching weather forecast from file...")
            return data[location][datetime_str]
        else:
            print("Fetching weather forecast from API...")
            params = {'key': self.api_key, 'q': location, 'dt': datetime_str}
            response = self.connect_to_api(params)
            if response:
                return response['forecast']
            else:
                return None

    def save_weather_forecast(self, location, datetime_str, forecast_data):
        data = self.read_file() or {}
        data.setdefault(location, {})[datetime_str] = forecast_data
        self.write_to_file(data)
