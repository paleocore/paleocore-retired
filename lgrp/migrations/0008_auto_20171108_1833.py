# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lgrp', '0007_taxonomy'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='taxon',
            options={'ordering': ['rank__ordinal', 'name'], 'verbose_name': 'LGRP Taxon', 'verbose_name_plural': 'LGRP Taxa'},
        ),
    ]
