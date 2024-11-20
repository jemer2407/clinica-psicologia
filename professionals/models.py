from django.db import models
from specialtys.models import Specialty

def custom_upload_to(instance, filename):
    old_instance = Professional.objects.get(pk=instance.pk)
    old_instance.avatar.delete()
    return 'profile/' + filename

# Create your models here.

class Professional(models.Model):
    name = models.CharField(max_length=50, verbose_name='Nombre')
    surnames = models.CharField(max_length=100, verbose_name='Apellidos')
    specialty = models.ManyToManyField(Specialty, verbose_name='Especialidad')
    image = models.ImageField(verbose_name='Imagen', upload_to=custom_upload_to)
    degree = models.CharField(max_length=100, verbose_name='Titulación')
    resume = models.TextField(verbose_name='Curriculum')

    class Meta:
        verbose_name = 'Profesional'
        verbose_name_plural = 'Profesionales'
        ordering = ['name']
        
    
    def __str__(self):
        return '{} {}'.format(self.name.title(), self.surnames.title())


