from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Users'
    verbose_name = _('Usuarios')  # Cambia 'Usuarios' al idioma que desees
