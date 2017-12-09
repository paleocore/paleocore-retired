# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hrp', '0017_auto_20160812_2008'),
    ]

    operations = [
        migrations.CreateModel(
            name='Archaeology',
            fields=[
                ('occurrence_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='hrp.Occurrence')),
                ('find_type', models.CharField(max_length=255, null=True, blank=True)),
                ('length_mm', models.DecimalField(null=True, max_digits=38, decimal_places=8, blank=True)),
                ('width_mm', models.DecimalField(null=True, max_digits=38, decimal_places=8, blank=True)),
            ],
            bases=('hrp.occurrence',),
        ),
        migrations.CreateModel(
            name='Geology',
            fields=[
                ('occurrence_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='hrp.Occurrence')),
                ('find_type', models.CharField(max_length=255, null=True, blank=True)),
                ('dip', models.DecimalField(null=True, max_digits=38, decimal_places=8, blank=True)),
                ('strike', models.DecimalField(null=True, max_digits=38, decimal_places=8, blank=True)),
                ('color', models.CharField(max_length=255, null=True, blank=True)),
                ('texture', models.CharField(max_length=255, null=True, blank=True)),
            ],
            bases=('hrp.occurrence',),
        ),
    ]
