# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('standard', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='term',
            name='is_class',
            field=models.BooleanField(default=False),
        ),
    ]
