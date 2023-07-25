import os

from twilio.rest import Client

account_sid = 'AC79dbf2e53290d2423b9e7faaae18e0bf'
auth_token = '[AuthToken]'
client = Client(account_sid, auth_token)


message = client.messages \
    .create(
        body='This SMS is sent by python code',
        from_='+12295455397',
        to='+916239619772'
        )  


print(message.sid)