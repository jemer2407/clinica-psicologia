# Generated by Django 5.1.3 on 2024-11-16 06:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0002_appointment_hora_alter_appointment_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appointment',
            old_name='hora',
            new_name='time',
        ),
    ]
