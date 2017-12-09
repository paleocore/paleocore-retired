# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hrp', '0016_biology_verbatim_taxon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='biology',
            name='identification_qualifier',
            field=models.ForeignKey(related_name='hrp_biology_occurrences', blank=True, to='taxonomy.IdentificationQualifier', null=True),
        ),
    ]
