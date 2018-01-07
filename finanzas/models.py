from django.db import models
from censo.models import *
# Create your models here.
class Deuda(models.Model):
	deuda = models.FloatField(null=True) # FloatField
	anio = models.IntegerField(null=True) # IntegerField
	mes = models.ForeignKey(Mes, on_delete=models.DO_NOTHING, null=True) # Mes
	casa = models.ForeignKey(Casa, on_delete=models.DO_NOTHING, null=True) # Casa
	fecha_carga = models.DateField(null=True) # DateField
	pagado = models.BooleanField() # BooleanField

	def __str__ (self):
		return self.mes + ' - ' + self.casa

class Pago(models.Model):
	casa = models.ForeignKey(Casa, on_delete=models.DO_NOTHING, null=True) # Casa
	fecha_pago = models.DateField(null=True) # DateField
	deuda = models.ForeignKey(Deuda, on_delete=models.DO_NOTHING, null=True) # Deuda
	pago = models.FloatField(null=True) # FloatField
	concepto = models.CharField(max_length=30, null=True) # CharField

	def __str__ (self):
		return self.concepto


class Monedas(models.Model):
	persona = models.ForeignKey(Persona, on_delete=models.DO_NOTHING, null=True) # Persona
	fecha_entrega = models.DateField(null=True) # DateField
	deuda = models.ForeignKey(Deuda, on_delete=models.DO_NOTHING, null=True) # Deuda
	oficio = models.ForeignKey(Oficio, on_delete=models.DO_NOTHING, null=True) # Oficio
	concepto = models.TextField(null=True) # TextField

	def __str__ (self):
		return self.concepto



class Gasto(models.Model):
	concepto = models.CharField(max_length=30, null=True)  # CharField
	persona = models.ForeignKey(Persona, on_delete=models.DO_NOTHING, null=True)  # persona
	fecha = models.DateField(null=True)  # DateField
	observacion = models.TextField(null=True)  # TextField

	def __str__(self):
		return self.concepto

