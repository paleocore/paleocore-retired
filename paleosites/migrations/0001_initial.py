# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_countries.fields
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Date',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('layer', models.CharField(max_length=300, null=True, verbose_name=b'Layer', blank=True)),
                ('industry', models.CharField(max_length=100, null=True, verbose_name=b'Industry', blank=True)),
                ('industry_2', models.CharField(max_length=100, null=True, verbose_name=b'Industry', blank=True)),
                ('industry_3', models.CharField(max_length=100, null=True, verbose_name=b'Industry', blank=True)),
                ('cat_no', models.CharField(max_length=100, null=True, verbose_name=b'Catalog Number', blank=True)),
                ('date', models.FloatField(null=True, verbose_name=b'Age', blank=True)),
                ('sd_plus', models.FloatField(null=True, verbose_name=b'SD Plus', blank=True)),
                ('sd_minus', models.FloatField(null=True, verbose_name=b'SD Minus', blank=True)),
                ('sample', models.CharField(max_length=100, null=True, verbose_name=b'Sample', blank=True)),
                ('technique', models.CharField(max_length=100, null=True, verbose_name=b'Method', blank=True)),
                ('corrected_date_BP', models.FloatField(null=True, verbose_name=b'Cal. Age BP', blank=True)),
                ('plus', models.FloatField(null=True, verbose_name=b'Cal. Plus', blank=True)),
                ('minus', models.FloatField(null=True, verbose_name=b'Cal. Minus', blank=True)),
                ('hominid_remains', models.TextField(null=True, verbose_name=b'Hominins', blank=True)),
                ('bibliography', models.TextField(null=True, verbose_name=b'Bibliography', blank=True)),
                ('period', models.CharField(max_length=100, null=True, verbose_name=b'Period', blank=True)),
                ('notes', models.TextField(null=True, verbose_name=b'Notes', blank=True)),
                ('intcal09_max', models.FloatField(null=True, verbose_name=b'IntCal09 Max. Age', blank=True)),
                ('intcal09_min', models.FloatField(null=True, verbose_name=b'IntCal09 Min. Age', blank=True)),
            ],
            options={
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('site', models.CharField(max_length=255, null=True, verbose_name=b'Site name')),
                ('country', django_countries.fields.CountryField(blank=True, max_length=2, null=True, verbose_name=b'Country')),
                ('data_source', models.CharField(max_length=50, null=True, verbose_name=b'Data Source', blank=True)),
                ('altitude', models.FloatField(null=True, verbose_name=b'Altitude', blank=True)),
                ('site_type', models.CharField(blank=True, max_length=20, null=True, verbose_name=b'Site type', choices=[(b'Shelter', b'Shelter'), (b'Cave', b'Cave'), (b'Open-air', b'Open-air'), (b'Unknown', b'Unknown')])),
                ('display', models.NullBooleanField(verbose_name=b'Flagged')),
                ('map_location', django.contrib.gis.db.models.fields.PointField(srid=4326, null=True, blank=True)),
                ('notes', models.TextField(null=True, blank=True)),
            ],
            options={
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='date',
            name='site',
            field=models.ForeignKey(to='paleosites.Site'),
        ),
        migrations.CreateModel(
            name='Site_plus_dates',
            fields=[
            ],
            options={
                'verbose_name': 'Sites and dates',
                'managed': True,
                'proxy': True,
                'verbose_name_plural': 'Sites and dates',
            },
            bases=('paleosites.site',),
        ),
    ]
