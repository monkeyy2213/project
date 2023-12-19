from django.contrib import admin

from .models import *

class OwnerAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth')

class PatientAdmin(admin.ModelAdmin):
    list_display = ('name', 'date_of_birth')

admin.site.register(Owner, OwnerAdmin)
admin.site.register(Patient, PatientAdmin)