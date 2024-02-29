"""from .models import AD_TypeIdentification, AD_Nationality, AD_City, AD_Sex, AD_EducationLevel, AD_TelephoneCompany, AD_Profile
from django.db.models.signals import pre_save
from django.dispatch import receiver
#from Users.models import USR_User


@receiver(pre_save, sender=AD_Profile)
@receiver(pre_save, sender=AD_TypeIdentification)
@receiver(pre_save, sender=AD_Nationality)
@receiver(pre_save, sender=AD_City)
@receiver(pre_save, sender=AD_Sex)
@receiver(pre_save, sender=AD_EducationLevel)
@receiver(pre_save, sender=AD_TelephoneCompany)
def set_created_by_or_updated_by(sender, instance, **kwargs):
    if not instance.pk:  # Si es un nuevo registro
        # Asignar el usuario que está creando el registro
        # Aquí se asume que la solicitud HTTP está disponible
        #instance.createdby = kwargs['request'].user  # Obtener el usuario actual de la solicitud HTTP
        instance.createdby = instance.updatedby = kwargs['user']
    else:
        # No permitir que se modifique el campo createdby cuando se actualiza el registro
        instance.createdby = instance.createdby
        # Asignar el usuario que está actualizando el registro
        instance.updatedby = kwargs['user']    # Obtener el usuario actual de la solicitud HTTP"""
