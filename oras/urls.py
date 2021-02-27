from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from . import views
from .views import KlausimaiPageView


urlpatterns = [
    path('', views.oras, name= 'oras'),
    path('temperatura/', KlausimaiPageView.as_view(), name= 'oro_temperatura'),
    path('prognoze/', views.index, name= 'prognoze')
]

