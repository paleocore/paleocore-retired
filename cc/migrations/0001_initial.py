# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Context',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cat_no', models.CharField(max_length=12)),
                ('unit', models.CharField(max_length=6)),
                ('id_no', models.CharField(max_length=6, verbose_name=b'ID')),
                ('level', models.CharField(max_length=50, null=True, blank=True)),
                ('code', models.CharField(max_length=25, null=True, blank=True)),
                ('excavator', models.CharField(max_length=50, null=True, blank=True)),
                ('exc_date', models.DateField(null=True, verbose_name=b'Date', blank=True)),
                ('exc_time', models.TimeField(null=True, verbose_name=b'Time', blank=True)),
                ('points', django.contrib.gis.db.models.fields.GeometryField(srid=-1, dim=3, null=True, blank=True)),
            ],
            options={
                'verbose_name': 'cc Context',
                'managed': True,
                'verbose_name_plural': 'cc Context (Catalog)',
            },
        ),
        migrations.CreateModel(
            name='Excavation_unit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('unit', models.CharField(max_length=6)),
                ('extent', django.contrib.gis.db.models.fields.GeometryField(srid=-1, dim=3, null=True, blank=True)),
            ],
            options={
                'verbose_name': 'Excavation Unit',
                'managed': True,
                'verbose_name_plural': 'Excavation units',
            },
        ),
        migrations.CreateModel(
            name='Lithic',
            fields=[
                ('context_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cc.Context')),
                ('dataclass', models.CharField(max_length=20, null=True, blank=True)),
                ('cortex', models.CharField(max_length=10, null=True, blank=True)),
                ('technique', models.CharField(max_length=20, null=True, blank=True)),
                ('alteration', models.CharField(max_length=20, null=True, blank=True)),
                ('edge_damage', models.CharField(max_length=20, null=True, blank=True)),
                ('fb_type', models.IntegerField(null=True, verbose_name=b'Bordes Type', blank=True)),
                ('fb_type_2', models.IntegerField(null=True, verbose_name=b'Bordes Type 2', blank=True)),
                ('fb_type_3', models.IntegerField(null=True, verbose_name=b'Bordes Type 3', blank=True)),
                ('platform_surface', models.CharField(max_length=20, null=True, blank=True)),
                ('platform_exterior', models.CharField(max_length=20, null=True, blank=True)),
                ('form', models.CharField(max_length=20, null=True, blank=True)),
                ('scar_morphology', models.CharField(max_length=20, null=True, blank=True)),
                ('retouched_edges', models.IntegerField(null=True, blank=True)),
                ('retouch_intensity', models.CharField(max_length=20, null=True, blank=True)),
                ('reprise', models.CharField(max_length=20, null=True, blank=True)),
                ('length', models.DecimalField(null=True, max_digits=10, decimal_places=2, blank=True)),
                ('width', models.DecimalField(null=True, max_digits=10, decimal_places=2, blank=True)),
                ('maximum_width', models.DecimalField(null=True, max_digits=10, decimal_places=2, blank=True)),
                ('thickness', models.DecimalField(null=True, max_digits=10, decimal_places=2, blank=True)),
                ('platform_width', models.DecimalField(null=True, max_digits=10, decimal_places=2, blank=True)),
                ('platform_thickness', models.DecimalField(null=True, max_digits=10, decimal_places=2, blank=True)),
                ('raw_material', models.CharField(max_length=20, null=True, blank=True)),
                ('exterior_surface', models.CharField(max_length=20, null=True, blank=True)),
                ('exterior_type', models.CharField(max_length=20, null=True, blank=True)),
                ('weight', models.DecimalField(null=True, max_digits=10, decimal_places=2, blank=True)),
                ('platform_technique', models.CharField(max_length=20, null=True, blank=True)),
                ('platform_angle', models.DecimalField(null=True, max_digits=3, decimal_places=0, blank=True)),
                ('multiple', models.NullBooleanField(default=False)),
                ('epa', models.IntegerField(null=True, blank=True)),
                ('core_shape', models.CharField(max_length=20, null=True, blank=True)),
                ('core_blank', models.CharField(max_length=20, null=True, blank=True)),
                ('core_surface_percentage', models.DecimalField(null=True, max_digits=3, decimal_places=0, blank=True)),
                ('proximal_removals', models.IntegerField(null=True, blank=True)),
                ('prepared_platforms', models.IntegerField(null=True, blank=True)),
                ('flake_direction', models.CharField(max_length=20, null=True, blank=True)),
                ('scar_length', models.DecimalField(null=True, max_digits=10, decimal_places=2, blank=True)),
                ('scar_width', models.DecimalField(null=True, max_digits=10, decimal_places=2, blank=True)),
            ],
            options={
                'verbose_name': 'cc Lithic',
                'managed': True,
                'verbose_name_plural': 'cc Lithics',
            },
            bases=('cc.context',),
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('context_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cc.Context')),
                ('image01', models.ImageField(upload_to=b'/media/', null=True, verbose_name=b'Image', blank=True)),
            ],
            options={
                'verbose_name': 'cc Image',
                'managed': True,
                'verbose_name_plural': 'cc Images',
            },
            bases=('cc.context',),
        ),
        migrations.CreateModel(
            name='Small_Find',
            fields=[
                ('context_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cc.Context')),
                ('coarse_stone_weight', models.IntegerField(null=True, blank=True)),
                ('coarse_fauna_weight', models.IntegerField(null=True, blank=True)),
                ('fine_stone_weight', models.IntegerField(null=True, blank=True)),
                ('fine_fauna_weight', models.IntegerField(null=True, blank=True)),
            ],
            options={
                'verbose_name': 'cc Small find (bucket)',
                'managed': True,
                'verbose_name_plural': 'cc Small finds (buckets)',
            },
            bases=('cc.context',),
        ),
        migrations.CreateModel(
            name='Lithics_with_Photos',
            fields=[
            ],
            options={
                'verbose_name': 'cc Lithic (only with photo)',
                'managed': True,
                'proxy': True,
                'verbose_name_plural': 'cc Lithics (only with photos)',
            },
            bases=('cc.context',),
        ),
    ]
