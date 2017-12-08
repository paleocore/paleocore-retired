# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


def import_identification_qualifiers(apps, schema_editor):
    taxonomy_identification_qualifier = apps.get_model("taxonomy", "IdentificationQualifier")
    lgrp_identification_qualifier = apps.get_model("lgrp", "IdentificationQualifier")
    for idq in taxonomy_identification_qualifier.objects.all():
        lgrp_identification_qualifier.objects.create(
            id=idq.id,
            name=idq.name,
            qualified=idq.qualified
        )


def import_taxon_ranks(apps, schema_editor):
    taxonomy_TaxonRank = apps.get_model("taxonomy", "TaxonRank")
    lgrp_TaxonRank = apps.get_model("lgrp", "TaxonRank")

    for taxon_rank in taxonomy_TaxonRank.objects.all():
        lgrp_TaxonRank.objects.create(
            id=taxon_rank.id,
            name=taxon_rank.name,
            plural=taxon_rank.plural,
            ordinal=taxon_rank.ordinal
        )


def import_taxa(apps, schema_editor):
    taxonomy_Taxon = apps.get_model("taxonomy", "Taxon")
    lgrp_Taxon = apps.get_model("lgrp", "Taxon")
    for taxon in taxonomy_Taxon.objects.all():
        lgrp_Taxon.objects.create(
            id=taxon.id,
            name=taxon.name,
        )


def update_taxon(apps, schema_editor):
    taxonomy_Taxon = apps.get_model("taxonomy", "Taxon")
    lgrp_Taxon = apps.get_model("lgrp", "Taxon")
    lgrp_TaxonRank = apps.get_model("lgrp", "TaxonRank")
    for taxon in taxonomy_Taxon.objects.all():
        lgrp_taxon = lgrp_Taxon.objects.get(pk=taxon.id)
        try:
            lgrp_taxon.parent = lgrp_Taxon.objects.get(pk=taxon.parent.id)
        except AttributeError:
            lgrp_taxon.parent = None
        try:
            lgrp_taxon.rank = lgrp_TaxonRank.objects.get(pk=taxon.rank.id)
        except AttributeError:
            lgrp_taxon.rank = None
        lgrp_taxon.save()


def reverse(apps, schema_editor):
    pass


class Migration(migrations.Migration):
    dependencies = [
        ('lgrp', '0006_auto_20171003_1641'),
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
                'verbose_name': 'LGRP Idenfication Qualifer',
            },
        ),
        migrations.CreateModel(
            name='Taxon',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('parent', models.ForeignKey(blank=True, to='lgrp.Taxon', null=True)),
            ],
            options={
                'verbose_name': 'LGRP Taxon',
                'verbose_name_plural': 'LGRP Taxa',
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
        migrations.RunPython(import_identification_qualifiers, reverse_code=reverse),
        migrations.RunPython(import_taxon_ranks, reverse_code=reverse),
        migrations.RunPython(import_taxa, reverse_code=reverse),

        migrations.AlterField(
            model_name='biology',
            name='identification_qualifier',
            field=models.ForeignKey(related_name='lgrp_id_qualifier_bio_occurrences',
                                    on_delete=django.db.models.deletion.SET_NULL, blank=True,
                                    to='lgrp.IdentificationQualifier', null=True),
        ),
        migrations.AlterField(
            model_name='biology',
            name='qualifier_taxon',
            field=models.ForeignKey(related_name='lgrp_qualifier_taxon_bio_occurrences',
                                    on_delete=django.db.models.deletion.SET_NULL, blank=True, to='lgrp.Taxon',
                                    null=True),
        ),
        migrations.AlterField(
            model_name='biology',
            name='taxon',
            field=models.ForeignKey(related_name='lgrp_taxon_bio_occurrences',
                                    on_delete=django.db.models.deletion.SET_DEFAULT, default=0, to='lgrp.Taxon'),
        ),
        migrations.AddField(
            model_name='taxon',
            name='rank',
            field=models.ForeignKey(blank=True, to='lgrp.TaxonRank', null=True),
        ),

        migrations.RunPython(update_taxon, reverse_code=reverse),
    ]