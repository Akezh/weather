# from django.http import HttpResponse
import requests
from django.shortcuts import render
from .models import City

def index(request):
  url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=535ba2a3c695c636ae722cc1f7ff3ed3'
  city = 'Astana'

  cities = City.objects.all()

  weather_data = []

  for city in cities:
    r = requests.get(url.format(city)).json()

    city_weather = {
      'city': city,
      'temperature': r['main']['temp'],
      'description': r['weather'][0]['description'],
      'icon': r['weather'][0]['icon']
    }

    weather_data.append(city_weather)
  print (weather_data)

  context = {'city_weather' : city_weather}
  
  return render(request, 'weather/weather.html', context)