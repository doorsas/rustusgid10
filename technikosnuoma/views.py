from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .forms import TechnikaForm
from .models import Technika


class ApiePageView(TemplateView):
    template_name = 'technikosnuoma/apie.html'

class NuomojuPageView(TemplateView):
    template_name = 'technikosnuoma/nuomoju.html'

class IeskauPageView(ListView):
    template_name = 'technikosnuoma/ieskaunuomotis.html'
    model = Technika
    ordering = ['-id']
    context_object_name = 'visatechnika'

class TechnikaDetailView(DetailView):
    model = Technika
    template_name = 'technikosnuoma/technika_detaliau.html'

class AddTechnikaView(CreateView):
    model = Technika
    form_class = TechnikaForm
    template_name = 'technikosnuoma//prideti_technika.html'