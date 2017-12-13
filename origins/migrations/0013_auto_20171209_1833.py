# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('origins', '0012_auto_20171209_1807'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fossil',
            old_name='PlaceName',
            new_name='place_name',
        ),
        migrations.RemoveField(
            model_name='fossil',
            name='Country',
        ),
        migrations.RemoveField(
            model_name='fossil',
            name='HomininElement',
        ),
        migrations.RemoveField(
            model_name='fossil',
            name='HomininElementNotes',
        ),
        migrations.RemoveField(
            model_name='fossil',
            name='Locality',
        ),
        migrations.RemoveField(
            model_name='fossil',
            name='SkeletalElement',
        ),
        migrations.RemoveField(
            model_name='fossil',
            name='SkeletalElementClass',
        ),
        migrations.RemoveField(
            model_name='fossil',
            name='SkeletalElementComplete',
        ),
        migrations.RemoveField(
            model_name='fossil',
            name='SkeletalElementPosition',
        ),
        migrations.RemoveField(
            model_name='fossil',
            name='SkeletalElementSide',
        ),
        migrations.RemoveField(
            model_name='fossil',
            name='SkeletalElementSubUnit',
        ),
        migrations.RemoveField(
            model_name='fossil',
            name='SkeletalElementSubUnitDescriptor',
        ),
        migrations.AlterField(
            model_name='fossilelement',
            name='fossil',
            field=models.ForeignKey(related_name='fossil_element', to='origins.Fossil', null=True),
        ),
    ]
