from django.contrib import admin
from .models import *

# Register your models here.
class GastoAdmin(admin.ModelAdmin):
    list_display = ['concepto', 'persona', 'fecha', 'observacion']

admin.site.register(Gasto,GastoAdmin)
admin.site.register(Pago)
admin.site.register(Monedas)
admin.site.register(Deuda)
