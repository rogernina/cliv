# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2017-06-28 20:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('configuracion', '0003_antiparasitario_servicios_vacunas'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicios',
            name='precio',
            field=models.CharField(max_length=50),
        ),
    ]
