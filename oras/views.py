from django.shortcuts import render
from .models import Klausimai
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView

def oras(request):
    return render(request, 'oras/oras.html', {})

# def oro_temperatura(request):
#     return render(request, 'oras/oro_temperatura.html', {})

class KlausimaiPageView(ListView):
    template_name = 'oras/oro_temperatura.html'
    model = Klausimai

