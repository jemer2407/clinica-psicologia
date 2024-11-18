from django.db import models
from specialtys.models import Specialty
from professionals.models import Professional

# Create your models here.

class Workshop(models.Model):
    name = models.CharField(max_length=50, verbose_name='Nombre')
    description = models.TextField(verbose_name='Descripción')
    specialty = models.ForeignKey(Specialty, verbose_name='Especialidad', on_delete=models.CASCADE)
    professional = models.ForeignKey(Professional, on_delete=models.CASCADE, verbose_name='Profesional')
    date = models.DateTimeField(verbose_name='Fecha', null=True, blank=True)

    class Meta:
        verbose_name = 'Taller'
        verbose_name_plural = 'Talleres'
        ordering = ['name']
        
    
    def __str__(self):
        return self.name