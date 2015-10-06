# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('standard', '0001_initial'),
        ('projects', '0001_initial2'),
        #('base', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='term',
            name='projects',
            field=models.ManyToManyField(to='projects.Project', through='projects.ProjectTerm', blank=True),
        ),
    ]
