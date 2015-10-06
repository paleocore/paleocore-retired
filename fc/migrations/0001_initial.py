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
                ('collection', models.CharField(max_length=15)),
                ('unit', models.CharField(max_length=6)),
                ('id_no', models.CharField(max_length=6, verbose_name=b'ID')),
                ('sector', models.CharField(max_length=50, null=True, blank=True)),
                ('analytical_level', models.CharField(max_length=50, null=True, blank=True)),
                ('level', models.CharField(max_length=50, null=True, blank=True)),
                ('code', models.CharField(max_length=25, null=True, blank=True)),
                ('exc_date', models.DateField(null=True, verbose_name=b'Date', blank=True)),
                ('excavator', models.CharField(max_length=50, null=True, blank=True)),
                ('points', django.contrib.gis.db.models.fields.GeometryField(srid=-1, dim=3, null=True, blank=True)),
            ],
            options={
                'verbose_name': 'FC Context',
                'managed': True,
                'verbose_name_plural': 'FC Context (Catalog)',
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
                'verbose_name': 'FC Excavation Unit',
                'managed': True,
                'verbose_name_plural': 'FC Excavation units',
            },
        ),
        migrations.CreateModel(
            name='Granulometry',
            fields=[
                ('grain_id', models.AutoField(serialize=False, verbose_name=b'ID', primary_key=True)),
                ('weight', models.DecimalField(null=True, max_digits=10, decimal_places=2, blank=True)),
            ],
            options={
                'verbose_name': 'FC stone in a granulometry bucket',
                'managed': True,
                'verbose_name_plural': 'FC Granulometry',
            },
        ),
        migrations.CreateModel(
            name='Refits',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('unit', models.CharField(max_length=6)),
                ('id_no', models.CharField(max_length=6, verbose_name=b'ID')),
                ('counter', models.IntegerField(null=True, blank=True)),
            ],
            options={
                'verbose_name': 'FC Refit',
                'managed': True,
                'verbose_name_plural': 'FC Refits',
            },
        ),
        migrations.CreateModel(
            name='Small_Find_Weights',
            fields=[
                ('smalls_id', models.AutoField(serialize=False, verbose_name=b'ID', primary_key=True)),
                ('weight', models.DecimalField(null=True, max_digits=10, decimal_places=2, blank=True)),
            ],
            options={
                'verbose_name': 'FC artifact in a bucket',
                'managed': True,
                'verbose_name_plural': 'FC Small Finds (Weights by piece)',
            },
        ),
        migrations.CreateModel(
            name='Fauna',
            fields=[
                ('context_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='fc.Context')),
                ('tentative_ID', models.CharField(max_length=20, null=True, blank=True)),
                ('genus', models.CharField(max_length=30, null=True, blank=True)),
                ('side', models.CharField(max_length=5, null=True, blank=True)),
                ('part', models.CharField(max_length=30, null=True, blank=True)),
                ('portion', models.CharField(max_length=30, null=True, blank=True)),
                ('segment', models.CharField(max_length=30, null=True, blank=True)),
                ('bone_type', models.CharField(max_length=30, null=True, blank=True)),
            ],
            options={
                'verbose_name': 'FC Fauna',
                'managed': True,
                'verbose_name_plural': 'FC Fauna',
            },
            bases=('fc.context',),
        ),
        migrations.CreateModel(
            name='Galet_Weights',
            fields=[
                ('context_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='fc.Context')),
                ('weight', models.DecimalField(null=True, max_digits=10, decimal_places=2, blank=True)),
            ],
            options={
                'verbose_name': 'FC Galet Weight',
                'managed': True,
                'verbose_name_plural': 'FC Galet Weights',
            },
            bases=('fc.context',),
        ),
        migrations.CreateModel(
            name='Lithic',
            fields=[
                ('context_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='fc.Context')),
                ('dataclass', models.CharField(max_length=20)),
                ('raw_material', models.CharField(max_length=20, null=True, blank=True)),
                ('support', models.CharField(max_length=20, null=True, blank=True)),
                ('technique', models.CharField(max_length=20, null=True, blank=True)),
                ('form', models.CharField(max_length=20, null=True, blank=True)),
                ('fb_type', models.IntegerField(null=True, verbose_name=b'Bordes Type', blank=True)),
                ('fb_type_2', models.IntegerField(null=True, verbose_name=b'Bordes Type 2', blank=True)),
                ('core_type', models.CharField(max_length=20, null=True, blank=True)),
                ('biface_type', models.CharField(max_length=20, null=True, blank=True)),
                ('retouched_edges', models.IntegerField(null=True, blank=True)),
                ('retouch_intensity', models.CharField(max_length=20, null=True, blank=True)),
                ('tf_character', models.CharField(max_length=20, null=True, blank=True)),
                ('tf_surface', models.CharField(max_length=20, null=True, blank=True)),
                ('tf_location', models.CharField(max_length=20, null=True, blank=True)),
                ('platform_surface', models.CharField(max_length=20, null=True, blank=True)),
                ('platform_exterior', models.CharField(max_length=20, null=True, blank=True)),
                ('core_faces', models.IntegerField(null=True, blank=True)),
                ('platforms', models.CharField(max_length=20, null=True, blank=True)),
                ('platform_technique_1', models.CharField(max_length=20, null=True, blank=True)),
                ('platform_technique_2', models.CharField(max_length=20, null=True, blank=True)),
                ('scar_morphology', models.CharField(max_length=20, null=True, blank=True)),
                ('cortex', models.CharField(max_length=12, null=True, blank=True)),
                ('discard', models.CharField(max_length=20, null=True, blank=True)),
                ('edge_damage', models.CharField(max_length=20, null=True, blank=True)),
                ('alteration', models.CharField(max_length=20, null=True, blank=True)),
                ('proximal_removals', models.IntegerField(null=True, blank=True)),
                ('scar_length', models.DecimalField(null=True, max_digits=10, decimal_places=2, blank=True)),
                ('length', models.DecimalField(null=True, max_digits=10, decimal_places=2, blank=True)),
                ('width', models.DecimalField(null=True, max_digits=10, decimal_places=2, blank=True)),
                ('thickness', models.DecimalField(null=True, max_digits=10, decimal_places=2, blank=True)),
                ('platform_width', models.DecimalField(null=True, max_digits=10, decimal_places=2, blank=True)),
                ('platform_thickness', models.DecimalField(null=True, max_digits=10, decimal_places=2, blank=True)),
                ('small_pw', models.DecimalField(null=True, max_digits=10, decimal_places=2, blank=True)),
                ('bulb', models.DecimalField(null=True, max_digits=10, decimal_places=2, blank=True)),
                ('epa', models.IntegerField(null=True, blank=True)),
                ('weight', models.DecimalField(null=True, max_digits=10, decimal_places=2, blank=True)),
            ],
            options={
                'verbose_name': 'FC Lithic',
                'managed': True,
                'verbose_name_plural': 'FC Lithics',
            },
            bases=('fc.context',),
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('context_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='fc.Context')),
                ('image01', models.ImageField(upload_to=b'/media/', null=True, verbose_name=b'Image', blank=True)),
            ],
            options={
                'verbose_name': 'FC Image',
                'managed': True,
                'verbose_name_plural': 'FC Images',
            },
            bases=('fc.context',),
        ),
        migrations.CreateModel(
            name='Small_Find',
            fields=[
                ('context_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='fc.Context')),
                ('screen_size', models.CharField(max_length=20, null=True, blank=True)),
                ('platform_count', models.IntegerField(null=True, blank=True)),
                ('platform_weight', models.IntegerField(null=True, blank=True)),
            ],
            options={
                'verbose_name': 'FC Small find (bucket)',
                'managed': True,
                'verbose_name_plural': 'FC Small Finds (Summary Counts by bucket)',
            },
            bases=('fc.context',),
        ),
        migrations.AddField(
            model_name='small_find_weights',
            name='context',
            field=models.ForeignKey(to='fc.Context'),
        ),
        migrations.AddField(
            model_name='granulometry',
            name='context',
            field=models.ForeignKey(to='fc.Context'),
        ),
        migrations.CreateModel(
            name='Buckets_with_Grains',
            fields=[
            ],
            options={
                'verbose_name': 'FC Bucket with Granulometry',
                'managed': True,
                'proxy': True,
                'verbose_name_plural': 'FC Buckets with Granulometry',
            },
            bases=('fc.context',),
        ),
        migrations.CreateModel(
            name='Lithics_with_Photos',
            fields=[
            ],
            options={
                'verbose_name': 'FC Lithic (only with photo)',
                'managed': True,
                'proxy': True,
                'verbose_name_plural': 'FC Lithics (only with photos)',
            },
            bases=('fc.context',),
        ),
        migrations.CreateModel(
            name='Small_find_weights_summary',
            fields=[
            ],
            options={
                'verbose_name': 'FC Weights of small finds in a bucket',
                'managed': True,
                'proxy': True,
                'verbose_name_plural': 'FC Small Finds (Weights by bucket)',
            },
            bases=('fc.context',),
        ),
    ]
