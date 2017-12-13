# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('origins', '0013_auto_20171209_1833'),
    ]

    operations = [
        migrations.AddField(
            model_name='fossil',
            name='origins',
            field=models.BooleanField(default=False),
        ),
    ]
