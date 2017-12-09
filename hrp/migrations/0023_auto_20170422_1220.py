# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hrp', '0022_auto_20170422_1146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='biology',
            name='identification_qualifier',
            field=models.ForeignKey(related_name='hrp_id_qualifier_bio_occurrences', on_delete=django.db.models.deletion.SET_NULL, blank=True, to='taxonomy.IdentificationQualifier', null=True),
        ),
        migrations.AlterField(
            model_name='biology',
            name='qualifier_taxon',
            field=models.ForeignKey(related_name='hrp_qualifier_taxon_bio_occurrences', on_delete=django.db.models.deletion.SET_NULL, blank=True, to='taxonomy.Taxon', null=True),
        ),
    ]
