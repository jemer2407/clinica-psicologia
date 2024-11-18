from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Specialty, Professional

# Register your models here.

class SpecialtyAdmin(SummernoteModelAdmin):
    summernote_fields = ('description',)
    list_display = ('name',)
    

class ProfessionalAdmin(SummernoteModelAdmin):
    summernote_fields = ('resume',)
    list_display = ('name', 'surnames')


admin.site.register(Specialty, SpecialtyAdmin)
admin.site.register(Professional, ProfessionalAdmin)




