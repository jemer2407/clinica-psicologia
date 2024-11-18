from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from .models import Specialty
from .forms import SpecialtyForm

# Create your views here.

class SpecialtyListView(ListView):
    model = Specialty
    template_name = 'specialtys/specialty_list.html'

class SpecialtyDetailView(DetailView):
    model = Specialty
    template_name = 'specialtys/specialty_detail.html'


# -------------- vista para listar las especialidades con usuario logueado --------------
class LoginSpecialtyListView(ListView):
    model = Specialty
    template_name = 'specialtys/specialty_maintenance_list.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Especialidades'
        return context

# vista para crear una especialidad
class SpecialtyCreateView(CreateView):
    model = Specialty
    form_class = SpecialtyForm
    template_name = 'specialtys/specialty_form.html'
    success_url = reverse_lazy('specialtys-maintenance-list')

# vista para editar una especialidad
class SpecialtyUpdateView(UpdateView):
    model = Specialty
    form_class = SpecialtyForm
    template_name = 'specialtys/specialty_form.html'
    success_url = reverse_lazy('specialtys-maintenance-list')

# vista para eliminar una especialidad
class SpecialtyDeleteView(DeleteView):
    model = Specialty
    template_name = 'specialtys/specialty_confirm_delete.html'
    success_url = reverse_lazy('specialtys-maintenance-list')