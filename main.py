import requests
from secrets import API_KEY

owm_endpoint = "https://api.openweathermap.org/data/2.5/onecall"
parameters = {
    'lat': '22.17',
    'lon': '76.06',
    'appid': API_KEY,
}

response = requests.get(owm_endpoint, params=parameters)
response.raise_for_status()
print(response.status_code)
