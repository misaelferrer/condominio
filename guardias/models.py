from django.db import models
from censo.models import *

# Create your models here.

class CronogramaGuardia(models.Model):
	titulo = models.CharField(max_length=40, null=True) # CharField
	hora_inicio = models.TimeField(null=True) # TimeField
	hora_fin = models.TimeField(null=True) # TimeField
	observaciones = models.TextField(null=True) # TextField

	def __str__ (self):
		return self.titulo


class Guardia(models.Model):
	fecha = models.DateField(null=True)  # DateField
	persona = models.ForeignKey(Persona, on_delete=models.DO_NOTHING, null=True) # Persona
	horario = models.ForeignKey(CronogramaGuardia, on_delete=models.DO_NOTHING, null=True)  # Persona
	observaciones = models.TextField(null=True) # TextFiel

	def __str__ (self):
		return self.persona + '-' + self.horario

