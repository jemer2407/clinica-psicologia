from django import forms
from .models import Appointment


class AppointmentForm(forms.ModelForm):
    
    class Meta:
        model = Appointment
        fields = '__all__'
                
        widgets = {
            'patient': forms.Select(attrs={'class':'form-control'}),
            'professional': forms.Select(attrs={'class':'form-control'}),
            'date': forms.DateInput(attrs={'class':'form-control id_date', 'type': 'text', 'id':'id_date'}),
            'time': forms.TimeInput(attrs={'class':'form-control id_date', 'type': 'time', 'id':'id_time'}),
            
            
        }
        labels = {
            'patient':'Paciente', 
            'professional': 'Profesional',
            'date': 'Fecha',
            'time': 'Hora'
            
        }
    
    