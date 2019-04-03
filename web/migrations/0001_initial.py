# Generated by Django 2.1.7 on 2019-02-27 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Galeria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(null=True, upload_to='static/fondo/seccion4/')),
                ('titulo', models.CharField(max_length=50, null=True)),
                ('subtitulo', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Icono',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=25, null=True)),
                ('icono', models.CharField(max_length=15, null=True)),
                ('cuenta', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=25, null=True)),
                ('link', models.URLField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Seccion1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emergente', models.CharField(max_length=50, null=True)),
                ('fondo', models.ImageField(null=True, upload_to='static/fondo/seccion1/')),
                ('titulo', models.CharField(max_length=50, null=True)),
                ('subtitulo', models.CharField(max_length=50, null=True)),
                ('parrafo', models.TextField(null=True)),
                ('labelboton', models.CharField(max_length=20, null=True)),
                ('link', models.URLField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Seccion2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fondo', models.ImageField(null=True, upload_to='static/fondo/seccion2/')),
                ('titulo', models.CharField(max_length=50, null=True)),
                ('parrafo', models.TextField(null=True)),
                ('link', models.URLField(max_length=50, null=True)),
                ('iconos', models.ManyToManyField(to='web.Icono')),
            ],
        ),
        migrations.CreateModel(
            name='Seccion3',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Seccion4',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50, null=True)),
                ('galeria', models.ManyToManyField(to='web.Galeria')),
            ],
        ),
        migrations.CreateModel(
            name='Seccion5',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Seccion6',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50, null=True)),
                ('parrafo', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Seccion7',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foto', models.ImageField(null=True, upload_to='static/fondo/seccion7/')),
                ('autor', models.CharField(max_length=50, null=True)),
                ('fecha', models.DateField(null=True)),
                ('descripcion', models.CharField(max_length=20, null=True)),
                ('precio', models.CharField(max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Seccion8',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('direccion', models.TextField(null=True)),
                ('email', models.EmailField(max_length=50, null=True)),
                ('telefono', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=25, null=True)),
                ('icono', models.CharField(max_length=15, null=True)),
                ('link', models.URLField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sugerencia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, null=True)),
                ('email', models.EmailField(max_length=50, null=True)),
                ('telefono', models.CharField(max_length=50, null=True)),
                ('Mensaje', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Titular',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, null=True)),
                ('link', models.URLField(max_length=50, null=True)),
                ('fondo', models.ImageField(null=True, upload_to='static/fondo/principal/')),
                ('subtitulo', models.CharField(max_length=50, null=True)),
                ('pie', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Voceria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foto', models.ImageField(null=True, upload_to='static/fondo/seccion5/')),
                ('nombre', models.CharField(max_length=50, null=True)),
                ('cargo', models.CharField(max_length=50, null=True)),
                ('twiter', models.CharField(max_length=20, null=True)),
                ('facebook', models.CharField(max_length=20, null=True)),
                ('google', models.CharField(max_length=20, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='seccion5',
            name='voceros',
            field=models.ManyToManyField(to='web.Voceria'),
        ),
        migrations.AddField(
            model_name='seccion3',
            name='servicios',
            field=models.ManyToManyField(to='web.Servicio'),
        ),
    ]