from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from django.core.mail import EmailMessage
import datetime
import holidays

from .models import Appointment
from patients.models import Patient
from .forms import AppointmentForm

def send_email(subject, message, patient, appointment):
    
    
    email = EmailMessage(
                    subject,
                    message.format(patient, appointment.date, appointment.time, appointment.professional),
                    "no-contestar@clinica-psicologia.com",
                    [patient.email],
                    #reply_to=[subscriber.email]
                )
    try:
        email.send()
        # Todo ha ido bien y rediccionamos a ok
        return True
        #return redirect(reverse_lazy('appointment-list') + "?ok")
    
    except:
        # algo no ha ido bien y rediccionamos a FAIL
        return False
        #return redirect(reverse_lazy('appointment-list') + "?fail")
    

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
        
        return context
    
    def form_valid(self, form):
        response = super().form_valid(form)
        appointment = self.object
        patient = Patient.objects.get(id=appointment.patient.id)
        subject = "Clínica Psicología: Nueva cita"
        message = "Hola {},\n\n usted tiene cita el {} a las {} con {} "
        
        if send_email(subject, message, patient, appointment):
            return redirect(reverse_lazy('appointment-list') + "?createok")
        else:
            return redirect(reverse_lazy('appointment-list') + "?createfail")
        

        #return response
    

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
    
    def form_valid(self, form):
        response = super().form_valid(form)
        appointment = self.object
        patient = Patient.objects.get(id=appointment.patient.id)
        subject = "Clínica Psicología: Modificación de cita"
        message = "Hola {},\n\n Su cita ha sido modificada al {} a las {} con {} "
        
        if send_email(subject, message, patient, appointment):
            return redirect(reverse_lazy('appointment-list') + "?updateok")
        else:
            return redirect(reverse_lazy('appointment-list') + "?updatefail")

# vista para editar una cita
class AppointmentDeleteView(DeleteView):
    model = Appointment
    template_name = 'appointment/appointment_confirm_delete.html'
    success_url = reverse_lazy('appointment-list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminar Cita'
        
        return context
    
    def form_valid(self, form):
        response = super().form_valid(form)
        appointment = self.object
        patient = Patient.objects.get(id=appointment.patient.id)
        subject = "Clínica Psicología: Cancelación de cita"
        message = "Hola {},\n\n Su cita del {} a las {} con {} ha sido cancelada"
        if send_email(subject, message, patient, appointment):
            return redirect(reverse_lazy('appointment-list') + "?deleteok")
        else:
            return redirect(reverse_lazy('appointment-list') + "?deletefail")

