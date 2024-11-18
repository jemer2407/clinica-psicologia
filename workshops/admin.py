from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Workshop


# Register your models here.
class WorkshopAdmin(SummernoteModelAdmin):
    summernote_fields = ('description',)
    list_display = ('name', 'professional', 'specialty', 'date')


admin.site.register(Workshop, WorkshopAdmin)