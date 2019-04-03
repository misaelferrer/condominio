from django.contrib import admin
from .models import *
from imagekit.admin import AdminThumbnail
# Register your models here.
class CalleAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'numero']




admin.site.register(Nacionalidad)
admin.site.register(TipoParentesco)
admin.site.register(Discapacidad)

class DocumentoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'foto_documento']

admin.site.register(Documento,DocumentoAdmin)
admin.site.register(Oficio)
admin.site.register(Mes)
admin.site.register(Sexo)
admin.site.register(Parentesco)

class ApartamentoAdmin(admin.ModelAdmin):
    list_display = ['numero', 'cantidad_habitaciones','foto_apartamento']

admin.site.register(Apartamento,ApartamentoAdmin)
admin.site.register(Habilidad)
admin.site.register(InstitucionEducativa)
admin.site.register(Grado)

class PersonaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'apellido','sexo','observaciones', 'apartamento', 'foto_persona']

admin.site.register(Persona,PersonaAdmin)
admin.site.register(Titulo)
