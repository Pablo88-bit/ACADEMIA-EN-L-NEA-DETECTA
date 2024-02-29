"""from django.contrib import admin
from django.contrib.admin import AdminSite
from Administration.models import AD_City, AD_EducationLevel, AD_Nationality, AD_TelephoneCompany
from Administration.models import AD_TypeIdentification, AD_Sex, AD_Profile
# Register your models here.


class CityAdmin(admin.ModelAdmin):
    #readonly_fields = ('createdby', 'updatedby')

    def set_created_by_or_updated_by(self, request, obj, form, change):
        if not obj.pk:  # Si es un nuevo registro
            # Asignar el usuario que está creando el registro
            obj.createdby = request.user
        else:
            # Asignar el usuario que está actualizando el registro
            obj.updatedby = request.user
        super().save_model(request, obj, form, change)

admin.site.register(AD_City, CityAdmin)
admin.site.register(AD_EducationLevel)
admin.site.register(AD_Nationality)
admin.site.register(AD_TelephoneCompany)
admin.site.register(AD_TypeIdentification)
admin.site.register(AD_Sex)
admin.site.register(AD_Profile)"""
