from django.contrib import admin
from .models import Canal, CanalUsuario, CanalMensaje


class CanalMensajeInLine(admin.TabularInline):
    model = CanalMensaje
    extra = 1

class CanalUsuarioInLine(admin.TabularInline):
    model = CanalUsuario
    extra = 1

class CanalAdmin(admin.ModelAdmin):
    inlines= [CanalMensajeInLine, CanalUsuarioInLine]

    class Meta:
        model = Canal

admin.site.register(Canal, CanalAdmin)
admin.site.register(CanalUsuario)
admin.site.register(CanalMensaje)