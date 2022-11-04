import os
from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv()
account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')
numtwilio = os.getenv('TWILIOPHONE')
myphone = os.getenv('MYPHONE')

def what():
    client = Client(account_sid, auth_token)
    message = client.messages.create(
                                body='msj enviado desde venv twilio python',
                                from_=numtwilio,
                                to=myphone
                              )
    print(message.sid)

what()