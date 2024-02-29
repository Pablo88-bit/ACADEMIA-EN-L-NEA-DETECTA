from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class AdministrationConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Administration'
    verbose_name = _('Administración')  # Cambia 'Administración' al idioma que desees

    #Importando signals a la aplicación
    def ready(self):
        import Administration.signals
