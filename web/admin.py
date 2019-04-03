from django.contrib import admin
from .models import *

# Register your models here.
class MenuAdmin(admin.ModelAdmin):
    list_display = ['nombre','link']
admin.site.register(Menu,MenuAdmin)

class TitularAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'link','subtitulo','pie','foto_fondo']
admin.site.register(Titular,TitularAdmin)

class Seccion1Admin(admin.ModelAdmin):
    list_display = ['emergente', 'titulo','subtitulo','parrafo','labelboton','link','foto_fondo']
admin.site.register(Seccion1,Seccion1Admin)

admin.site.register(Icono)

class Seccion2Admin(admin.ModelAdmin):
    list_display = ['titulo', 'parrafo','link','foto_fondo']
admin.site.register(Seccion2,Seccion2Admin)

admin.site.register(Servicio)
admin.site.register(Seccion3)

class GaleriaAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'subtitulo','foto_imagen']
admin.site.register(Galeria,GaleriaAdmin)

admin.site.register(Seccion4)

class VoceriaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'cargo','twiter','facebook','google','foto_persona']
admin.site.register(Voceria,VoceriaAdmin)

admin.site.register(Seccion5)
admin.site.register(Seccion6)

class Seccion7Admin(admin.ModelAdmin):
    list_display = ['autor', 'fecha','descripcion','precio','foto_fondo']
admin.site.register(Seccion7,Seccion7Admin)

admin.site.register(Seccion8)
admin.site.register(Sugerencia)
