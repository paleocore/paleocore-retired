# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hrp', '0007_auto_20160705_1939'),
    ]

    operations = [
        migrations.AlterField(
            model_name='occurrence',
            name='collecting_method',
            field=models.CharField(max_length=50, null=True, choices=[(b'Survey', b'Survey'), (b'dryscreen5mm', b'dryscreen5mm'), (b'wetscreen1mm', b'wetscreen1mm')]),
        ),
    ]
