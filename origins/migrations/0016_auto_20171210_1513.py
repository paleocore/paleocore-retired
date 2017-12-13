# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('origins', '0015_auto_20171210_1315'),
    ]

    operations = [
        migrations.RenameField(
            model_name='context',
            old_name='collection_name',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='context',
            name='collection_aka',
        ),
        migrations.RemoveField(
            model_name='context',
            name='collection_no',
        ),
        migrations.RemoveField(
            model_name='context',
            name='collection_subset',
        ),
        migrations.RemoveField(
            model_name='context',
            name='early_interval',
        ),
        migrations.RemoveField(
            model_name='context',
            name='formation',
        ),
        migrations.RemoveField(
            model_name='context',
            name='lat',
        ),
        migrations.RemoveField(
            model_name='context',
            name='late_interval',
        ),
        migrations.RemoveField(
            model_name='context',
            name='lng',
        ),
        migrations.RemoveField(
            model_name='context',
            name='max_ma',
        ),
        migrations.RemoveField(
            model_name='context',
            name='member',
        ),
        migrations.RemoveField(
            model_name='context',
            name='min_ma',
        ),
        migrations.RemoveField(
            model_name='context',
            name='n_occs',
        ),
        migrations.RemoveField(
            model_name='context',
            name='record_type',
        ),
        migrations.RemoveField(
            model_name='context',
            name='reference_no',
        ),
        migrations.AlterField(
            model_name='context',
            name='geological_formation',
            field=models.CharField(max_length=50, null=True, verbose_name=b'Formation', blank=True),
        ),
        migrations.AlterField(
            model_name='context',
            name='geological_member',
            field=models.CharField(max_length=50, null=True, verbose_name=b'Member', blank=True),
        ),
    ]
