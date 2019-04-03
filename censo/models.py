from django.db import models
from django.utils.safestring import mark_safe

class Mes(models.Model):
    mes = models.CharField(max_length=15, null=True)  # CharField

    def __str__(self):
        return self.mes


class Documento(models.Model):
    nombre = models.CharField(max_length=15, null=True)  # CharField
    documento = models.ImageField(upload_to='static/documentos/', null=True)  # ImageField

    def __str__(self):
        return self.nombre

    def url(self):
        return self.documento

    def foto_documento(self):
        # used in the admin site model as a "thumbnail"
        return mark_safe('<img src="../../../' + self.url().__str__() + '" width="70" height="50" />')


class Sexo(models.Model):
    sexo = models.CharField(max_length=15, null=True)  # CharField

    def __str__(self):
        return self.sexo


class Nacionalidad(models.Model):
    nacionalidad = models.CharField(max_length=15, null=True)  # CharField

    def __str__(self):
        return self.nacionalidad


class Apartamento(models.Model):
    foto = models.ImageField(upload_to='static/apartamentos/', null=True)  # ImageField
    numero = models.CharField(max_length=10, null=True)  # CharField
    observaciones = models.TextField(null=True)  # TextField
    cantidad_habitaciones = models.IntegerField(null=True)  # IntegerField

    def __str__(self):
        return self.numero

    def url(self):
        return self.foto

    def foto_apartamento(self):
        # used in the admin site model as a "thumbnail"
        return mark_safe('<img src="../../../' + self.url().__str__() + '" width="70" height="50" />')


class Discapacidad(models.Model):
    discapacidad = models.CharField(max_length=30, null=True)  # CharField

    def __str__(self):
        return self.discapacidad


class Oficio(models.Model):
    oficio = models.CharField(max_length=30, null=True)  # CharField

    def __str__(self):
        return self.oficio


class Habilidad(models.Model):
    habilidad = models.CharField(max_length=30, null=True)  # CharField

    def __str__(self):
        return self.habilidad


class InstitucionEducativa(models.Model):
    institucion_educativa = models.CharField(max_length=30, null=True)  # CharField

    def __str__(self):
        return self.institucion_educativa


class Grado(models.Model):
    grado = models.CharField(max_length=30, null=True)  # CharField
    institucion_educativa = models.ForeignKey(InstitucionEducativa, on_delete=models.DO_NOTHING,
                                              null=True)  # InstitucionEducativa

    def __str__(self):
        return self.grado


class Titulo(models.Model):
    titulo = models.CharField(max_length=30)  # CharField
    institucion_educativa = models.ForeignKey(InstitucionEducativa, on_delete=models.DO_NOTHING,
                                              null=True)  # InstitucionEducativa

    def __str__(self):
        return self.titulo


class Persona(models.Model):
    foto = models.ImageField(upload_to='static/personas/', null=True)  # ImageField
    nacionalidad = models.ForeignKey(Nacionalidad, on_delete=models.DO_NOTHING, null=True)  # Nacionalidad
    apartamento = models.ForeignKey(Apartamento, on_delete=models.DO_NOTHING, null=True)  # Nacionalidad
    cedula = models.CharField(max_length=10, null=True)  # CharField
    nombre = models.CharField(max_length=20, null=True)  # CharField
    apellido = models.CharField(max_length=20, null=True)  # CharField
    sexo = models.ForeignKey(Sexo, on_delete=models.DO_NOTHING, null=True)  # Sexo
    documento = models.ManyToManyField(Documento)  # Documento
    discapaz = models.BooleanField()  # BooleanField
    discapacidad = models.ManyToManyField(Discapacidad)  # Discapacidad
    oficio = models.ForeignKey(Oficio, on_delete=models.DO_NOTHING, null=True)  # Oficio
    fecha_nacimiento = models.DateField(null=True)  # DateField
    vive_desde = models.IntegerField(null=True)  # IntegerField
    habilidad = models.ManyToManyField(Habilidad)  # Habilidad
    titulos = models.ManyToManyField(Titulo)  # Titulo
    ultimo_grado_aprobado = models.ForeignKey(Grado, on_delete=models.DO_NOTHING, null=True)  # Grado
    indigena = models.BooleanField()  # BooleanField
    ingreso_mensual = models.FloatField(null=True)  # FloatField
    observaciones = models.TextField(null=True)  # TextField

    def url(self):
        return self.foto

    def foto_persona(self):
        # used in the admin site model as a "thumbnail"
        return mark_safe('<img src="../../../' + self.url().__str__() + '" width="70" height="50" />')

    def __str__(self):
        return self.nombre + ' - ' + self.apellido


class TipoParentesco(models.Model):
    tipoParentesco = models.CharField(max_length=30, null=True)  # CharField

    def __str__(self):
        return self.tipoParentesco


class Parentesco(models.Model):
    persona = models.ForeignKey(Persona, related_name='persona', on_delete=models.DO_NOTHING, null=True)  # Persona
    pariente = models.ForeignKey(Persona, related_name='pariente', on_delete=models.DO_NOTHING, null=True)  # Persona
    tipoParentesco = models.ForeignKey(TipoParentesco, on_delete=models.DO_NOTHING, null=True)  # TipoParentesco

    def __str__(self):
        return self.tipoParentesco

