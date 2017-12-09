# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hrp', '0003_auto_20160617_1105'),
    ]

    operations = [
        migrations.AddField(
            model_name='occurrence',
            name='distance_from_found',
            field=models.DecimalField(null=True, max_digits=38, decimal_places=8, blank=True),
        ),
        migrations.AddField(
            model_name='occurrence',
            name='distance_from_likely',
            field=models.DecimalField(null=True, max_digits=38, decimal_places=8, blank=True),
        ),
        migrations.AddField(
            model_name='occurrence',
            name='distance_from_lower',
            field=models.DecimalField(null=True, max_digits=38, decimal_places=8, blank=True),
        ),
        migrations.AddField(
            model_name='occurrence',
            name='distance_from_upper',
            field=models.DecimalField(null=True, max_digits=38, decimal_places=8, blank=True),
        ),
        migrations.AddField(
            model_name='occurrence',
            name='stratigraphic_marker_found',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='occurrence',
            name='stratigraphic_marker_likely',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='occurrence',
            name='stratigraphic_marker_lower',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='occurrence',
            name='stratigraphic_marker_upper',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='occurrence',
            name='collection_code',
            field=models.CharField(max_length=20, null=True, verbose_name=b'Collection Code', blank=True),
        ),
    ]
