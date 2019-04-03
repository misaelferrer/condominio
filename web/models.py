from django.db import models
from django.utils.safestring import mark_safe

# Create your models here.
class Menu(models.Model):
	nombre = models.CharField(max_length=25, null=True)  # TextField
	link = models.CharField(max_length=50, null=True)  # CharField

	def __str__(self):
		return self.nombre

class Titular(models.Model):
	nombre = models.CharField(max_length=50, null=True)
	link = models.URLField(max_length=50, null=True)  # CharField
	fondo = models.ImageField(upload_to='static/fondo/principal/', null=True)  # ImageField
	subtitulo = models.CharField(max_length=50, null=True)
	pie = models.CharField(max_length=50, null=True)

	def __str__(self):
		return self.nombre

	def url(self):
		return self.fondo

	def foto_fondo(self):
		# used in the admin site model as a "thumbnail"
		return mark_safe('<img src="../../../' + self.url().__str__() + '" width="70" height="50" />')

class Seccion1(models.Model):
	emergente = models.CharField(max_length=50, null=True)
	fondo = models.ImageField(upload_to='static/fondo/seccion1/', null=True)  # ImageField
	titulo = models.CharField(max_length=50, null=True)
	subtitulo = models.CharField(max_length=50, null=True)
	parrafo = models.TextField(null=True) # TextField
	labelboton = models.CharField(max_length=20, null=True)
	link = models.URLField(max_length=50, null=True)  # CharField

	def url(self):
		return self.fondo

	def foto_fondo(self):
		# used in the admin site model as a "thumbnail"
		return mark_safe('<img src="../../../' + self.url().__str__() + '" width="70" height="50" />')

	def __str__(self):
		return self.titulo

class Icono(models.Model):
	nombre = models.CharField(max_length=25, null=True)  # TextField
	icono = models.CharField(max_length=15, null=True)  # CharField
	cuenta = models.IntegerField(null=True) # IntegerField

	def __str__(self):
		return self.nombre

class Seccion2(models.Model):
	fondo = models.ImageField(upload_to='static/fondo/seccion2/', null=True)  # ImageField
	titulo = models.CharField(max_length=50, null=True)
	parrafo = models.TextField(null=True) # TextField
	link = models.URLField(max_length=50, null=True)  # CharField
	iconos = models.ManyToManyField(Icono)  # Icono

	def __str__(self):
		return self.titulo

	def url(self):
		return self.fondo

	def foto_fondo(self):
		# used in the admin site model as a "thumbnail"
		return mark_safe('<img src="../../../' + self.url().__str__() + '" width="70" height="50" />')

class Servicio(models.Model):
	nombre = models.CharField(max_length=25, null=True)  # TextField
	icono = models.CharField(max_length=15, null=True)  # CharField
	link = models.URLField(max_length=50, null=True)  # CharField
	def __str__(self):
		return self.nombre

class Seccion3(models.Model):
	titulo = models.CharField(max_length=50, null=True)
	servicios = models.ManyToManyField(Servicio)  # Servicio

	def __str__(self):
		return self.titulo

class Galeria(models.Model):
	imagen = models.ImageField(upload_to='static/fondo/seccion4/', null=True)  # ImageField
	titulo = models.CharField(max_length=50, null=True)
	subtitulo = models.CharField(max_length=50, null=True)

	def __str__(self):
		return self.titulo

	def url(self):
		return self.imagen

	def foto_imagen(self):
		# used in the admin site model as a "thumbnail"
		return mark_safe('<img src="../../../' + self.url().__str__() + '" width="70" height="50" />')

class Seccion4(models.Model):
	titulo = models.CharField(max_length=50, null=True)  # CharField
	galeria = models.ManyToManyField(Galeria)  # Galeria

	def __str__(self):
		return self.titulo

class Voceria(models.Model):
	foto = models.ImageField(upload_to='static/fondo/seccion5/', null=True)  # ImageField
	nombre = models.CharField(max_length=50, null=True)
	cargo = models.CharField(max_length=50, null=True)
	twiter = models.CharField(max_length=20, null=True)
	facebook = models.CharField(max_length=20, null=True)
	google = models.CharField(max_length=20, null=True)

	def __str__(self):
		return self.nombre

	def url(self):
		return self.foto

	def foto_persona(self):
		# used in the admin site model as a "thumbnail"
		return mark_safe('<img src="../../../' + self.url().__str__() + '" width="70" height="50" />')

class Seccion5(models.Model):
	titulo = models.CharField(max_length=50, null=True)  # CharField
	voceros = models.ManyToManyField(Voceria)  # Voceria

	def __str__(self):
		return self.titulo

class Seccion6(models.Model):
	titulo = models.CharField(max_length=50, null=True)  # CharField
	parrafo = models.TextField(null=True) # TextField

	def __str__(self):
		return self.titulo


class Seccion7(models.Model):
	foto = models.ImageField(upload_to='static/fondo/seccion7/', null=True)  # ImageField
	autor = models.CharField(max_length=50, null=True)
	fecha = models.DateField(null=True) # DateField
	descripcion = models.CharField(max_length=20, null=True)
	precio = models.FloatField(null=True)

	def __str__(self):
		return self.descripcion

	def url(self):
		return self.foto

	def foto_fondo(self):
		# used in the admin site model as a "thumbnail"
		return mark_safe('<img src="../../../' + self.url().__str__() + '" width="70" height="50" />')

class Seccion8(models.Model):
	direccion = models.TextField(null=True) # TextField
	email = models.EmailField(max_length=50, null=True)
	telefono = models.CharField(max_length=50, null=True)

	def __str__(self):
		return self.titulo

class Sugerencia(models.Model):
	nombre = models.CharField(max_length=50, null=True)
	email = models.EmailField(max_length=50, null=True)
	telefono = models.CharField(max_length=50, null=True)
	Mensaje = models.TextField(null=True)  # TextField

	def __str__(self):
		return self.titulo
