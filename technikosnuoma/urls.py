from django.urls import path

from .views import ApiePageView, NuomojuPageView, IeskauPageView, TechnikaDetailView, AddTechnikaView

urlpatterns = [
    path('', ApiePageView.as_view(), name='pradinis'),
    path('nuomoju/', NuomojuPageView.as_view(), name='nuomoju'),
    path('ieskaunuomai/', IeskauPageView.as_view(), name='ieskau'),
    path('technika/<int:pk>', TechnikaDetailView.as_view(), name='technika_detaliau'),
    path('prideti_technika/', AddTechnikaView.as_view(), name='prideti_technika')
    ]