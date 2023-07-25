import os

from twilio.rest import Client

account_sid = '[auth_account]'
auth_token = '[auth_token]'
client = Client(account_sid, auth_token)


message = client.messages \
    .create(
        body='This SMS is sent by python code',
        from_='Number_By_Twilio',
        to='Your_Phone_Number'
        )  


print(message.sid)
print("Message sent")