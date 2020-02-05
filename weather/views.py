from django.shortcuts import render
from .forms import CityForm
from .models import City
import requests

def index(request):
  url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=535ba2a3c695c636ae722cc1f7ff3ed3'
  
  if request.method == 'POST':
    form = CityForm(request.POST)
    form.save()
    
  form = CityForm()

  cities = City.objects.all()
  weather_data = []

  for city in cities:
    r = requests.get(url.format(city)).json()

    city_weather = {
      'city': city.name,
      'temperature': r['main']['temp'],
      'description' : r['weather'][0]['description'],
      'icon' : r['weather'][0]['icon'],
    }

    weather_data.append(city_weather)

  context = {'weather_data' : weather_data, 'form' : form}
  return render(request, 'weather/weather.html', context)
