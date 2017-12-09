# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hrp', '0009_auto_20160707_1411'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='occurrence',
            name='catalog_number',
        ),
        migrations.AlterField(
            model_name='occurrence',
            name='item_number',
            field=models.IntegerField(null=True, verbose_name=b'Item #', blank=True),
        ),
    ]
