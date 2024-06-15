# outfit_recommendation.py

def recommend_outfit(weather_data):
    temperature = weather_data['main']['temp']
    humidity = weather_data['main']['humidity']
    weather_condition = weather_data['weather'][0]['main']

    if weather_condition == 'Rain':
        return "Bring an umbrella and wear a light jacket."
    elif temperature < 10:
        return "Wear a heavy coat."
    elif temperature >= 10 and temperature < 20:
        return "Wear a light jacket."
    else:
        return "Weather is pleasant. Wear as you like!"

