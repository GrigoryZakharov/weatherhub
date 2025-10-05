import os
import requests

API_KEY = os.getenv("OPENWEATHER_API_KEY")

def fetch_weather(city: str):
    API_KEY = os.getenv("OPENWEATHER_API_KEY")
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    try:
        resp = requests.get(url, timeout=5)
        data = resp.json()
        if resp.status_code != 200 or "main" not in data:
            raise ValueError(f"Ошибка API: {resp.status_code}, ответ: {data}")
        return {
            "city": city,
            "temperature": data["main"]["temp"],
            "description": data["weather"][0]["description"]
        }
    except requests.RequestException as e:
        print(f"[ERROR] Не удалось получить погоду для {city}: {e}")
        return None
