from django.contrib import admin
from .models import PatientModel

class PatientModelAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'phone', 'image']

    def first_name(self, obj):
        return obj.user.first_name

    def last_name(self, obj):
        return obj.user.last_name

admin.site.register(PatientModel, PatientModelAdmin)
