from django.contrib import admin
from .models import SpecializationModel
from .models import DesignationModel
from .models import AvailableTimeModel
from .models import DoctorModel
from .models import ReviewModel
# Register your models here.

class SpecializationAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}  # Auto-fill slug from name in admin panel

class DesignationModelAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}  # Auto-fill slug from name in admin panel


admin.site.register(SpecializationModel, SpecializationAdmin)
admin.site.register(DesignationModel, DesignationModelAdmin)
admin.site.register(AvailableTimeModel)
admin.site.register(DoctorModel)
admin.site.register(ReviewModel)