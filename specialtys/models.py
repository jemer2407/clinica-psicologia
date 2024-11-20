from django.db import models

def custom_upload_to(instance, filename):
    old_instance = Specialty.objects.get(pk=instance.pk)
    old_instance.avatar.delete()
    return 'profile/' + filename

# Create your models here.

class Specialty(models.Model):
    name = models.CharField(max_length=200, verbose_name='Nombre')
    description = models.TextField(verbose_name='Descripción', null=True, blank=True)
    image = models.ImageField(verbose_name='Imagen', upload_to=custom_upload_to, null=True, blank=True)

    class Meta:
        verbose_name = 'Especialidad'
        verbose_name_plural = 'Especialidades'
        
    
    def __str__(self):
        return self.name