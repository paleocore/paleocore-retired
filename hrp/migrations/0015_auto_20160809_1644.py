# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('taxonomy', '0003_remove_identificationqualifier_taxon'),
        ('hrp', '0014_auto_20160802_1445'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='biology',
            name='author_year_of_scientific_name',
        ),
        migrations.RemoveField(
            model_name='biology',
            name='date_identified',
        ),
        migrations.RemoveField(
            model_name='biology',
            name='infraspecific_epithet',
        ),
        migrations.RemoveField(
            model_name='biology',
            name='infraspecific_rank',
        ),
        migrations.RemoveField(
            model_name='biology',
            name='nomenclatural_code',
        ),
        migrations.AddField(
            model_name='biology',
            name='qualifier_taxon',
            field=models.ForeignKey(blank=True, to='taxonomy.Taxon', null=True),
        ),
        migrations.AddField(
            model_name='biology',
            name='vertbatim_identification_qualifier',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='biology',
            name='year_identified',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
