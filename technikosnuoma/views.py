from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy




class ApiePageView(TemplateView):
    template_name = 'technikosnuoma/apie.html'

class NuomojuPageView(TemplateView):
    template_name = 'technikosnuoma/nuomoju.html'

class IeskauPageView(TemplateView):
    template_name = 'technikosnuoma/ieskaunuomotis.html'

