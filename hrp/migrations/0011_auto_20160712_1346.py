# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hrp', '0010_auto_20160711_1629'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='locality',
            options={'ordering': ('locality_number', 'sublocality'), 'verbose_name': 'HRP Locality', 'verbose_name_plural': 'HRP Localities'},
        ),
        migrations.RenameField(
            model_name='locality',
            old_name='paleolocality_number',
            new_name='locality_number',
        ),
        migrations.RemoveField(
            model_name='locality',
            name='paleo_sublocality',
        ),
        migrations.RemoveField(
            model_name='occurrence',
            name='locality_text',
        ),
        migrations.RemoveField(
            model_name='occurrence',
            name='paleo_sublocality',
        ),
        migrations.RemoveField(
            model_name='occurrence',
            name='paleolocality_number',
        ),
    ]
