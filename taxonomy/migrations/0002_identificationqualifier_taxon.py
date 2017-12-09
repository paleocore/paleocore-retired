# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('taxonomy', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='identificationqualifier',
            name='taxon',
            field=models.ForeignKey(blank=True, to='taxonomy.Taxon', null=True),
        ),
    ]
