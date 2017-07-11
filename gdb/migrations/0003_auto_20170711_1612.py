# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gdb', '0002_auto_20170621_2316'),
    ]

    operations = [
        migrations.AddField(
            model_name='occurrence',
            name='elevation',
            field=models.DecimalField(null=True, max_digits=10, decimal_places=4, blank=True),
        ),
        migrations.AlterField(
            model_name='occurrence',
            name='basis_of_record',
            field=models.CharField(max_length=50, verbose_name=b'Basis of Record', choices=[(b'FossilSpecimen', b'Fossil'), (b'HumanObservation', b'Observation')]),
        ),
        migrations.AlterField(
            model_name='occurrence',
            name='item_description',
            field=models.CharField(max_length=255, null=True, verbose_name=b'Description', blank=True),
        ),
    ]
