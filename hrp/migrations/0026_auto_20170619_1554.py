# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hrp', '0025_auto_20170619_1508'),
    ]

    operations = [
        migrations.RenameField(
            model_name='occurrence',
            old_name='analytical_unit',
            new_name='analytical_unit_1',
        ),
    ]
