import os
from secrets import TWILIO_PHONE, TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, MY_PHONE
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient


class MessageClient:

    def __init__(self):
        self.account_sid = TWILIO_ACCOUNT_SID
        self.phone = TWILIO_PHONE
        self.auth_token = TWILIO_AUTH_TOKEN
        self.my_phone = MY_PHONE
        proxy_client = TwilioHttpClient()
        proxy_client.session.proxies = {'https': os.environ['https_proxy']}

        self.client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, http_client=proxy_client)

    def send_alert(self):

        message = self.client.messages.create(
            body="It is going to rain today. Remember to bring an umbrella.",
            from_=self.phone,
            to=self.my_phone
        )
        print(message.status)
