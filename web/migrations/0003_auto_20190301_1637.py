# Generated by Django 2.1.7 on 2019-03-01 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_auto_20190228_1622'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='link',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
