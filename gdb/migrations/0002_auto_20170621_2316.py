# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gdb', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='occurrence',
            name='date_time_collected',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='occurrence',
            name='locality',
            field=models.ForeignKey(blank=True, to='gdb.Locality', null=True),
        ),
    ]
