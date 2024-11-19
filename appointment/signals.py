from django.db.models.signals import pre_save
from django.shortcuts import redirect
from django.dispatch import receiver
from django.urls import reverse, reverse_lazy

from appointment.models import Appointment


@receiver(pre_save, sender=Appointment)
def my_handler_appointment(sender, instance, **kwargs):
    print("pre guardado")
    print(f'Kwargs:{kwargs}')
    print(instance.patient)
    if Appointment.objects.filter(date=instance.date).filter(time=instance.time):
        print('ya hay una cita con esa fecha y hora')
    else:
        print('cita con fecha y hora correcta')
    

    
        