# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gdb', '0003_auto_20170711_1612'),
    ]

    operations = [
        migrations.AlterField(
            model_name='locality',
            name='locality_number',
            field=models.IntegerField(serialize=False, primary_key=True),
        ),
    ]
