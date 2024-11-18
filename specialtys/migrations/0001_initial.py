# Generated by Django 5.1.3 on 2024-11-12 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Specialty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Nombre')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Descripción')),
                ('image', models.ImageField(blank=True, null=True, upload_to='specialty', verbose_name='Imagen')),
            ],
            options={
                'verbose_name': 'Especialidad',
                'verbose_name_plural': 'Especialidades',
            },
        ),
    ]