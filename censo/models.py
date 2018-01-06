from django.db import models

# Create your models here.

class Mes(models.Model):
	mes = models.CharField(max_length=15, null=True) # CharField

	def __str__ (self):
		return self.mes

class Calle(models.Model):
	nombre = models.CharField(max_length=50,null=True) # TextField
	numero = models.CharField(max_length=10, null=True) # CharField
	
	def __str__ (self):
		return self.nombre 

class TipoParentesco(models.Model):
	tipoParentesco = models.CharField(max_length=30, null=True) # CharField

	def __str__ (self):
		return self.tipoParentesco

class Casa(models.Model):
	foto = models.ImageField(upload_to='casas/', null=True)  # ImageField
	numero = models.CharField(max_length=10, null=True) # CharField
	observaciones = models.TextField(null=True) # TextField
	calle = models.ForeignKey(Calle, on_delete=models.DO_NOTHING, null=True) # Calle
	cantidad_habitaciones = models.IntegerField(null=True) # IntegerField

	def __str__ (self):
		return self.numero

class Deuda(models.Model):
	deuda = models.FloatField(null=True) # FloatField
	anio = models.IntegerField(null=True) # IntegerField
	mes = models.ForeignKey(Mes, on_delete=models.DO_NOTHING, null=True) # Mes
	casa = models.ForeignKey(Casa, on_delete=models.DO_NOTHING, null=True) # Casa
	fecha_carga = models.DateField(null=True) # DateField
	pagado = models.BooleanField(default=False) # BooleanField

	def __str__ (self):
		return self.mes + self.casa

class Pago(models.Model):
	casa = models.ForeignKey(Casa, on_delete=models.DO_NOTHING, null=True) # Casa
	fecha_pago = models.DateField(null=True) # DateField
	deuda = models.ForeignKey(Deuda, on_delete=models.DO_NOTHING, null=True) # Deuda
	pago = models.FloatField(null=True) # FloatField
	concepto = models.CharField(max_length=30, null=True) # CharField

	def __str__ (self):
		return self.concepto 


class Discapacidad(models.Model):
	discapacidad = models.CharField(max_length=30, null=True) # CharField

	def __str__ (self):
		return self.discapacidad


class Oficio(models.Model):
	oficio = models.CharField(max_length=30, null=True) # CharField

	def __str__ (self):
		return self.oficio 

class Eleccion(models.Model):
	titulo = models.CharField(max_length=30, null=True) # CharField
	fecha = models.DateField(null=True) # DateField

	def __str__ (self):
		return self.titulo 

class TratamientoPermanente(models.Model):
	enfermedad = models.CharField(max_length=30, null=True) # CharField
	medicina = models.CharField(max_length=30, null=True) # CharField

	def __str__ (self):
		return self.enfermedad + self.medicina

class Habilidad(models.Model):
	habilidad = models.CharField(max_length=30, null=True) # CharField

	def __str__ (self):
		return self.habilidad 

class InstitucionEducativa(models.Model):
	institucion_educativa = models.CharField(max_length=30, null=True) # CharField

	def __str__ (self):
		return self.institucion_educativa 

class CronogramaGuardia(models.Model):
	hora_inicio = models.TimeField(null=True) # TimeField
	hora_fin = models.TimeField(null=True) # TimeField
	titulo = models.CharField(max_length=40, null=True) # CharField
	observaciones = models.TextField(null=True) # TextField

	def __str__ (self):
		return self.titulo 

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
	titulo = models.CharField(max_length=30, null=True) # CharField
	institucion_educativa = models.ForeignKey(InstitucionEducativa, on_delete=models.DO_NOTHING, null=True) # InstitucionEducativa

	def __str__ (self):
		return self.titulo


class Persona(models.Model):
	foto = models.ImageField(upload_to='casas/', null=True) # ImageField
	nacionalidad = models.CharField(max_length=20, null=True) # CharField
	cedula = models.CharField(max_length=10, null=True) # CharField
	nombre = models.CharField(max_length=20, null=True) # CharField
	apellido = models.CharField(max_length=20, null=True) # CharField
	discapaz = models.BooleanField(default=False) # BooleanField
	discapacidad = models.ManyToManyField(Discapacidad) # Discapacidad
	sexo = models.BooleanField(default=False) # BooleanField
	familia = models.ForeignKey(Familia, on_delete=models.DO_NOTHING, null=True) # Familia
	oficio = models.ForeignKey(Oficio, on_delete=models.DO_NOTHING, null=True) # Oficio
	fecha_nacimiento = models.DateField(null=True) # DateField
	vive_desde = models.IntegerField(null=True) # IntegerField
	habilidad = models.ForeignKey(Habilidad, on_delete=models.DO_NOTHING, null=True) # Habilidad
	titulos = models.ManyToManyField(Titulo) # Titulo
	ultimo_grado_aprobado = models.ForeignKey(Grado, on_delete=models.DO_NOTHING, null=True) # Grado
	indigena = models.BooleanField(default=False) # BooleanField
	etnia = models.ForeignKey(Etnia, on_delete=models.DO_NOTHING, null=True) # Etnia
	ingreso_mensual = models.FloatField(null=True) # FloatField
	observaciones = models.TextField(null=True) # TextField
	tratamiento_permanente = models.ManyToManyField(TratamientoPermanente) # TratamientoPermanente

	def __str__ (self):
		return self.nombre + self.apellido

class Monedas(models.Model):
	persona = models.ForeignKey(Persona, on_delete=models.DO_NOTHING, null=True) # Persona
	fecha_entrega = models.DateField(null=True) # DateField
	deuda = models.ForeignKey(Deuda, on_delete=models.DO_NOTHING, null=True) # Deuda
	oficio = models.ForeignKey(Oficio, on_delete=models.DO_NOTHING, null=True) # Oficio
	concepto = models.TextField(null=True) # TextField

	def __str__ (self):
		return self.concepto


class Parentesco(models.Model):
	persona = models.ForeignKey(Persona, related_name='persona', on_delete=models.DO_NOTHING, null=True) # Persona
	pariente = models.ForeignKey(Persona, related_name='pariente', on_delete=models.DO_NOTHING, null=True) # Persona
	tipoParentesco = models.ForeignKey(TipoParentesco, on_delete=models.DO_NOTHING, null=True) # TipoParentesco

	def __str__ (self):
		return self.tipoParentesco


class Candidatura(models.Model):
	nombre = models.CharField(max_length=30, null=True)  # CharField
	persona = models.ManyToManyField(Persona)  # persona

	def __str__(self):
		return self.nombre + self.persona

class Boleta(models.Model):
	titulo = models.CharField(max_length=30, null=True) # CharField
	eleccion = models.ForeignKey(Eleccion, on_delete=models.DO_NOTHING, null=True) # Eleccion
	candidatura = models.ManyToManyField(Candidatura) # Candidatura

	def __str__ (self):
		return self.titulo


class Gasto(models.Model):
	concepto = models.CharField(max_length=30, null=True)  # CharField
	persona = models.ForeignKey(Persona, on_delete=models.DO_NOTHING, null=True)  # persona
	fecha = models.DateField(null=True)  # DateField
	observacion = models.TextField(null=True)  # TextField

	def __str__(self):
		return self.concepto


class Guardia(models.Model):
	persona = models.ForeignKey(Persona, on_delete=models.DO_NOTHING, null=True) # Persona
	observaciones = models.TextField(null=True) # TextFiel
	fecha = models.DateField(null=True) # DateField

	def __str__ (self):
		return self.observaciones 


class Votacion(models.Model):
	hora = models.TimeField(null=True) # TimeField
	candidato = models.ForeignKey(Candidatura, on_delete=models.DO_NOTHING, null=True) # Candidatura

	def __str__ (self):
		return self.candidato + self.hora
