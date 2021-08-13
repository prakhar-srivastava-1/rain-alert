from data import WeatherData
from message_client import MessageClient
from rain import will_it_rain

weather_data = WeatherData()
weather_codes = weather_data.weather_data
print(weather_codes)

if will_it_rain(weather_codes):
    message_client = MessageClient()
    message_client.send_alert()
