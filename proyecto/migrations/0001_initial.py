# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ObserverSamples',
            fields=[
                ('obs_sample_id', models.CharField(max_length=50, serialize=False, primary_key=True, db_column='Obs Sample ID')),
                ('observer', models.CharField(max_length=100, null=True, db_column='Observer', blank=True)),
                ('date', models.DateTimeField(null=True, db_column='Date', blank=True)),
                ('time_record_created', models.DateTimeField(null=True, db_column='Time Record Created', blank=True)),
                ('comments', models.TextField(null=True, db_column='Comments', blank=True)),
                ('gps_used', models.CharField(max_length=25, null=True, db_column='GPS Used', blank=True)),
                ('os_rev_by_pi', models.NullBooleanField(db_column='OS Rev by PI')),
                ('os_rev_by_assistant', models.NullBooleanField(db_column='OS Rev by Assistant')),
            ],
            options={
                'db_table': 'observer samples',
                'managed': True,
            },
        ),
    ]
