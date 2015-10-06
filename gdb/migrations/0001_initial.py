# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Locality',
            fields=[
                ('locality_number', models.AutoField(serialize=False, primary_key=True)),
                ('locality_field_number', models.CharField(max_length=50, null=True, blank=True)),
                ('name', models.CharField(max_length=50, null=True, blank=True)),
                ('date_discovered', models.DateField(null=True, blank=True)),
                ('formation', models.CharField(max_length=50, null=True, blank=True)),
                ('member', models.CharField(max_length=50, null=True, blank=True)),
                ('NALMA', models.CharField(max_length=50, null=True, blank=True)),
                ('survey', models.CharField(max_length=50, null=True, blank=True)),
                ('quad_sheet', models.CharField(max_length=50, null=True, blank=True)),
                ('verbatim_latitude', models.CharField(max_length=50, null=True, blank=True)),
                ('verbatim_longitude', models.CharField(max_length=50, null=True, blank=True)),
                ('verbatim_utm', models.CharField(max_length=50, null=True, blank=True)),
                ('verbatim_gps_coordinates', models.CharField(max_length=50, null=True, blank=True)),
                ('verbatim_elevation', models.IntegerField(null=True, blank=True)),
                ('gps_date', models.DateField(null=True, blank=True)),
                ('resource_area', models.CharField(max_length=50, null=True, blank=True)),
                ('notes', models.TextField(null=True, blank=True)),
                ('cm_locality_number', models.IntegerField(null=True, blank=True)),
                ('region', models.CharField(max_length=50, null=True, blank=True)),
                ('blm_district', models.CharField(max_length=50, null=True, blank=True)),
                ('county', models.CharField(max_length=50, null=True, blank=True)),
                ('image', models.FileField(max_length=255, null=True, upload_to=b'uploads/images/gdb', blank=True)),
                ('geom', django.contrib.gis.db.models.fields.GeometryField(srid=4326, null=True, blank=True)),
                ('date_last_modified', models.DateTimeField(auto_now=True, verbose_name=b'Date Last Modified')),
            ],
            options={
                'verbose_name_plural': 'GDB Localities',
            },
        ),
        migrations.CreateModel(
            name='Occurrence',
            fields=[
                ('specimen_number', models.AutoField(serialize=False, primary_key=True)),
                ('cm_specimen_number', models.IntegerField(null=True, blank=True)),
                ('date_collected', models.DateField(null=True, blank=True)),
                ('time_collected', models.CharField(max_length=50, null=True, blank=True)),
                ('date_last_modified', models.DateTimeField(auto_now=True, verbose_name=b'Date Last Modified')),
                ('basis_of_record', models.CharField(blank=True, max_length=50, verbose_name=b'Basis of Record', choices=[(b'FossilSpecimen', b'Fossil'), (b'HumanObservation', b'Observation')])),
                ('item_type', models.CharField(blank=True, max_length=255, null=True, verbose_name=b'Item Type', choices=[(b'Artifactual', b'Artifactual'), (b'Faunal', b'Faunal'), (b'Floral', b'Floral'), (b'Geological', b'Geological')])),
                ('collecting_method', models.CharField(blank=True, max_length=50, null=True, verbose_name=b'Collecting Method', choices=[(b'Surface Standard', b'Surface Standard'), (b'Surface Intensive', b'Surface Intensive'), (b'Surface Complete', b'Surface Complete'), (b'Exploratory Survey', b'Exploratory Survey'), (b'Dry Screen 5mm', b'Dry Screen 5mm'), (b'Dry Screen 2mm', b'Dry Screen 2mm'), (b'Wet Screen 1mm', b'Wet Screen 1mm')])),
                ('related_catalog_items', models.CharField(max_length=50, null=True, verbose_name=b'Related Catalog Items', blank=True)),
                ('item_scientific_name', models.CharField(max_length=255, null=True, verbose_name=b'Scientific Name', blank=True)),
                ('item_description', models.CharField(max_length=255, null=True, blank=True)),
                ('image', models.FileField(max_length=255, null=True, upload_to=b'uploads/images/gdb', blank=True)),
                ('loan_date', models.DateField(null=True, blank=True)),
                ('loan_recipient', models.CharField(max_length=255, null=True, blank=True)),
                ('on_loan', models.BooleanField(default=False)),
                ('geom', django.contrib.gis.db.models.fields.GeometryField(srid=4326, null=True, blank=True)),
            ],
            options={
                'verbose_name': 'GDB Occurrence',
            },
        ),
        migrations.CreateModel(
            name='Biology',
            fields=[
                ('occurrence_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='gdb.Occurrence')),
                ('kingdom', models.CharField(max_length=50, null=True, blank=True)),
                ('phylum', models.CharField(max_length=50, null=True, blank=True)),
                ('tax_class', models.CharField(max_length=50, null=True, verbose_name=b'Class', blank=True)),
                ('tax_order', models.CharField(max_length=50, null=True, verbose_name=b'Order', blank=True)),
                ('family', models.CharField(max_length=50, null=True, blank=True)),
                ('subfamily', models.CharField(max_length=50, null=True, blank=True)),
                ('tribe', models.CharField(max_length=50, null=True, blank=True)),
                ('genus', models.CharField(max_length=50, null=True, blank=True)),
                ('specific_epithet', models.CharField(max_length=50, null=True, verbose_name=b'Species Name', blank=True)),
                ('infraspecific_epithet', models.CharField(max_length=50, null=True, blank=True)),
                ('infraspecific_rank', models.CharField(max_length=50, null=True, blank=True)),
                ('author_year_of_scientific_name', models.CharField(max_length=50, null=True, blank=True)),
                ('nomenclatural_code', models.CharField(max_length=50, null=True, blank=True)),
                ('identification_qualifier', models.CharField(max_length=50, null=True, blank=True)),
                ('identified_by', models.CharField(max_length=100, null=True, blank=True)),
                ('date_identified', models.DateTimeField(null=True, blank=True)),
                ('type_status', models.CharField(max_length=50, null=True, blank=True)),
                ('sex', models.CharField(max_length=50, null=True, blank=True)),
                ('life_stage', models.CharField(max_length=50, null=True, blank=True)),
                ('preparations', models.CharField(max_length=50, null=True, blank=True)),
                ('morphobank_num', models.IntegerField(null=True, blank=True)),
                ('element', models.CharField(max_length=50, null=True, blank=True)),
                ('side', models.CharField(max_length=50, null=True, blank=True)),
                ('attributes', models.CharField(max_length=50, null=True, blank=True)),
                ('notes', models.TextField(max_length=64000, null=True, blank=True)),
                ('lower_tooth', models.CharField(max_length=50, null=True, blank=True)),
                ('upper_tooth', models.CharField(max_length=50, null=True, blank=True)),
                ('jaw', models.CharField(max_length=50, null=True, blank=True)),
                ('mandible', models.CharField(max_length=50, null=True, blank=True)),
                ('maxilla', models.CharField(max_length=50, null=True, blank=True)),
                ('teeth', models.CharField(max_length=50, null=True, blank=True)),
                ('cranial', models.CharField(max_length=50, null=True, blank=True)),
                ('miscellaneous', models.CharField(max_length=50, null=True, blank=True)),
                ('vertebral', models.CharField(max_length=50, null=True, blank=True)),
                ('forelimb', models.CharField(max_length=50, null=True, blank=True)),
                ('hindlimb', models.CharField(max_length=50, null=True, blank=True)),
                ('NALMA', models.CharField(max_length=50, null=True, blank=True)),
                ('sub_age', models.CharField(max_length=50, null=True, blank=True)),
            ],
            options={
                'verbose_name': 'GDB Biology',
                'verbose_name_plural': 'GDB Biology Items',
            },
            bases=('gdb.occurrence',),
        ),
        migrations.AddField(
            model_name='occurrence',
            name='locality',
            field=models.ForeignKey(to='gdb.Locality'),
        ),
    ]
