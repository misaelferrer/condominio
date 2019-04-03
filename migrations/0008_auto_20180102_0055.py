# Generated by Django 2.0 on 2018-01-02 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('censo', '0007_auto_20180102_0048'),
    ]

    operations = [
        migrations.CreateModel(
            name='Documento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=15)),
                ('documento', models.ImageField(blank=True, upload_to='documentos/')),
            ],
        ),
        migrations.AddField(
            model_name='persona',
            name='documento',
            field=models.ManyToManyField(to='censo.Documento'),
        ),
    ]