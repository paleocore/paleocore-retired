# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hrp', '0013_auto_20160712_1646'),
    ]

    operations = [
        migrations.AlterField(
            model_name='occurrence',
            name='collection_remarks',
            field=models.TextField(max_length=255, null=True, verbose_name=b'Remarks', blank=True),
        ),
        migrations.AlterField(
            model_name='occurrence',
            name='georeference_remarks',
            field=models.TextField(max_length=50, null=True, blank=True),
        ),
    ]
