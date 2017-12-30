# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lgrp', '0008_auto_20171108_1833'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, null=True, blank=True)),
            ],
            options={
                'verbose_name': 'LGRP Person',
                'verbose_name_plural': 'LGRP People',
            },
        ),
        migrations.AddField(
            model_name='occurrence',
            name='collector_person',
            field=models.ForeignKey(related_name='person_collector', on_delete=django.db.models.deletion.SET_NULL,
                                    blank=True, to='lgrp.Person', null=True),
        ),
        migrations.AddField(
            model_name='occurrence',
            name='finder_person',
            field=models.ForeignKey(related_name='person_finder', on_delete=django.db.models.deletion.SET_NULL,
                                    blank=True, to='lgrp.Person', null=True),
        ),
    ]
