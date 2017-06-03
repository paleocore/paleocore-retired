# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lgrp', '0003_auto_20170501_1922'),
    ]

    operations = [
        migrations.AddField(
            model_name='occurrence',
            name='old_cat_number',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
    ]
