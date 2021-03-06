from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from . import views
from .views import KlausimaiPageView


urlpatterns = [
    path('', views.oras, name= 'oras'),
    path('temperatura/', KlausimaiPageView.as_view(), name= 'oro_temperatura'),
    path('prognoze/', views.index, name= 'prognoze'),
    path('delete/<city_name>', views.delete_city, name= 'delete_city'),
    path('kamuolys/', views.kamuolys, name= 'kamuolys'),
    path('chess/', views.chess, name= 'chess')
]

