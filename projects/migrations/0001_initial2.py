# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        # ('contenttypes', '0002_remove_content_type_name'),
        ('base', '0001_initial'),
        ('standard', '0001_initial'),
        ('projects', '0001_initial')
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectTerm',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('native', models.BooleanField(default=False, help_text=b'If true, this term is native to the project or standard, otherwise the term is being reused by the project or standard.')),
                ('mapping', models.CharField(help_text=b'If this term is being reused from another standard or project, the mapping field is used to provide the name of the field in this project or standard as opposed to the name in the project or standard from which it is being reused.', max_length=255, null=True, blank=True)),
                ('project', models.ForeignKey(to='projects.Project')),
                ('term', models.ForeignKey(to='standard.Term')),
            ],
            options={
                'db_table': 'projects_project_term',
                'verbose_name': 'Project Term',
                'verbose_name_plural': 'Project Terms',
            },
        ),
        migrations.AddField(
            model_name='project',
            name='terms',
            field=models.ManyToManyField(to='standard.Term', through='projects.ProjectTerm', blank=True),
        ),
        migrations.AddField(
            model_name='project',
            name='users',
            field=models.ManyToManyField(to='base.PaleocoreUser', blank=True),
        ),
        migrations.AlterUniqueTogether(
            name='projectterm',
            unique_together=set([('project', 'term')]),
        ),
    ]
