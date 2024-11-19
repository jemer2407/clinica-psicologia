from django.db import models
from professionals.models import Professional
from patients.models import Patient

# Create your models here.

class Appointment(models.Model):
    patient = models.ForeignKey(Patient, verbose_name='Paciente', on_delete=models.CASCADE)
    professional = models.ForeignKey(Professional, on_delete=models.CASCADE, verbose_name='Profesional')
    date = models.DateField(verbose_name='Fecha')
    time = models.TimeField(verbose_name='Hora')


    class Meta:
        verbose_name = 'Cita'
        verbose_name_plural = 'Citas'
        ordering = ['date']
        
    
    def __str__(self):
        return self.patient


