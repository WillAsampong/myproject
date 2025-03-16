# weather/views.py
from django.shortcuts import render 
import requests

def weather_forecast(request): 
    city = 'New York' # You can change the city as needed 
    api_key = 'd30fbf48b8e0902eb2ab19455a6fd747' # Replace with your actual API key 
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}' 

    response = requests.get(url) 
    data = response.json()

    weather_description = data['weather'][0]['description'] 
    temperature_kelvin = data['main']['temp'] 
    temperature_celsius = temperature_kelvin - 273.15 

    context = { 
        'city': city,
        'description': weather_description,
        'temperature': temperature_celsius 
    }

    return render(request, 'weather/weather_forecast.html', context)
