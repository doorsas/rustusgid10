from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy




class ApiePageView(TemplateView):
    template_name = 'technikosnuoma/apie.html'
