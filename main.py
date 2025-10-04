import  requests
from twilio.rest import Client

weather_endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "81bec49d89d74ac91ce2168b807964a2"
account_sid = 'AC2db5b1f3764b4cb6c1fd78ca7d4a36ee'
auth_token = '06bbb17026d915a8d5e2f8f33064ed7e'

parameters ={
    "appid" : api_key,
    "lat" : 44.389355,
    "lon" : -79.690331,
    "cnt":4,
}
client = Client(account_sid,auth_token)

response = requests.get(weather_endpoint,params=parameters)
response.raise_for_status()
weather_data = response.json()
will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
if will_rain:
    message = client.messages.create(
        body="It's going to rain today. Remember to bring an ☔",
        from_="+18543004890",
        to="+12499892593",
    )
    print(message.status)