from twilio.rest import Client

TWILIO_SID = "....."
TWILIO_AUTH_TOKEN = "....."


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message_body):
        message = self.client.messages.create(
            from_=".....",
            body=message_body,
            to='.....'
        )

        print(message.sid)

    def send_whatsapp(self, message_body):
        message = self.client.messages.create(
            from_="whatsapp:+.....",
            body=message_body,
            to='whatsapp:+.....'
        )
