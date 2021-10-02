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
will_rain = False

response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]
for hourly_data in weather_slice:
    condition_data = hourly_data["weather"][0]["id"]
    if condition_data in range(500, 700):
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an ☂.",
        from_="YOUR_TWILIO_NUMBER",
        to="YOUR_PHONE_NUMBER"
    )
    print(message.status)
