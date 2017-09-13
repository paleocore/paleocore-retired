# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hrp', '0030_auto_20170803_1625'),
    ]

    operations = [
        migrations.AddField(
            model_name='occurrence',
            name='found_by',
            field=models.ForeignKey(related_name='occurrence_found_by', blank=True, to='hrp.Person', null=True),
        ),
        migrations.AddField(
            model_name='occurrence',
            name='recorded_by',
            field=models.ForeignKey(related_name='occurrence_recorded_by', blank=True, to='hrp.Person', null=True),
        ),
    ]
