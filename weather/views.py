import requests
from django.shortcuts import render


def index(request):
  url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=d30eb513f3e2d8a6996e9d83bfcdd779'
  city = 'London'
    
  r = requests.get(url.format(city)).json()

  city_weather = {
            'city' : city,
            'temperature' : r['main']['temp'],
            'description' : r['weather'][0]['description'],
            'icon' : r['weather'][0]['icon'],
        }


  context = {'city_weather' : city_weather}
  return render(request, 'weather/weather.html', context)