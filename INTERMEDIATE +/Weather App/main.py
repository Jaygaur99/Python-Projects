import requests
from twilio.rest import Client
import os

URL = "https://pro.openweathermap.org/data/2.5/onecall"
API_KEY = os.environ['OWM_API_KEY']
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
MY_LAT = 23.4561
MY_LONG = 75.4227


parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": API_KEY,
    "exclude": "current,minutely,daily"
}

response = requests.get(url=URL, params=parameters)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data['hourly'][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data['weather'][0]['id']
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
            body="It is going to rain today, Remember to bring your umbrella",
            from_='+15625241176',
            to='+918120567679'
    )
    print(message.status)


