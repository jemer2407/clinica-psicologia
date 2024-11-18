from django import forms
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from .models import Specialty


class SpecialtyForm(forms.ModelForm):
    
    class Meta:
        model = Specialty
        fields = '__all__'
        specialtys = Specialty.objects.all()
                
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Nombre'}),
            'description': SummernoteWidget(
                  attrs={"class": "form-control mt-3"}),
            'image': forms.ClearableFileInput(attrs={
                'class': 'form-control-file mt-3'})
            
        }
        labels = {
            'name':'', 
            'description':'Descripción', 
            'image':'Imagen'
            
        }
