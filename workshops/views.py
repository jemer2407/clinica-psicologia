from django.shortcuts import render, get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from .models import Workshop
from professionals.models import Professional
from specialtys.models import Specialty
from .forms import WorkshopForm
# Create your views here.

class WorkshopListView(ListView):
    model = Workshop
    template_name = 'workshop/workshop_list.html'
    ordering = ['professional',]

class WorkshopDetailView(DetailView):
    model = Workshop
    template_name = 'workshop/workshop_detail.html'


class WorkshopProfessionalListView(ListView):
    model = Workshop
    template_name = 'workshop/workshops_by_filter_list.html'

    def get_queryset(self):
        professional_id = get_object_or_404(Professional, id=self.kwargs['pk'])
        return Workshop.objects.filter(professional=professional_id)

class WorkshopSpecialtyListView(ListView):
    model = Workshop
    template_name = 'workshop/workshops_by_filter_list.html'

    def get_queryset(self):
        specialty_id = get_object_or_404(Specialty, id=self.kwargs['pk'])
        return Workshop.objects.filter(specialty=specialty_id)

# ------------ vista para listar los talleres con usuario logueado ---------------
class LoginWorkshopListView(ListView):
    model = Workshop
    template_name = 'workshop/workshop_maintenance_list.html'
    ordering = ['professional',]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Talleres'
        return context

# vista para crear un taller
class WorkshopCreateView(CreateView):
    model = Workshop
    form_class = WorkshopForm
    template_name = 'workshop/workshop_form.html'
    success_url = reverse_lazy('workshops-maintenance-list')

# vista para editar un taller
class WorkshopUpdateView(UpdateView):
    model = Workshop
    form_class = WorkshopForm
    template_name = 'workshop/workshop_form.html'
    success_url = reverse_lazy('workshops-maintenance-list')

# vista para eliminar una especialidad
class WorkshopDeleteView(DeleteView):
    model = Workshop
    template_name = 'workshop/workshop_confirm_delete.html'
    success_url = reverse_lazy('workshops-maintenance-list')


class LoginWorkshopProfessionalListView(ListView):
    model = Workshop
    template_name = 'workshop/workshop_maintenance_list.html'

    def get_queryset(self):
        professional_id = get_object_or_404(Professional, id=self.kwargs['pk'])
        return Workshop.objects.filter(professional=professional_id)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Talleres que imparte {}'.format(Professional.objects.get(id=self.kwargs['pk'])) 
        return context