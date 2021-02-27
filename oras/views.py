from django.shortcuts import render
from .models import Klausimai, City
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
import requests
from .forms import CityForm


def oras(request):
    url = 'https://api.meteo.lt/v1/places/{}/forecasts/long-term'

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
            'temperature': r['forecastTimestamps'][0]['airTemperature'],
            'description': r['forecastTimestamps'][0]['windSpeed'],
            'vejo_greitis': r['forecastTimestamps'][0]['windSpeed'],
        }

        weather_data.append(city_weather)
        print(weather_data)
    context = {'weather_data': weather_data, 'form': form}
    return render(request, 'oras/oras.html', context)

# def oro_temperatura(request):
#     return render(request, 'oras/oro_temperatura.html', {})

class KlausimaiPageView(ListView):
    template_name = 'oras/oro_temperatura.html'
    model = Klausimai

# class PrognozePageView(TemplateView):
#     template_name = 'oras/oro_prognoze.html'

def index(request):
    url = 'https://api.meteo.lt/v1/places/{}/forecasts/long-term'


    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()

    form = CityForm()

    cities = City.objects.all()

    weather_data = []

    for city in cities:

        r = requests.get(url.format(city)).json()

        city_weather = {
            'city' : city.name,
            'temperature' : r['forecastTimestamps'][0]['airTemperature'],
            'description' : r['forecastTimestamps'][0]['windSpeed'],
            'vejo_greitis' : r['forecastTimestamps'][0]['windSpeed'],
        }

        weather_data.append(city_weather)
        print (weather_data)
    context = {'weather_data' : weather_data, 'form' : form}
    return render(request, 'oras/oro_prognoze.html', context)

# def gautiprognoze():
#     url = 'https://api.meteo.lt/v1/places/{}/forecasts/long-term'
#     miestas = input('Įveskite miestą :')
#     r = requests.get(url.format(miestas))
#     a = r.text
#     b = json.loads(a)
#     # print (b)
#     print (b['place']['name'])
#     oro_temperatura = str(b['forecastTimestamps'][0]['airTemperature'])
#     vejo_greitis = str(b['forecastTimestamps'][0]['windSpeed'])
#     santykine_dregme = str(b['forecastTimestamps'][0]['relativeHumidity'])
#     print ('Oro temperatūra: ' + oro_temperatura)
#     print ('Vėjo greitis: ' + vejo_greitis)
#     print ('Santykinė oro drėgmė: ' + santykine_dregme)
#     pasirinkimas = input('Dar vieną miestą ?: T arba N :')
#     if pasirinkimas == 'T':
#         gautiprognoze()
#     else:
#         exit()
# gautiprognoze()