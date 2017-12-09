# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hrp', '0004_auto_20160622_1256'),
    ]

    operations = [
        migrations.AddField(
            model_name='occurrence',
            name='timestamp',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='occurrence',
            name='basis_of_record',
            field=models.CharField(blank=True, max_length=50, verbose_name=b'Basis of Record', choices=[(b'Collection', b'Collection'), (b'Observation', b'Observation')]),
        ),
        migrations.AlterField(
            model_name='occurrence',
            name='collecting_method',
            field=models.CharField(max_length=50, choices=[(b'Surface Standard', b'Surface Standard'), (b'Surface Intensive', b'Surface Intensive'), (b'Surface Complete', b'Surface Complete'), (b'Exploratory Survey', b'Exploratory Survey'), (b'Dry Screen 5mm', b'Dry Screen 5mm'), (b'Dry Screen 2mm', b'Dry Screen 2mm'), (b'Wet Screen 1mm', b'Wet Screen 1mm')]),
        ),
        migrations.AlterField(
            model_name='occurrence',
            name='field_number',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
    ]
