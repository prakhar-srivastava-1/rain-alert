from secrets import TWILIO_PHONE, TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, MY_PHONE
from twilio.rest import Client


class MessageClient:

    def __init__(self):
        self.account_sid = TWILIO_ACCOUNT_SID
        self.phone = TWILIO_PHONE
        self.auth_token = TWILIO_AUTH_TOKEN
        self.client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

    def send_alert(self):
        message = self.client.messages.create(
            body="It is raining.",
            from_=TWILIO_PHONE,
            to=MY_PHONE
        )
        print(message.sid)
