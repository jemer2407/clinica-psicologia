from django import forms
from django_summernote.widgets import SummernoteWidget
from .models import Professional


class ProfessionalForm(forms.ModelForm):
    
    class Meta:
        model = Professional
        fields = '__all__'
        
        
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Nombre'}),
            'surnames': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Apellidos'}),
            'specialty': forms.SelectMultiple(attrs={'class':'form-control'}),
            'image': forms.ClearableFileInput(attrs={
                'class': 'form-control-file mt-3'}),
            'degree': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Titulación'}),
            'resume': SummernoteWidget(
                  attrs={"class": "form-control"})
            
        }
        labels = {
            'name':'', 
            'surnames':'', 
            'specialty':'Especialidades', 
            'image':'Imagen', 
            'degree':'', 
            'resume': 'Curriculum'
        }
