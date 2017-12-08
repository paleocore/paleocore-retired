# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('origins', '0007_reference_fossil'),
    ]

    operations = [
        migrations.AddField(
            model_name='context',
            name='best_age',
            field=models.DecimalField(null=True, max_digits=20, decimal_places=10, blank=True),
        ),
        migrations.AddField(
            model_name='context',
            name='geological_bed',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='context',
            name='geological_formation',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='context',
            name='geological_member',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='context',
            name='max_age',
            field=models.DecimalField(null=True, max_digits=20, decimal_places=10, blank=True),
        ),
        migrations.AddField(
            model_name='context',
            name='min_age',
            field=models.DecimalField(null=True, max_digits=20, decimal_places=10, blank=True),
        ),
        migrations.AddField(
            model_name='context',
            name='older_interval',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='context',
            name='younger_interval',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='reference',
            name='fossil',
            field=models.ManyToManyField(to='origins.Fossil'),
        ),
    ]
