from django.contrib import admin
from .models import Patient

# Register your models here.

class PatientAdmin(admin.ModelAdmin):
    list_display = ('name', 'surnames', 'company', 'professional')


admin.site.register(Patient, PatientAdmin)
