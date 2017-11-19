# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2017-06-14 22:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0002_venta_codigo'),
        ('clinica', '0010_vacunacion_dosis'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vacunacion',
            name='vacuna',
        ),
        migrations.AddField(
            model_name='vacunacion',
            name='vacuna',
            field=models.ForeignKey(blank=True, default=1, max_length=100, on_delete=django.db.models.deletion.CASCADE, to='ventas.Producto'),
            preserve_default=False,
        ),
    ]
