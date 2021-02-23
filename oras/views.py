from django.shortcuts import render

def oras(request):
    return render(request, 'oras/oras.html', {})