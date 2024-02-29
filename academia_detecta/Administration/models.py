"""from django.db import models
#from django.contrib.auth.models import Permission
from django.contrib.auth.models import Group
from Users.models import USR_User

    
# Create your models here.    
class AD_TypeIdentification(models.Model):
    ad_typeidentification_id = models.BigAutoField(auto_created=True, primary_key=True, unique=True, serialize=False, verbose_name='Identificador') 
    code = models.CharField(max_length=50, null=False, blank=False, verbose_name='Código Tipo Identificación')    
    name = models.CharField(max_length=50, null=False, blank=False, verbose_name='Nombre', help_text='Nombre del Tipo de Identificación')
    description = models.TextField(max_length=255, null=True, blank=True, editable=True, verbose_name='Descripción')
    isactive = models.BooleanField(default=True, verbose_name='Activo')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Creado') 
    createdby = models.ForeignKey(USR_User, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Creado Por', related_name='created_ad_typeidentification')
    updated = models.DateTimeField(auto_now=True, verbose_name='Actualizado')
    updatedby = models.ForeignKey(USR_User, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Actualizado Por', related_name='updated_ad_typeidentification')

    class Meta:                   #Meta class we can change the table name in the DB and in the System
        db_table = 'ad_typeidentification'    
        verbose_name = 'Tipo de Identificación'
        verbose_name_plural = 'Tipos de Identificaciones'

    def __str__(self):            #This function allows us to return the name object
        return self.name
    


class AD_Nationality(models.Model):
    ad_nationality_id = models.BigAutoField(auto_created=True, primary_key=True, unique=True, serialize=False, verbose_name='Identificador') 
    code = models.CharField(max_length=50, null=False, blank=False, verbose_name='Código Nacionalidad')    
    name = models.CharField(max_length=50, null=False, blank=False, verbose_name='Nombre', help_text='Nombre de la Nacionalidad')
    description = models.TextField(max_length=255, null=True, blank=True, editable=True, verbose_name='Descripción')
    isactive = models.BooleanField(default=True, verbose_name='Activo')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Creado') 
    createdby = models.ForeignKey(USR_User, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Creado Por', related_name='created_ad_nationality')
    updated = models.DateTimeField(auto_now=True, verbose_name='Actualizado')
    updatedby = models.ForeignKey(USR_User, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Actualizado Por', related_name='updated_ad_nationality')

    class Meta:                   #Meta class we can change the table name in the DB and in the System
        db_table = 'ad_nationality'  
        verbose_name = 'Nacionalidad'
        verbose_name_plural = 'Nacionalidades'

    def __str__(self):            #This function allows us to return the name object
        return self.name
    


class AD_City(models.Model):
    ad_city_id = models.BigAutoField(auto_created=True, primary_key=True, unique=True, serialize=False, verbose_name='Identificador') 
    code = models.CharField(max_length=50, null=False, blank=False, verbose_name='Código Ciudad')    
    name = models.CharField(max_length=50, null=False, blank=False, verbose_name='Nombre', help_text='Nombre de la Ciudad')
    description = models.TextField(max_length=255, null=True, blank=True, editable=True, verbose_name='Descripción')
    isactive = models.BooleanField(default=True, verbose_name='Activo')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Creado') 
    createdby = models.ForeignKey(USR_User, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Creado Por', related_name='created_ad_city')
    updated = models.DateTimeField(auto_now=True, verbose_name='Actualizado')
    updatedby = models.ForeignKey(USR_User, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Actualizado Por', related_name='updated_ad_city')

    class Meta:                   #Meta class we can change the table name in the DB and in the System
        db_table = 'ad_city'   
        verbose_name = 'Ciudad'
        verbose_name_plural = 'Ciudades'

    def __str__(self):            #This function allows us to return the name object
        return self.name  
    


class AD_Sex(models.Model):
    ad_sex_id = models.BigAutoField(auto_created=True, primary_key=True, unique=True, serialize=False, verbose_name='Identificador') 
    code = models.CharField(max_length=50, null=False, blank=False, verbose_name='Código del Sexo')    
    name = models.CharField(max_length=50, null=False, blank=False, verbose_name='Nombre', help_text='Nombre descriptivo del sexo del Usuario')
    description = models.TextField(max_length=255, null=True, blank=True, editable=True, verbose_name='Descripción')
    isactive = models.BooleanField(default=True, verbose_name='Activo')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Creado') 
    createdby = models.ForeignKey(USR_User, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Creado Por', related_name='created_ad_sex')
    updated = models.DateTimeField(auto_now=True, verbose_name='Actualizado')
    updatedby = models.ForeignKey(USR_User, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Actualizado Por', related_name='updated_ad_sex')

    class Meta:                   #Meta class we can change the table name in the DB and in the System
        db_table = 'ad_sex'    
        verbose_name = 'Sexo'
        verbose_name_plural = 'Sexos'

    def __str__(self):            #This function allows us to return the name object
        return self.name
    


class AD_EducationLevel(models.Model):   
    ad_educationlevel_id = models.BigAutoField(auto_created=True, primary_key=True, unique=True, serialize=False, verbose_name='Identificador') 
    code = models.CharField(max_length=50, null=False, blank=False, verbose_name='Código del Nivel de Escolaridad')    
    name = models.CharField(max_length=50, null=False, blank=False, verbose_name='Nombre', help_text='Nombre del Nivel de Escolaridad')
    description = models.TextField(max_length=255, null=True, blank=True, editable=True, verbose_name='Descripción')
    isactive = models.BooleanField(default=True, verbose_name='Activo')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Creado') 
    createdby = models.ForeignKey(USR_User, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Creado Por', related_name='created_ad_educationlevel')
    updated = models.DateTimeField(auto_now=True, verbose_name='Actualizado')
    updatedby = models.ForeignKey(USR_User, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Actualizado Por', related_name='updated_ad_educationlevel')

    class Meta:                   #Meta class we can change the table name in the DB and in the System
        db_table = 'ad_educationlevel'   
        verbose_name = 'Nivel de Escolaridad'
        verbose_name_plural = 'Niveles de Escolaridad'

    def __str__(self):            #This function allows us to return the name object
        return self.name 
    


class AD_TelephoneCompany(models.Model):
    ad_telephonecompany_id = models.BigAutoField(auto_created=True, primary_key=True, unique=True, serialize=False, verbose_name='Identificador') 
    code = models.CharField(max_length=50, null=False, blank=False, verbose_name='Código de la Compañía Telefónica')    
    name = models.CharField(max_length=50, null=False, blank=False, verbose_name='Nombre', help_text='Nombre de la Compañía Telefónica')
    description = models.TextField(max_length=255, null=True, blank=True, editable=True, verbose_name='Descripción')
    isactive = models.BooleanField(default=True, verbose_name='Activo')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Creado') 
    createdby = models.ForeignKey(USR_User, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Creado Por', related_name='created_ad_telephonecompany')
    updated = models.DateTimeField(auto_now=True, verbose_name='Actualizado')
    updatedby = models.ForeignKey(USR_User, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Actualizado Por', related_name='updated_ad_telephonecompany')

    class Meta:                   #Meta class we can change the table name in the DB and in the System
        db_table = 'ad_telephonecompany'    
        verbose_name = 'Compañia Telefónica'
        verbose_name_plural = 'Compañias Telefónicas'

    def __str__(self):            #This function allows us to return the name object
        return f"Código:{self.code}, Nombre Compañia:{self.name}"
    


class AD_Profile(models.Model):
    ad_profile_id = models.BigAutoField(auto_created=True, primary_key=True, unique=True, serialize=False, verbose_name='Identificador')
    license = models.CharField(max_length=50, null=False, blank=False, verbose_name='Carnet ó Código', help_text='Carnet o Código')
    first_name = models.CharField(max_length=50, null=False, blank=False, verbose_name='Primer Nombre')
    second_name = models.CharField(max_length=50, null=True, blank=True, verbose_name='Segundo Nombre')
    surname = models.CharField(max_length=50, null=False, blank=False, verbose_name='Primer Apellido')
    second_surname = models.CharField(max_length=50, null=True, blank=True, verbose_name='Segundo Apellido')
    type_identification = models.ForeignKey(AD_TypeIdentification, on_delete=models.CASCADE, null=False, blank=False, verbose_name="Tipo Identificación")
    identification_number = models.CharField(max_length=25, null=False, blank=False, verbose_name='Número de Identificación')
    nss = models.CharField(max_length=25, null=True, blank=True, verbose_name='Número de Seguro Social')
    birth_date = models.DateField(null=False, blank=False, verbose_name='Fecha de Nacimiento')
    nationality = models.ForeignKey(AD_Nationality, on_delete=models.CASCADE, null=False, blank=False, verbose_name="Nacionalidad")
    city = models.ForeignKey(AD_City, on_delete=models.CASCADE, null=False, blank=False, verbose_name="Ciudad")
    address = models.TextField(max_length=255, null=True, blank=True, verbose_name="Dirección Domiciliar")
    education_level = models.ForeignKey(AD_EducationLevel, on_delete=models.CASCADE, null=False, blank=False, verbose_name="Nivel de Escolaridad")
    sex = models.ForeignKey(AD_Sex, on_delete=models.CASCADE, null=False, blank=False, verbose_name="Sexo")
    image_profile = models.ImageField(upload_to='profile/', null=False, blank=False, verbose_name="Imagen del Perfil")
    observations = models.TextField(max_length=255, null=True, blank=True, verbose_name="Observaciones")
    description = models.TextField(max_length=255, null=True, blank=True, verbose_name='Descripción')
    isactive = models.BooleanField(default=True, verbose_name='Activo')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Creado') 
    createdby = models.ForeignKey(USR_User, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Creado Por', related_name='created_ad_profile')
    updated = models.DateTimeField(auto_now=True, verbose_name='Actualizado')
    updatedby = models.ForeignKey(USR_User, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Actualizado Por', related_name='updated_ad_profile')
    group = models.ForeignKey(Group, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Grupo del Usuario')
    user = models.OneToOneField(USR_User, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Usuario dueño del Perfil')

    class Meta:                 #Meta class we can change the table name in the DB and in the System
        db_table = 'ad_profile'
        verbose_name = 'Perfil Usuario'
        verbose_name_plural = 'Perfil Usuarios'

    def __str__(self):          #This function allows us to return the name object
        return f"{self.license} - Nombre:{self.first_name} {self.surname}, - Grupo:{self.group}"
    


class AD_Email(models.Model):
    ad_email_id = models.BigAutoField(auto_created=True, primary_key=True, unique=True, serialize=False, verbose_name='Identificador')
    email = models.EmailField(max_length=100, null=False, blank=False, verbose_name='Correo electrónico')
    isactive = models.BooleanField(default=True, verbose_name='Activo')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Creado') 
    createdby = models.ForeignKey(USR_User, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Creado Por', related_name='created_ad_email')
    updated = models.DateTimeField(auto_now=True, verbose_name='Actualizado')
    updatedby = models.ForeignKey(USR_User, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Actualizado Por', related_name='updated_ad_email')
    profile = models.ForeignKey(AD_Profile, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Usuario')

    class Meta:                 #Meta class we can change the table name in the DB and in the System
        db_table = 'ad_email'
        verbose_name = 'Correo de Recuperación'
        verbose_name_plural = 'Correos de Recuperación'

    def __str__(self):           #This function allows us to return the name object
        return f"{self.profile.user} - {self.email}"
    


class AD_Phone(models.Model):
    ad_phone_id = models.BigAutoField(auto_created=True, primary_key=True, unique=True, serialize=False, verbose_name='Identificador')
    phone_number = models.CharField(max_length=8, null=False, blank=False, verbose_name='Número Telefónico')
    isactive = models.BooleanField(default=True, verbose_name='Activo')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Creado') 
    createdby = models.ForeignKey(USR_User, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Creado Por', related_name='created_ad_phone')
    updated = models.DateTimeField(auto_now=True, verbose_name='Actualizado')
    updatedby = models.ForeignKey(USR_User, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Actualizado Por', related_name='updated_ad_phone')
    profile = models.ForeignKey(AD_Profile, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Usuario')
    company = models.ForeignKey(AD_TelephoneCompany, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Compañía Telefónica')

    class Meta:                 #Meta class we can change the table name in the DB and in the System
        db_table = 'ad_phone'
        verbose_name = 'Teléfono de Contacto'
        verbose_name_plural = 'Teléfonos de Contacto'

    def __str__(self):          #This function allows us to return the name object 
        return f"{self.profile.user} - {self.phone}"
    


class AD_TypePhoneNumber(models.Model):
    ad_typephonenumber_id = models.BigAutoField(auto_created=True, primary_key=True, unique=True, serialize=False, verbose_name='Identificador')
    name = models.CharField(max_length=50, null=False, blank=False, verbose_name='Tipo de Número')
    isactive = models.BooleanField(default=True, verbose_name='Activo')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Creado') 
    createdby = models.ForeignKey(USR_User, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Creado Por', related_name='created_ad_typephonenumber')
    updated = models.DateTimeField(auto_now=True, verbose_name='Actualizado')
    updatedby = models.ForeignKey(USR_User, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Actualizado Por', related_name='updated_ad_typephonenumber')
    phone = models.ForeignKey(AD_Phone, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Número Telefónico')

    class Meta:                 #Meta class we can change the table name in the DB and in the System
        db_table = 'ad_type_phone_number'
        verbose_name = 'Tipo de Teléfono'
        verbose_name_plural = 'Tipos de Teléfonos'

    def __str__(self):          #This function allows us to return the name object 
        return f"{self.profile.user} - {self.phone}" """