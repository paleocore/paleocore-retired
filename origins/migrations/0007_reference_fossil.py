# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('origins', '0006_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='reference',
            name='fossil',
            field=models.ManyToManyField(to='origins.Fossil', null=True, blank=True),
        ),
    ]
