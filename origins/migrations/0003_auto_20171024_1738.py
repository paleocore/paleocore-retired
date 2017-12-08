# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('origins', '0002_context_member'),
    ]

    operations = [
        migrations.CreateModel(
            name='IdentificationQualifier',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=15, blank=True)),
                ('qualified', models.BooleanField()),
            ],
            options={
                'verbose_name': 'Identification Qualifer',
            },
        ),
        migrations.CreateModel(
            name='Taxon',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('parent', models.ForeignKey(blank=True, to='origins.Taxon', null=True)),
            ],
            options={
                'ordering': ['rank__ordinal', 'name'],
                'verbose_name': 'Taxon',
                'verbose_name_plural': 'Taxa',
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
                'verbose_name': 'LGRP Taxon Rank',
            },
        ),
        migrations.AddField(
            model_name='fossil',
            name='catalog_number',
            field=models.CharField(max_length=40, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='fossil',
            name='collection_code',
            field=models.CharField(max_length=10, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='fossil',
            name='holotype',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='fossil',
            name='image',
            field=models.ImageField(max_length=255, null=True, upload_to=b'uploads/images/origins', blank=True),
        ),
        migrations.AddField(
            model_name='fossil',
            name='nickname',
            field=models.CharField(max_length=40, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='fossil',
            name='project_abbreviation',
            field=models.CharField(max_length=10, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='fossil',
            name='project_name',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='fossil',
            name='verbatim_provenience',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='reference',
            name='reference_pdf',
            field=models.FileField(max_length=255, null=True, upload_to=b'uploads/files/origins', blank=True),
        ),
        migrations.AddField(
            model_name='taxon',
            name='rank',
            field=models.ForeignKey(blank=True, to='origins.TaxonRank', null=True),
        ),
    ]
