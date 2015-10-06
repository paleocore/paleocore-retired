# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Turkana',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('museum', models.CharField(max_length=200, null=True, blank=True)),
                ('specimen_prefix', models.CharField(max_length=200, null=True, blank=True)),
                ('specimen_number', models.IntegerField(null=True, blank=True)),
                ('specimen_suffix', models.CharField(max_length=200, null=True, blank=True)),
                ('field_number', models.CharField(max_length=200, null=True, blank=True)),
                ('record_number', models.IntegerField(null=True, blank=True)),
                ('year_found', models.IntegerField(null=True, blank=True)),
                ('study_area', models.CharField(max_length=200, null=True, blank=True)),
                ('collecting_area', models.CharField(max_length=200, null=True, blank=True)),
                ('locality', models.CharField(max_length=200, null=True, blank=True)),
                ('air_photo', models.CharField(max_length=200, null=True, blank=True)),
                ('x_coordinate', models.DecimalField(null=True, max_digits=50, decimal_places=20, blank=True)),
                ('y_coordinate', models.DecimalField(null=True, max_digits=50, decimal_places=20, blank=True)),
                ('gps_datum', models.DecimalField(null=True, max_digits=50, decimal_places=20, blank=True)),
                ('latitude', models.DecimalField(null=True, max_digits=50, decimal_places=20, blank=True)),
                ('longitude', models.DecimalField(null=True, max_digits=50, decimal_places=20, blank=True)),
                ('formation', models.CharField(max_length=200, null=True, blank=True)),
                ('member', models.CharField(max_length=200, null=True, blank=True)),
                ('level', models.CharField(max_length=200, null=True, blank=True)),
                ('stratigraphic_unit', models.CharField(max_length=200, null=True, blank=True)),
                ('stratigraphic_code', models.CharField(max_length=200, null=True, blank=True)),
                ('excavation', models.CharField(max_length=200, null=True, blank=True)),
                ('square_number', models.CharField(max_length=200, null=True, blank=True)),
                ('age_estimate', models.IntegerField(null=True, blank=True)),
                ('age_max', models.IntegerField(null=True, blank=True)),
                ('age_min', models.IntegerField(null=True, blank=True)),
                ('matrix', models.CharField(max_length=200, null=True, blank=True)),
                ('weathering', models.CharField(max_length=200, null=True, blank=True)),
                ('surface', models.CharField(max_length=200, null=True, blank=True)),
                ('color', models.CharField(max_length=200, null=True, blank=True)),
                ('identifier', models.CharField(max_length=200, null=True, blank=True)),
                ('year_identified', models.IntegerField(null=True, blank=True)),
                ('publication_author', models.CharField(max_length=200, null=True, blank=True)),
                ('year_published', models.IntegerField(null=True, blank=True)),
                ('year_published_suffix', models.CharField(max_length=200, null=True, blank=True)),
                ('class_field', models.CharField(max_length=200, null=True, verbose_name=b'class', blank=True)),
                ('order', models.CharField(max_length=200, null=True, blank=True)),
                ('family', models.CharField(max_length=200, null=True, blank=True)),
                ('family_code', models.IntegerField(null=True, blank=True)),
                ('subfamily', models.CharField(max_length=200, null=True, blank=True)),
                ('tribe', models.CharField(max_length=200, null=True, blank=True)),
                ('tribe_code', models.IntegerField(null=True, blank=True)),
                ('genus_qualifier', models.CharField(max_length=200, null=True, blank=True)),
                ('genus', models.CharField(max_length=200, null=True, blank=True)),
                ('genus_code', models.IntegerField(null=True, blank=True)),
                ('species_qualifier', models.CharField(max_length=200, null=True, blank=True)),
                ('species', models.CharField(max_length=200, null=True, blank=True)),
                ('body_element', models.CharField(max_length=200, null=True, blank=True)),
                ('body_element_code', models.IntegerField(null=True, blank=True)),
                ('part_description', models.CharField(max_length=200, null=True, blank=True)),
                ('side', models.CharField(max_length=200, null=True, blank=True)),
                ('sex', models.CharField(max_length=200, null=True, blank=True)),
                ('age', models.IntegerField(null=True, blank=True)),
                ('body_size', models.CharField(max_length=200, null=True, blank=True)),
                ('remarks', models.CharField(max_length=500, null=True, blank=True)),
                ('date_entered', models.IntegerField(null=True, blank=True)),
                ('signed', models.CharField(max_length=200, null=True, blank=True)),
                ('storage_location', models.CharField(max_length=200, null=True, blank=True)),
                ('li1', models.CharField(max_length=1, null=True, blank=True)),
                ('li2', models.CharField(max_length=1, null=True, blank=True)),
                ('li3', models.CharField(max_length=1, null=True, blank=True)),
                ('lc', models.CharField(max_length=1, null=True, blank=True)),
                ('lp1', models.CharField(max_length=1, null=True, blank=True)),
                ('lp2', models.CharField(max_length=1, null=True, blank=True)),
                ('lp3', models.CharField(max_length=1, null=True, blank=True)),
                ('lp4', models.CharField(max_length=1, null=True, blank=True)),
                ('lm1', models.CharField(max_length=1, null=True, blank=True)),
                ('lm2', models.CharField(max_length=1, null=True, blank=True)),
                ('lm3', models.CharField(max_length=1, null=True, blank=True)),
                ('ui1', models.CharField(max_length=1, null=True, blank=True)),
                ('ui2', models.CharField(max_length=1, null=True, blank=True)),
                ('ui3', models.CharField(max_length=1, null=True, blank=True)),
                ('uc', models.CharField(max_length=1, null=True, blank=True)),
                ('up1', models.CharField(max_length=1, null=True, blank=True)),
                ('up2', models.CharField(max_length=1, null=True, blank=True)),
                ('up3', models.CharField(max_length=1, null=True, blank=True)),
                ('up4', models.CharField(max_length=1, null=True, blank=True)),
                ('um1', models.CharField(max_length=1, null=True, blank=True)),
                ('um2', models.CharField(max_length=1, null=True, blank=True)),
                ('um3', models.CharField(max_length=1, null=True, blank=True)),
                ('ldi1', models.CharField(max_length=1, null=True, blank=True)),
                ('ldi2', models.CharField(max_length=1, null=True, blank=True)),
                ('ldi3', models.CharField(max_length=1, null=True, blank=True)),
                ('ldc', models.CharField(max_length=1, null=True, blank=True)),
                ('ldp1', models.CharField(max_length=1, null=True, blank=True)),
                ('ldp2', models.CharField(max_length=1, null=True, blank=True)),
                ('ldp3', models.CharField(max_length=1, null=True, blank=True)),
                ('ldp4', models.CharField(max_length=1, null=True, blank=True)),
                ('udi1', models.CharField(max_length=1, null=True, blank=True)),
                ('udi2', models.CharField(max_length=1, null=True, blank=True)),
                ('udi3', models.CharField(max_length=1, null=True, blank=True)),
                ('udc', models.CharField(max_length=1, null=True, blank=True)),
                ('udp1', models.CharField(max_length=1, null=True, blank=True)),
                ('udp2', models.CharField(max_length=1, null=True, blank=True)),
                ('udp3', models.CharField(max_length=1, null=True, blank=True)),
                ('udp4', models.CharField(max_length=1, null=True, blank=True)),
                ('area_modifier', models.CharField(max_length=200, null=True, blank=True)),
            ],
            options={
                'ordering': ['formation', 'study_area', 'member'],
                'verbose_name_plural': 'Turkana Data',
            },
        ),
    ]
