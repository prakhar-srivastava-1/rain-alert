import requests
from secrets import API_KEY


class WeatherData:

    def __init__(self):
        self.owm_endpoint = "https://api.openweathermap.org/data/2.5/onecall"
        self.parameters = {
            'lat': '22.17',
            'lon': '76.06',
            'appid': API_KEY,
            'exclude': 'current,minutely,daily',
        }
        self.weather_data = self.grab_codes()

    def get_response(self):
        response = requests.get(self.owm_endpoint, params=self.parameters)
        response.raise_for_status()
        weather_data = response.json()["hourly"]
        return weather_data[:12]

    def grab_codes(self):
        weather_json = self.get_response()
        codes = [hour["weather"][0]["id"] for hour in weather_json]
        return codes
