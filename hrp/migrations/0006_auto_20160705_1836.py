# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hrp', '0005_auto_20160627_1720'),
    ]

    operations = [
        migrations.RenameField(
            model_name='occurrence',
            old_name='analytical_unit_1',
            new_name='analytical_unit',
        ),
    ]
