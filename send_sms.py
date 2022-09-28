# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = 'AC472a5bf38d07e89fe5af094bb5224975'
auth_token = '75c9ef972e5c9a5498faf8e1a9331e0e'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Hello Blink. Congrats on your first Twilio message",
                     from_='+12172752124',
                     to='+2348147456430'
                 )

print(message.sid)
