from django.db import models

# Create your models here.

class Subscriber(models.Model):
    name = models.CharField(max_length=50, verbose_name='Nombre')
    email = models.EmailField(max_length=100, verbose_name='Email')

    class Meta:
        verbose_name = 'Suscriptor'
        verbose_name_plural = 'Suscriptores'
        ordering = ['name']
        
    
    def __str__(self):
        return self.name