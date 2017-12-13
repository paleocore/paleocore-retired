# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('origins', '0008_auto_20171025_2115'),
    ]

    operations = [
        migrations.AddField(
            model_name='context',
            name='verbatim_collection_aka',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='context',
            name='verbatim_collection_name',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='context',
            name='verbatim_collection_no',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='context',
            name='verbatim_collection_subset',
            field=models.CharField(max_length=20, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='context',
            name='verbatim_early_interval',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='context',
            name='verbatim_formation',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='context',
            name='verbatim_lat',
            field=models.DecimalField(null=True, max_digits=20, decimal_places=10, blank=True),
        ),
        migrations.AddField(
            model_name='context',
            name='verbatim_late_interval',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='context',
            name='verbatim_lng',
            field=models.DecimalField(null=True, max_digits=20, decimal_places=10, blank=True),
        ),
        migrations.AddField(
            model_name='context',
            name='verbatim_max_ma',
            field=models.DecimalField(null=True, max_digits=20, decimal_places=10, blank=True),
        ),
        migrations.AddField(
            model_name='context',
            name='verbatim_member',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='context',
            name='verbatim_min_ma',
            field=models.DecimalField(null=True, max_digits=20, decimal_places=10, blank=True),
        ),
        migrations.AddField(
            model_name='context',
            name='verbatim_n_occs',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='context',
            name='verbatim_record_type',
            field=models.CharField(max_length=20, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='context',
            name='verbatim_reference_no',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
