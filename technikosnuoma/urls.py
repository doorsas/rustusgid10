from django.urls import path

from .views import ApiePageView



urlpatterns = [
    path('', ApiePageView.as_view(), name='pradinis'),
    ]