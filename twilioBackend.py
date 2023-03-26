# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client

# Set environment variables for your credentials
# Read more at http://twil.io/secure

account_sid = "AC1b7e9265d043418313fa0a98d23d2d86"
auth_token = "b3dbc190f40d0d7338e7a09241d5cd7c"
client = Client(account_sid, auth_token)
User = "Ronald Santos Garcia"
call_purpose = "appointment"
reason = "late"
eta = "10 Minutes"
say = "" 
outBound = "+15712450024"
if reason == "late": 
  say= "Hello this is {} and I am running late to my {}. My Estimated Time is {}".format(User, call_purpose,eta )

elif reason == "accident": 
  say = "Hey, I am not going to be able to make it. I was in accident. I am okay,I won't be able to return your calls."
elif reason == "cannot come": 
  say = "Cannot come to our event. Something came up. I will came back later and explain everything."
  
  
  
  
  
  

call = client.calls.create(
  
  twiml='<Response>  <Pause length="3"/><Say> {}</Say></Response>'.format(say),
  to=outBound,
  from_="+18665253387"
)

print(call.sid)