from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
import datetime
import holidays

from .models import Appointment
from patients.models import Patient
from .forms import AppointmentForm
# Create your views here.

def obtener_proximos_5_anos():
  #Devuelve una lista con los próximos 5 años a partir del año actual.
 
  year_now = datetime.date.today().year
  return list(range(year_now, year_now + 6))

class Year:
    def __init__(self, lista):
        self.datos = lista
    
    def add_element(self, element):
        self.datos.append(element)



class AppointmentListView(ListView):
    model = Appointment
    template_name = 'appointment/appointment_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de citas'
        context['today'] = datetime.date.today().strftime("%Y-%m-%d")
        return context
    
class AppointmentPatientListView(ListView):
    model = Appointment
    template_name = 'appointment/appointment_list.html'

    def get_queryset(self):
        patient_id = get_object_or_404(Patient, id=self.kwargs['pk'])
        return Appointment.objects.filter(patient=patient_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de citas'
        return context

# vista para crear una cita
class AppointmentCreateView(CreateView):
    model = Appointment
    form_class = AppointmentForm
    template_name = 'appointment/appointment_form.html'
    success_url = reverse_lazy('appointment-list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Crear Cita'

        # obtener festivos nacionales
 
        holidays_spain = holidays.Spain(years=obtener_proximos_5_anos())

        # Convertir las fechas festivas a un formato compatible con Flatpickr
        holiday_dates = [holiday.strftime('%Y-%m-%d') for holiday in holidays_spain]
        
        context['holidays'] = holiday_dates
        print(context['holidays'])
        return context

    

# vista para editar una cita
class AppointmentUpdateView(UpdateView):
    model = Appointment
    form_class = AppointmentForm
    template_name = 'appointment/appointment_form.html'
    success_url = reverse_lazy('appointment-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Editar Cita'
        return context

# vista para editar una cita
class AppointmentDeleteView(DeleteView):
    model = Appointment
    template_name = 'appointment/appointment_confirm_delete.html'
    success_url = reverse_lazy('appointment-list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminar Cita'
        return context

