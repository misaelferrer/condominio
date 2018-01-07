from django.db import models
from censo.models import *

# Create your models here.
class Eleccion(models.Model):
	titulo = models.CharField(max_length=30, null=True) # CharField
	fecha = models.DateField(null=True) # DateField

	def __str__ (self):
		return self.titulo


class Candidatura(models.Model):
	nombre = models.CharField(max_length=30, null=True)  # CharField
	persona = models.ManyToManyField(Persona)  # persona

	def __str__(self):
		return self.nombre + ' - ' + self.persona

class Boleta(models.Model):
	titulo = models.CharField(max_length=30, null=True) # CharField
	eleccion = models.ForeignKey(Eleccion, on_delete=models.DO_NOTHING, null=True) # Eleccion
	candidatura = models.ForeignKey(Candidatura, on_delete=models.DO_NOTHING, null=True) # Candidatura

	def __str__ (self):
		return self.titulo


class Votacion(models.Model):
	hora = models.TimeField(null=True) # TimeField
	candidato = models.ForeignKey(Candidatura, on_delete=models.DO_NOTHING, null=True) # Candidatura

	def __str__ (self):
		return self.candidato + ' - ' + self.hora

