from django.contrib import admin
#from django.contrib.admin import AdminSite
#from Users.models import USR_User
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.contrib.sessions.models import Session


admin.site.site_header = "ACADEMIA DETECTA"

# Register your models here.
#admin.site.unregister(Group)
admin.site.unregister(User)

class UsuarioAdmin(admin.ModelAdmin):

        fieldsets = (
            (None, {'fields': ('username', 'password')}),
            ('Información Personal', {'fields': ('first_name', 'last_name', 'email')}),
            ('Permisos', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
            ('Fechas Importantes', {'fields': ('last_login', 'date_joined')}),
        )
        add_fieldsets = (
            (None, {
               'classes': ('wide',),
               'fields': ('username', 'password1', 'password2'),
            }),
        )

        #Ocultando el eliminar
        def has_delete_permission(self, request, obj=None):
                return False

admin.site.register(User, UsuarioAdmin)


"""class GroupAdmin(admin.ModelAdmin):
        search_fields = ('name', 'user_count')  # Habilitar la búsqueda por nombre de grupo
        filter_horizontal = ('permissions',)  # Agregar un campo para seleccionar permisos 
        search_fields = ('name',)  # Habilitar la búsqueda por nombre de grupo

        def user_count(self, obj):
                return obj.user_set.count()  # Método para obtener el recuento de usuarios en un grupo

        user_count.short_description = 'Número de Usuarios'  # Nombre de la columna en la lista de grupos
        user_count.admin_order_field = 'user_set__count'  # Orden de la columna en la lista de grupos
        user_count.allow_tags = True  # Habilitar etiquetado en la columna en la lista de grupos 

        #Ocultando el eliminar
        def has_delete_permission(self, request, obj=None):
                return False 


#admin.site.unregister(Group)
admin.site.register(Group, GroupAdmin)"""



class PermissionAdmin(admin.ModelAdmin):
        list_display = ('name', 'content_type')  
        list_per_page = 6  # Paginación de 6 registros por página

        def has_delete_permission(self, request, obj=None):
                return False  # Oculta el botón de borrar
        
        #Denegar permiso a añadir cualquier registro 
        def has_add_permission(self, request, obj=None):
                return False

admin.site.register(Permission, PermissionAdmin)


class ContentTypeAdmin(admin.ModelAdmin):
        list_display = ('app_label', 'model')
        list_per_page = 6
        readonly_fields = ['app_label', 'model']
        #actions = None  # Elimina las acciones por lotes

        #Denegar permiso a eliminar cualquier registro 
        def has_delete_permission(self, request, obj=None):
                return False
        
        #Denegar permiso a actualizar cualquier registro 
        def has_change_permission(self, request, obj=None):
                return False  # Denegar permiso de cambio incluso para administradores
        
        #Denegar permiso a añadir cualquier registro 
        def has_add_permission(self, request, obj=None):
                return False
        
        #def content_type_name(self, obj):
        #    return obj.content_type.name

        #content_type_name.short_description = 'Tipo de Contenido'

admin.site.register(ContentType, ContentTypeAdmin) 



"""class SessionAdmin(admin.ModelAdmin):
        list_display = ('session_data', 'expire_date')
        list_per_page = 6
        #readonly_fields = ['session_key', 'session_data', 'expire_date']

        #Denegar permiso a eliminar cualquier registro 
        def has_delete_permission(self, request, obj=None):
                return False
        
        #Denegar permiso a actualizar cualquier registro 
        def has_change_permission(self, request, obj=None):
                return False  # Denegar permiso de cambio incluso para administradores
        
        #Denegar permiso a añadir cualquier registro 
        def has_add_permission(self, request, obj=None):
                return False
        
        #def get_actions(self, request):
                # Override to remove the delete action
                #actions = super().get_actions(request)
                #del actions['delete_selected']
                #return actions

admin.site.register(Session, SessionAdmin)"""