from typing import Any
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from .models import Professional
from specialtys.models import Specialty
from .forms import ProfessionalForm

# Create your views here.

class ProfessionalsListView(ListView):
    model = Professional

class ProfessionalDetailView(DetailView):
    model = Professional
    template_name = 'professionals/professional_detail.html'

class ProfessionalBySpecialtyListView(ListView):
    model = Professional
    #template_name = 'patients/patients_professional_list.html'
    template_name = 'professionals/professionals_specialty_list.html'
    
    def get_queryset(self):
        specialty_id = get_object_or_404(Specialty, id=self.kwargs['pk'])
        return Professional.objects.filter(specialty=specialty_id)

# ------------------ vista para listar los profesionales en una tabla ----------------------
@method_decorator(staff_member_required, name='dispatch')
class LoginProfessionalsListView(ListView):
    model = Professional
    template_name = 'professionals/professional_maintenance_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Profesionales'
        return context

# vista para listar los profesionales de una especialidad
@method_decorator(staff_member_required, name='dispatch')
class LoginProfessionalBySpecialtyListView(ListView):
    model = Professional
    #template_name = 'patients/patients_professional_list.html'
    template_name = 'professionals/professional_maintenance_list.html'

    def get_queryset(self):
        specialty_id = get_object_or_404(Specialty, id=self.kwargs['pk'])
        return Professional.objects.filter(specialty=specialty_id)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Profesionales de la especilidad {}'.format(Specialty.objects.get(id=self.kwargs['pk'])) 
        return context

# vista para crear un profesional
@method_decorator(staff_member_required, name='dispatch')
class ProfessionalCreateView(CreateView):
    model = Professional
    form_class = ProfessionalForm
    template_name = 'professionals/professional_form.html'
    success_url = reverse_lazy('professionals-maintenance-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Crear profesional'
        return context



# vista para editar un profesional
@method_decorator(staff_member_required, name='dispatch')
class ProfessionalUpdateView(UpdateView):
    model = Professional
    form_class = ProfessionalForm
    template_name = 'professionals/professional_form.html'
    success_url = reverse_lazy('professionals-maintenance-list')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Editar profesional'
        return context
    
# vista para eliminar un profesional
@method_decorator(staff_member_required, name='dispatch')
class ProfessionalDeleteView(DeleteView):
    model = Professional
    template_name = 'professionals/professional_confirm_delete.html'
    success_url = reverse_lazy('professionals-maintenance-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminar profesional'
        return context