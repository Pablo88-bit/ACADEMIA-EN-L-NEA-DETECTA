"""from django.db import models
from django.contrib.auth.models import AbstractUser

#from Administration.models import AD_TypeIdentification, AD_Nationality, AD_City, AD_EducationLevel, AD_Sex
# Create your models here.


#AbstractUser
class USR_User(AbstractUser):
    description = models.TextField(max_length=255, null=True, blank=True, verbose_name='Descripción')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Creado') 
    createdby = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, verbose_name='Creado Por', related_name='created_usr_user')
    updated = models.DateTimeField(auto_now=True, verbose_name='Actualizado')
    updatedby = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, verbose_name='Actualizado Por', related_name='updated_usr_user')

    class Meta:
        db_table = 'usr_user'
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'"""



    
   
