from django.db import models

# Create your models here.

class Specialty(models.Model):
    name = models.CharField(max_length=200, verbose_name='Nombre')
    description = models.TextField(verbose_name='Descripción', null=True, blank=True)
    image = models.ImageField(verbose_name='Imagen', upload_to='specialty', null=True, blank=True)

    class Meta:
        verbose_name = 'Especialidad'
        verbose_name_plural = 'Especialidades'
        
    
    def __str__(self):
        return self.name