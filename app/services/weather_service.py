import requests
import os

#API_KEY = os.getenv("API_KEY") or "YOUR_API_KEY"  # fallback for local testing
API_KEY = "5537a5a11a993db5b9dd98184ff0363b"

def get_weather_data(city="Delhi"):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    try:
        response = requests.get(url)
        data = response.json()

        # ✅ Handle API errors safely
        if response.status_code != 200 or "main" not in data:
            print("Weather API error:", data)
            return {
                "temperature": 25,
                "humidity": 60,
                "rainfall": 0,
                "note": "Default weather used"
            }

        return {
            "temperature": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "rainfall": data.get("rain", {}).get("1h", 0)
        }

    except Exception as e:
        print("Weather service error:", e)
        return {
            "temperature": 25,
            "humidity": 60,
            "rainfall": 0,
            "note": "Fallback weather"
        }