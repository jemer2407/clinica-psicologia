from django.db import models
from specialtys.models import Specialty


# Create your models here.

class Professional(models.Model):
    name = models.CharField(max_length=50, verbose_name='Nombre')
    surnames = models.CharField(max_length=100, verbose_name='Apellidos')
    specialty = models.ManyToManyField(Specialty, verbose_name='Especialidad')
    image = models.ImageField(verbose_name='Imagen', upload_to='professionals')
    degree = models.CharField(max_length=100, verbose_name='Titulación')
    resume = models.TextField(verbose_name='Curriculum')

    class Meta:
        verbose_name = 'Profesional'
        verbose_name_plural = 'Profesionales'
        ordering = ['name']
        
    
    def __str__(self):
        return '{} {}'.format(self.name.title(), self.surnames.title())


