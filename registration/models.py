from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


def custom_upload_to(instance, filename):
    old_instance = Profile.objects.get(pk=instance.pk)
    old_instance.avatar.delete()
    return 'profile/' + filename

# Create your models here.

# Modelo para el perfil de usuario
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(verbose_name='Imagen de perfil', upload_to=custom_upload_to, null=True, blank=True)
    bio = models.TextField(verbose_name='Biografía', null=True, blank=True)
    link = models.URLField(verbose_name='Enlace', max_length=200, null=True, blank=True)

    class Meta:
        ordering = ['user__username']

@receiver(post_save, sender=User)
def ensure_profile_exists(sender, instance, **kwargs):
     
     """print(f'Kwargs:{kwargs}')
     print(kwargs.get('created', False))"""
     if kwargs.get('created', False):
        Profile.objects.get_or_create(user=instance)
        