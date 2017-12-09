# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gdb', '0004_auto_20170711_1727'),
    ]

    operations = [
        migrations.AlterField(
            model_name='biology',
            name='family',
            field=models.CharField(max_length=50, null=True, verbose_name=b'Family', blank=True),
        ),
        migrations.AlterField(
            model_name='biology',
            name='genus',
            field=models.CharField(max_length=50, null=True, verbose_name=b'Genus', blank=True),
        ),
        migrations.AlterField(
            model_name='biology',
            name='infraspecific_epithet',
            field=models.CharField(max_length=50, null=True, verbose_name=b'Infraspecies', blank=True),
        ),
        migrations.AlterField(
            model_name='biology',
            name='infraspecific_rank',
            field=models.CharField(max_length=50, null=True, verbose_name=b'Infraspecies rank', blank=True),
        ),
        migrations.AlterField(
            model_name='biology',
            name='kingdom',
            field=models.CharField(max_length=50, null=True, verbose_name=b'Kingdom', blank=True),
        ),
        migrations.AlterField(
            model_name='biology',
            name='phylum',
            field=models.CharField(max_length=50, null=True, verbose_name=b'Phylum', blank=True),
        ),
        migrations.AlterField(
            model_name='biology',
            name='subfamily',
            field=models.CharField(max_length=50, null=True, verbose_name=b'Subfamily', blank=True),
        ),
        migrations.AlterField(
            model_name='biology',
            name='tribe',
            field=models.CharField(max_length=50, null=True, verbose_name=b'Tribe', blank=True),
        ),
    ]
