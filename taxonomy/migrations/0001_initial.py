# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='IdentificationQualifier',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=15, blank=True)),
                ('qualified', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Taxon',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('parent', models.ForeignKey(blank=True, to='taxonomy.Taxon', null=True)),
            ],
            options={
                'ordering': ['rank__ordinal', 'name'],
                'verbose_name': 'Taxon',
                'verbose_name_plural': 'taxa',
            },
        ),
        migrations.CreateModel(
            name='TaxonRank',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=50)),
                ('plural', models.CharField(unique=True, max_length=50)),
                ('ordinal', models.IntegerField(unique=True)),
            ],
            options={
                'verbose_name': 'Taxon Rank',
            },
        ),
        migrations.AddField(
            model_name='taxon',
            name='rank',
            field=models.ForeignKey(to='taxonomy.TaxonRank'),
        ),
    ]
