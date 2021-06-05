import requests
from twilio.rest import Client

api_key = "YOUR_OPENWEATHER_API_KEY"
account_sid = "YOUR_TWILIO_ACCOUNT_SID"
auth_token = "YOUR_TWILIO_AUTH_TOKEN"

parameters = {
    "lat": 41.997345,
    "lon": 21.427996,
    "appid": api_key,
    "exclude": "current,minutely,daily,alerts"
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()
data = response.json()
weather_state = []
for i in range(13):
    hourly_id = data["hourly"][i]["weather"][0]["id"]
    weather_state.append(hourly_id)

if min(weather_state) < 700:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an ☂.",
        from_="YOUR_TWILIO_NUMBER",
        to="YOUR_PHONE_NUMBER"
    )
    print(message.status)
