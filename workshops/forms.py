from django import forms
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from .models import Workshop


class WorkshopForm(forms.ModelForm):
    
    class Meta:
        model = Workshop
        fields = '__all__'
                
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Nombre'}),
            'description': SummernoteWidget(
                  attrs={"class": "form-control mt-3"}),
            'specialty': forms.Select(attrs={'class':'form-control'}),
            'professional': forms.Select(attrs={'class':'form-control'}),
            'date': forms.DateTimeInput(attrs={'class':'form-control', 'type': 'datetime-local'}),
            
        }
        labels = {
            'name':'', 
            'description':'Descripción', 
            'specialty': 'Especialidad',
            'professional': 'Profesional',
            'date': 'Fecha y hora'
            
        }