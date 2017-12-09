# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hrp', '0020_auto_20160816_1145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='biology',
            name='identification_qualifier',
            field=models.ForeignKey(related_name='hrp_id_qualifier_bio_occurrences', blank=True, to='taxonomy.IdentificationQualifier', null=True),
        ),
        migrations.AlterField(
            model_name='biology',
            name='qualifier_taxon',
            field=models.ForeignKey(related_name='hrp_qualifier_taxon_bio_occurrences', blank=True, to='taxonomy.Taxon', null=True),
        ),
        migrations.AlterField(
            model_name='biology',
            name='taxon',
            field=models.ForeignKey(related_name='hrp_taxon_bio_occurrences', to='taxonomy.Taxon'),
        ),
    ]
