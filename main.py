import requests
from twilio.rest import Client

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "2ff023be979a63fba59486521ccde85e"
account_sid = 'AC976a363d76bf84618e671fe77dfa53b9'
auth_token = '05676e6139e2162e2dd9a98dbe1a3af9'
client = Client(account_sid, auth_token)

weather_para = {
    "lat": 21.145800,
    "lon": 79.088158,
    "appid": api_key,
    "cnt": 4,
}

response = requests.get(OWM_Endpoint, params=weather_para)
weather_data = response.json()
# print(weather_data["list"][0]["weather"][0]["id"])
will_rain = False
for hr_data in weather_data["list"]:
    condition_code = hr_data["weather"][0]["id"]
    if int(condition_code) < 700:
        # print("Bring a umbrella.")
        will_rain =True

if will_rain:
    message = client.messages.create(
        body="Hello papa",
        from_='+12532525823',
        to='+919737638450'
    )
    print(message.status)