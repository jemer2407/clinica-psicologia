from django.db import models
from professionals.models import Professional

# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nombre')

    class Meta:
        verbose_name = 'Compañía'
        verbose_name_plural = 'Compañías'
        ordering = ['name']
        
    
    def __str__(self):
        return self.name

class Patient(models.Model):
    name = models.CharField(max_length=50, verbose_name='Nombre')
    surnames = models.CharField(max_length=100, verbose_name='Apellidos')
    company = models.ForeignKey(Company, verbose_name='Compañía Seguro', blank=True, null=True, on_delete=models.CASCADE)
    professional = models.ForeignKey(Professional, on_delete=models.CASCADE, verbose_name='Profesional')
    email = models.EmailField(verbose_name='Email', max_length=100, null=True, blank=True)

    class Meta:
        verbose_name = 'Paciente'
        verbose_name_plural = 'Pacientes'
        ordering = ['name']
        
    
    def __str__(self):
        return '{} {}'.format(self.name.title(), self.surnames.title())
        


