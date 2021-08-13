from data import WeatherData
from message_client import MessageClient


# weather_data = WeatherData()
# weather_codes = weather_data.weather_data
# print(weather_codes)
#
#
# # check if its raining
# for code in weather_codes:
#     if code < 700:
#         print("It's raining")
#         break

message_client = MessageClient()
message_client.send_alert()
