# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('origins', '0011_auto_20171209_1745'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fossilelement',
            old_name='HomininElement',
            new_name='hominin_element',
        ),
        migrations.RenameField(
            model_name='fossilelement',
            old_name='HomininElementNotes',
            new_name='hominin_element_notes',
        ),
        migrations.RenameField(
            model_name='fossilelement',
            old_name='Locality',
            new_name='skeletal_element',
        ),
        migrations.RenameField(
            model_name='fossilelement',
            old_name='SkeletalElement',
            new_name='skeletal_element_class',
        ),
        migrations.RenameField(
            model_name='fossilelement',
            old_name='SkeletalElementClass',
            new_name='skeletal_element_complete',
        ),
        migrations.RenameField(
            model_name='fossilelement',
            old_name='SkeletalElementComplete',
            new_name='skeletal_element_position',
        ),
        migrations.RenameField(
            model_name='fossilelement',
            old_name='SkeletalElementPosition',
            new_name='skeletal_element_side',
        ),
        migrations.RenameField(
            model_name='fossilelement',
            old_name='SkeletalElementSide',
            new_name='skeletal_element_subunit',
        ),
        migrations.RenameField(
            model_name='fossilelement',
            old_name='PlaceName',
            new_name='skeletal_element_subunit_descriptor',
        ),
        migrations.RemoveField(
            model_name='fossilelement',
            name='Country',
        ),
        migrations.RemoveField(
            model_name='fossilelement',
            name='SkeletalElementSubUnit',
        ),
        migrations.RemoveField(
            model_name='fossilelement',
            name='SkeletalElementSubUnitDescriptor',
        ),
    ]
