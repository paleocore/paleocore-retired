# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hrp', '0021_auto_20160928_1435'),
    ]

    operations = [
        migrations.AlterField(
            model_name='biology',
            name='taxon',
            field=models.ForeignKey(related_name='hrp_taxon_bio_occurrences', on_delete=django.db.models.deletion.SET_DEFAULT, default=0, to='taxonomy.Taxon'),
        ),
    ]
