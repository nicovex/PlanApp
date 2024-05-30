from django.contrib import admin

# Register your models here.
from . import models

admin.site.site_title = "Planner"


class ProyectoAdmin(admin.ModelAdmin):
    
    list_display = ('nombre',
                    'descripcion',
                    'fecha_inicio',
                    'fecha_fin',
    )
    list_display_links = ("nombre",)
    search_fields = ("nombre",)
    ordering = ("fecha_inicio", "nombre")
    # list_filter = ("responsable",)
    date_hierarchy = "fecha_inicio"

class TareaAdmin(admin.ModelAdmin):
    
    list_display = ("nombre", "completada")
    list_display_links = ("nombre",)

class ResponsableAdmin(admin.ModelAdmin):
    list_display = ("user", "avatar")
    list_display_links = ("user",)

admin.site.register(models.Proyecto, ProyectoAdmin)
admin.site.register(models.Tarea, TareaAdmin)
admin.site.register(models.Responsable, ResponsableAdmin)