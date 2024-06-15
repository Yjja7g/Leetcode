# weather_api.py

import requests

API_KEY = '9fd57d49dcf76d1c9f1729ebed20679f'

def get_weather_data(city):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'  # 섭씨 온도로 설정
    }
    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        weather_data = response.json()
        return weather_data
    else:
        print(f"Failed to retrieve weather data: {response.status_code}")
        return None
