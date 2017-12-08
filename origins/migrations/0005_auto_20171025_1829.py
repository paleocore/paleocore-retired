# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('origins', '0004_auto_20171025_1822'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fossil',
            name='country',
            field=django_countries.fields.CountryField(blank=True, max_length=2, null=True, verbose_name=b'Country'),
        ),
    ]
