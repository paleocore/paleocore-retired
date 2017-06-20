# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hrp', '0026_auto_20170619_1554'),
    ]

    operations = [
        migrations.AddField(
            model_name='biology',
            name='element_remarks',
            field=models.TextField(max_length=500, null=True, blank=True),
        ),
    ]