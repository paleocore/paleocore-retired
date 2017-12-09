# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hrp', '0008_auto_20160707_1345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='occurrence',
            name='item_number',
            field=models.FloatField(null=True, verbose_name=b'Item #', blank=True),
        ),
    ]
