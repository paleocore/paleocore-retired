# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('origins', '0014_fossil_origins'),
    ]

    operations = [
        migrations.RenameField(
            model_name='site',
            old_name='collection_aka',
            new_name='verbatim_collection_aka',
        ),
        migrations.RenameField(
            model_name='site',
            old_name='collection_name',
            new_name='verbatim_collection_name',
        ),
        migrations.RenameField(
            model_name='site',
            old_name='collection_no',
            new_name='verbatim_collection_no',
        ),
        migrations.RenameField(
            model_name='site',
            old_name='collection_subset',
            new_name='verbatim_collection_subset',
        ),
        migrations.RenameField(
            model_name='site',
            old_name='early_interval',
            new_name='verbatim_early_interval',
        ),
        migrations.RenameField(
            model_name='site',
            old_name='formation',
            new_name='verbatim_formation',
        ),
        migrations.RenameField(
            model_name='site',
            old_name='lat',
            new_name='verbatim_lat',
        ),
        migrations.RenameField(
            model_name='site',
            old_name='late_interval',
            new_name='verbatim_late_interval',
        ),
        migrations.RenameField(
            model_name='site',
            old_name='lng',
            new_name='verbatim_lng',
        ),
        migrations.RenameField(
            model_name='site',
            old_name='max_ma',
            new_name='verbatim_max_ma',
        ),
        migrations.RenameField(
            model_name='site',
            old_name='min_ma',
            new_name='verbatim_min_ma',
        ),
        migrations.RenameField(
            model_name='site',
            old_name='n_occs',
            new_name='verbatim_n_occs',
        ),
        migrations.RenameField(
            model_name='site',
            old_name='record_type',
            new_name='verbatim_record_type',
        ),
        migrations.RenameField(
            model_name='site',
            old_name='reference_no',
            new_name='verbatim_reference_no',
        ),
    ]
