from django.shortcuts import render, redirect
from .models import Klausimai, City
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
import requests
from .forms import CityForm


def oras(request):
    url = 'https://api.meteo.lt/v1/places/{}/forecasts/long-term'

    err_msg = ''
    message = ''
    message_class = ''


    if request.method == 'POST':
        form = CityForm(request.POST)

        if form.is_valid():
            new_city = form.cleaned_data['name']
            existing_city_count = City.objects.filter(name = new_city).count()

            if existing_city_count == 0:
                r = requests.get(url.format(new_city)).json()
                print (len(r))
                if len(r) == 1:
                    err_msg = "Nėra tokio miesto"
                else:
                    form.save()
            else:
                err_msg = "Toks miestas jau pridėtas"
        if err_msg:
            message = err_msg
            message_class = 'is-danger'
        else:
            message = "Miestas sėkmingai pridėtas"
            message_class = 'is-success'



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
            'dregme' : r['forecastTimestamps'][0]['relativeHumidity'],

        }

        weather_data.append(city_weather)
        # print(weather_data)
    context = {
        'weather_data': weather_data,
        'form': form,
        'message': message,
        'message_class' : message_class,
                }

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

    err_msg = ''
    message = ''
    message_class = ''


    if request.method == 'POST':
        form = CityForm(request.POST)

        if form.is_valid():
            new_city = form.cleaned_data['name']
            existing_city_count = City.objects.filter(name = new_city).count()

            if existing_city_count == 0:
                r = requests.get(url.format(new_city)).json()
                print (len(r))
                if len(r) == 1:
                    err_msg = "Nėra tokio miesto"
                else:
                    form.save()
            else:
                err_msg = "Toks miestas jau pridėtas"
        if err_msg:
            message = err_msg
            message_class = 'is-danger'
        else:
            message = "Miestas sėkmingai pridėtas"
            message_class = 'is-success'



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
            'dregme' : r['forecastTimestamps'][0]['relativeHumidity'],

        }

        weather_data.append(city_weather)
        # print(weather_data)
    context = {
        'weather_data': weather_data,
        'form': form,
        'message': message,
        'message_class' : message_class,
                }

    return render(request, 'oras/oro_prognoze.html', context)


def delete_city(request, city_name):
    City.objects.get(name=city_name).delete()
    return redirect('oras')

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