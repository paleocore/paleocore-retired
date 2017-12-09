# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hrp', '0002_auto_20160615_1726'),
    ]

    operations = [
        migrations.AlterField(
            model_name='locality',
            name='id',
            field=models.CharField(max_length=255, serialize=False, primary_key=True),
        ),
    ]
