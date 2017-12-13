# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('origins', '0009_auto_20171209_1702'),
    ]

    operations = [
        migrations.AddField(
            model_name='fossil',
            name='verbatim_Country',
            field=models.CharField(max_length=20, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='fossil',
            name='verbatim_HomininElement',
            field=models.CharField(max_length=40, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='fossil',
            name='verbatim_HomininElementNotes',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='fossil',
            name='verbatim_Locality',
            field=models.CharField(max_length=40, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='fossil',
            name='verbatim_PlaceName',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='fossil',
            name='verbatim_SkeletalElement',
            field=models.CharField(max_length=40, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='fossil',
            name='verbatim_SkeletalElementClass',
            field=models.CharField(max_length=40, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='fossil',
            name='verbatim_SkeletalElementComplete',
            field=models.CharField(max_length=40, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='fossil',
            name='verbatim_SkeletalElementPosition',
            field=models.CharField(max_length=40, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='fossil',
            name='verbatim_SkeletalElementSide',
            field=models.CharField(max_length=40, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='fossil',
            name='verbatim_SkeletalElementSubUnit',
            field=models.CharField(max_length=40, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='fossil',
            name='verbatim_SkeletalElementSubUnitDescriptor',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
    ]
