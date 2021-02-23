from django.shortcuts import render

def oras(request):
    return render(request, 'oras/oras.html', {})

def oro_temperatura(request):
    return render(request, 'oras/oro_temperatura.html', {})