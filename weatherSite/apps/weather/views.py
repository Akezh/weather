# from django.http import HttpResponse
import requests
from django.shortcuts import render

def index(request):
  url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=535ba2a3c695c636ae722cc1f7ff3ed3'
  city = 'Las Vegas'

  r = requests.get(url.format(city)).json()

  city_weather = {
    'city': city,
    'temperature': r['main']['temp'],
    'description': r['weather'][0]['description'],
    'icon': r['weather'][0]['icon']
  }

  context = {'city_weather' : city_weather}
  
  # return render(request, "weather/weather.html")
  return render(request, 'weather/weather.html', context)