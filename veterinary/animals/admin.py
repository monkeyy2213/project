from django.contrib import admin

from .models import *

class OwnerAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name')

class PatientAdmin(admin.ModelAdmin):
    list_display = ('name', 'date_of_birth')

# class VeterinarianAdmin(admin.ModelAdmin):
#     list_display = ('last_name', 'first_name')

# class VisitAdmin(admin.ModelAdmin):
#     list_display = ('visit_date', 'patient')

# class ServiceAdmin(admin.ModelAdmin):
#     list_display = ('name')

# class ProvidedServiceAdmin(admin.ModelAdmin):
#     list_display = ('service', 'date')

# class AnamnesisAdmin(admin.ModelAdmin):
#     list_display = ('patient', 'visit')

admin.site.register(Owner, OwnerAdmin)
admin.site.register(Patient, PatientAdmin)
# admin.site.register(Veterinarian, VeterinarianAdmin)
# admin.site.register(Visit, VisitAdmin)
# admin.site.register(Service, ServiceAdmin)
# admin.site.register(ProvidedService, ProvidedServiceAdmin)
# admin.site.register(Anamnesis, AnamnesisAdmin)
