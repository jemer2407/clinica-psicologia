from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from .models import Patient, Company
from .forms import PatientForm, CompanyForm
from professionals.models import Professional

# Create your views here.

@method_decorator(staff_member_required, name='dispatch')
class PatientListView(ListView):
    model = Patient
    template_name = 'patients/patients_list.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Pacientes'
        return context

@method_decorator(staff_member_required, name='dispatch')
class PatientCreateView(CreateView):
    model = Patient
    form_class = PatientForm
    template_name = 'patients/patient_form.html'
    success_url = reverse_lazy('patients-list')

# vista para editar un paciente
@method_decorator(staff_member_required, name='dispatch')
class PatientUpdateView(UpdateView):
    model = Patient
    form_class = PatientForm
    template_name = 'patients/patient_form.html'
    success_url = reverse_lazy('patients-list')

# vista para eliminar un paciente
@method_decorator(staff_member_required, name='dispatch')
class PatientDeleteView(DeleteView):
    model = Patient
    template_name = 'patients/patient_confirm_delete.html'
    success_url = reverse_lazy('patients-list')


# ------------- vistas para companies -------------
@method_decorator(staff_member_required, name='dispatch')
class CompanyListView(ListView):
    model = Company
    template_name = 'companies/company_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Compañías Médicas'
        return context
    
@method_decorator(staff_member_required, name='dispatch')
class CompanyCreateView(CreateView):
    model = Company
    form_class = CompanyForm
    template_name = 'companies/company_form.html'
    success_url = reverse_lazy('companies-list')

# vista para editar un paciente
@method_decorator(staff_member_required, name='dispatch')
class CompanyUpdateView(UpdateView):
    model = Company
    form_class = CompanyForm
    template_name = 'companies/company_form.html'
    success_url = reverse_lazy('companies-list')

# vista para eliminar un paciente
@method_decorator(staff_member_required, name='dispatch')
class CompanyDeleteView(DeleteView):
    model = Company
    template_name = 'companies/company_confirm_delete.html'
    success_url = reverse_lazy('companies-list')

# vista para listar todos los pacientes que tiene un profesional
@method_decorator(staff_member_required, name='dispatch')
class PatientsOfProfessionalListView(ListView):
    model = Patient
    #template_name = 'patients/patients_professional_list.html'
    template_name = 'patients/patients_list.html'
    
    def get_queryset(self):
        self.professional_id = get_object_or_404(Professional, id=self.kwargs['pk'])
        print(self.professional_id)
        return Patient.objects.filter(professional=self.professional_id)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Pacientes de {}'.format(Professional.objects.get(id=self.kwargs['pk'])) 
        return context
    