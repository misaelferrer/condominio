from django.db import models

# Create your models here.

class CarnetPatria(models.Model):
	nombre = models.CharField(max_length=15, null=True)  # CharField
	serial = models.CharField(max_length=15, null=True) # CharField
	codigo = models.CharField(max_length=15, null=True)  # CharField
	imagen = models.ImageField(upload_to='static/carnet_patria/', null=True)  # ImageField

	def __str__ (self):
		return self.serial

class Mes(models.Model):
	mes = models.CharField(max_length=15, null=True) # CharField

	def __str__ (self):
		return self.mes


class Documento(models.Model):
	nombre = models.CharField(max_length=15, null=True) # CharField
	documento = models.ImageField(upload_to='static/documentos/', null=True)  # ImageField
	def __str__ (self):
		return self.nombre


class Mision(models.Model):
	mision = models.CharField(max_length=35, null=True) # CharField

	def __str__ (self):
		return self.mision


class Sexo(models.Model):
	sexo = models.CharField(max_length=15, null=True) # CharField

	def __str__ (self):
		return self.sexo


class Nacionalidad(models.Model):
	nacionalidad = models.CharField(max_length=15, null=True) # CharField

	def __str__ (self):
		return self.nacionalidad


class Calle(models.Model):
	nombre = models.CharField(max_length=50,null=True) # TextField
	numero = models.CharField(max_length=10, null=True) # CharField
	
	def __str__ (self):
		return self.nombre 

class Casa(models.Model):
	foto = models.ImageField(upload_to='static/casas/', null=True)  # ImageField
	numero = models.CharField(max_length=10, null=True) # CharField
	observaciones = models.TextField(null=True) # TextField
	calle = models.ForeignKey(Calle, on_delete=models.DO_NOTHING, null=True) # Calle
	cantidad_habitaciones = models.IntegerField(null=True) # IntegerField

	def __str__ (self):
		return self.numero

class Discapacidad(models.Model):
	discapacidad = models.CharField(max_length=30, null=True) # CharField

	def __str__ (self):
		return self.discapacidad


class Oficio(models.Model):
	oficio = models.CharField(max_length=30, null=True) # CharField

	def __str__ (self):
		return self.oficio 


class TratamientoPermanente(models.Model):
	enfermedad = models.CharField(max_length=30, null=True) # CharField
	medicina = models.CharField(max_length=30, null=True) # CharField
	informe_medico = models.ImageField(upload_to='static/informes_medicos/', null=True)  # ImageField
	recipe = models.ImageField(upload_to='static/recipes/', null=True)  # ImageField

	def __str__ (self):
		return self.enfermedad + ' - ' + self.medicina

class Habilidad(models.Model):
	habilidad = models.CharField(max_length=30, null=True) # CharField

	def __str__ (self):
		return self.habilidad 

class InstitucionEducativa(models.Model):
	institucion_educativa = models.CharField(max_length=30, null=True) # CharField

	def __str__ (self):
		return self.institucion_educativa 

class Grado(models.Model):
	grado = models.CharField(max_length=30, null=True) # CharField
	institucion_educativa = models.ForeignKey(InstitucionEducativa, on_delete=models.DO_NOTHING, null=True) # InstitucionEducativa

	def __str__ (self):
		return self.grado 

class Etnia(models.Model):
	etnia = models.CharField(max_length=30, null=True) # CharField

	def __str__ (self):
		return self.etnia
class Familia(models.Model):
	nombre = models.CharField(max_length=20, null=True) # CharField
	casa = models.ForeignKey(Casa, on_delete=models.DO_NOTHING, null=True) # Casa

	def __str__ (self):
		return self.nombre

class Titulo(models.Model):
	titulo = models.CharField(max_length=30) # CharField
	institucion_educativa = models.ForeignKey(InstitucionEducativa, on_delete=models.DO_NOTHING, null=True) # InstitucionEducativa

	def __str__ (self):
		return self.titulo


class Persona(models.Model):
	foto = models.ImageField(upload_to='static/personas/', null=True) # ImageField
	nacionalidad = models.ForeignKey(Nacionalidad, on_delete=models.DO_NOTHING, null=True) # Nacionalidad
	cedula = models.CharField(max_length=10, null=True) # CharField
	nombre = models.CharField(max_length=20, null=True) # CharField
	apellido = models.CharField(max_length=20, null=True) # CharField
	sexo = models.ForeignKey(Sexo, on_delete=models.DO_NOTHING, null=True)  # Sexo
	documento = models.ManyToManyField(Documento)  # Documento
	carnet_patria = models.ForeignKey(CarnetPatria, on_delete=models.DO_NOTHING, null=True)  # CarnetPatria
	discapaz = models.BooleanField() # BooleanField
	discapacidad = models.ManyToManyField(Discapacidad) # Discapacidad
	tratamiento_permanente = models.ManyToManyField(TratamientoPermanente)  # TratamientoPermanente
	mision = models.ManyToManyField(Mision)  # Mision
	familia = models.ForeignKey(Familia, on_delete=models.DO_NOTHING, null=True) # Familia
	oficio = models.ForeignKey(Oficio, on_delete=models.DO_NOTHING, null=True) # Oficio
	fecha_nacimiento = models.DateField(null=True) # DateField
	vive_desde = models.IntegerField(null=True) # IntegerField
	habilidad = models.ManyToManyField(Habilidad) # Habilidad
	titulos = models.ManyToManyField(Titulo) # Titulo
	ultimo_grado_aprobado = models.ForeignKey(Grado, on_delete=models.DO_NOTHING, null=True) # Grado
	indigena = models.BooleanField() # BooleanField
	etnia = models.ForeignKey(Etnia, on_delete=models.DO_NOTHING, null=True) # Etnia
	ingreso_mensual = models.FloatField(null=True) # FloatField
	observaciones = models.TextField(null=True) # TextField

	def __str__ (self):
		return self.nombre + ' - ' + self.apellido

class TipoParentesco(models.Model):
	tipoParentesco = models.CharField(max_length=30, null=True) # CharField

	def __str__ (self):
		return self.tipoParentesco

class Parentesco(models.Model):
	persona = models.ForeignKey(Persona, related_name='persona', on_delete=models.DO_NOTHING, null=True) # Persona
	pariente = models.ForeignKey(Persona, related_name='pariente', on_delete=models.DO_NOTHING, null=True) # Persona
	tipoParentesco = models.ForeignKey(TipoParentesco, on_delete=models.DO_NOTHING, null=True) # TipoParentesco

	def __str__ (self):
		return self.tipoParentesco

