from django.contrib import admin
from .models import *
# Register your models here.
class CalleAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'numero']

admin.site.register(Calle,CalleAdmin)

class GastoAdmin(admin.ModelAdmin):
    list_display = ['concepto', 'persona', 'fecha', 'observacion']

admin.site.register(Gasto,GastoAdmin)


admin.site.register(TipoParentesco)
admin.site.register(Pago)
admin.site.register(Candidatura)
admin.site.register(Discapacidad)
admin.site.register(Boleta)
admin.site.register(Oficio)
admin.site.register(Mes)
admin.site.register(Parentesco)
admin.site.register(Eleccion)
admin.site.register(TratamientoPermanente)
admin.site.register(Casa)
admin.site.register(Habilidad)
admin.site.register(Monedas)
admin.site.register(InstitucionEducativa)
admin.site.register(CronogramaGuardia)
admin.site.register(Grado)
admin.site.register(Etnia)
admin.site.register(Persona)
admin.site.register(Titulo)
admin.site.register(Familia)
admin.site.register(Guardia)
admin.site.register(Deuda)
admin.site.register(Votacion)