from django import forms
from .models import Patient, Company
from professionals.models import Professional

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Nombre'}),
            'surnames': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Apellidos'}),
            'company': forms.Select(attrs={'class':'form-control'}),
            'professional': forms.Select(attrs={'class':'form-control'})
            
        }
        labels = {
            'name':'', 
            'surnames':'',
            'company': 'Compañía Médica',
            'professional':'Profesional'
        }

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Nombre'}),
            
        }
        labels = {
            'name':''
            
        }