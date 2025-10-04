# 🌦️ Rain Alert with Twilio SMS

This is **Day 35 of the Python Bootcamp** 🐍💻.  
The project checks the weather forecast using the **OpenWeatherMap API** 🌍 and sends you an **SMS alert via Twilio** 📲 if it’s going to rain.  
Perfect for making sure you never forget your umbrella ☔ again!

---

## 🚀 How It Works

1. **Fetch Weather Data** 🌤️

   - Uses the [OpenWeatherMap Forecast API](https://openweathermap.org/forecast5) to get hourly weather forecasts for a specific location.
   - The script checks the next **4 time intervals** (`cnt=4`) for rain.

2. **Check Rain Condition** 🌧️

   - Each weather condition has a numeric code (`id`).
   - If the code is **less than 700**, that means rain, snow, or drizzle → you’ll get an alert.

3. **Send SMS via Twilio** 📞
   - If rain is detected, Twilio sends you a text message:
     > "It's going to rain today. Remember to bring an ☔"

---

## 📂 Code Breakdown

```python
import requests
from twilio.rest import Client
```

👉 Importing required libraries:

- `requests` for making API calls
- `twilio` for sending SMS

```python
weather_endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "YOUR_OPENWEATHERMAP_API_KEY"
account_sid = "YOUR_TWILIO_ACCOUNT_SID"
auth_token = "YOUR_TWILIO_AUTH_TOKEN"
```

👉 API keys and authentication details. Replace these with your own 🔑.

```python
parameters = {
    "appid": api_key,
    "lat": 44.389355,   # Latitude 🌍
    "lon": -79.690331,  # Longitude 🌍
    "cnt": 4,           # How many forecast intervals to check
}
```

👉 Setting location and request parameters.

```python
response = requests.get(weather_endpoint, params=parameters)
response.raise_for_status()
weather_data = response.json()
```

👉 Fetching forecast data and converting it into JSON format.

```python
will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
```

👉 Looping through forecast data to see if rain is expected.

```python
if will_rain:
    message = client.messages.create(
        body="It's going to rain today. Remember to bring an ☔",
        from_="+YOUR_TWILIO_PHONE_NUMBER",
        to="+YOUR_VERIFIED_PHONE_NUMBER",
    )
    print(message.status)
```

👉 If rain is detected, Twilio sends an SMS. The status of the message (`queued`, `sent`, etc.) is printed.

---

## 🛠️ Requirements

- Python 3 🐍
- `requests` → `pip install requests`
- `twilio` → `pip install twilio`
- OpenWeatherMap API key
- Twilio account with a phone number

---

## ⚠️ Notes

- On **Twilio free trial**, you can only send SMS to verified numbers ✅.
- If running on **PythonAnywhere free plan**, Twilio SMS may not work due to internet restrictions 🚫. Run locally or upgrade plan.

---
