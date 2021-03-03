from django.urls import path

from .views import ApiePageView, NuomojuPageView, IeskauPageView



urlpatterns = [
    path('', ApiePageView.as_view(), name='pradinis'),
    path('nuomoju/', NuomojuPageView.as_view(), name='nuomoju'),
    path('ieskaunuomai/', IeskauPageView.as_view(), name='ieskau'),
    ]