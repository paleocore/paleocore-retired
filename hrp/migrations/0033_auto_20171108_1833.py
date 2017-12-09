# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hrp', '0032_taxonomy'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='identificationqualifier',
            options={'verbose_name': 'HRP Idenfication Qualifer'},
        ),
        migrations.AlterModelOptions(
            name='taxon',
            options={'ordering': ['rank__ordinal', 'name'], 'verbose_name': 'HRP Taxon', 'verbose_name_plural': 'HRP Taxa'},
        ),
        migrations.AlterModelOptions(
            name='taxonrank',
            options={'verbose_name': 'HRP Taxon Rank'},
        ),
    ]
