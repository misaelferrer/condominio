from django.contrib import admin
from .models import *
# Register your models here.
class CalleAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'numero']

admin.site.register(Calle,CalleAdmin)



admin.site.register(Nacionalidad)
admin.site.register(TipoParentesco)
admin.site.register(Discapacidad)
admin.site.register(Documento)
admin.site.register(CarnetPatria)
admin.site.register(Oficio)
admin.site.register(Mes)
admin.site.register(Mision)
admin.site.register(Sexo)
admin.site.register(Parentesco)
admin.site.register(TratamientoPermanente)
admin.site.register(Casa)
admin.site.register(Habilidad)
admin.site.register(InstitucionEducativa)
admin.site.register(Grado)
admin.site.register(Etnia)
admin.site.register(Persona)
admin.site.register(Titulo)
admin.site.register(Familia)
