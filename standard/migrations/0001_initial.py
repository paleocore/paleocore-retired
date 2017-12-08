# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '__first__'),
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('subject', models.CharField(max_length=100)),
                ('body', models.TextField()),
                ('timestamp', models.DateTimeField()),
                ('author', models.ForeignKey(to='base.PaleocoreUser')),
            ],
            options={
                'ordering': ['-timestamp'],
                'verbose_name': 'Comment',
                'verbose_name_plural': 'Comments',
            },
        ),
        migrations.CreateModel(
            name='Term',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('definition', models.TextField()),
                ('example', models.TextField(null=True, blank=True)),
                ('remarks', models.TextField(null=True, blank=True)),
                ('data_range', models.CharField(max_length=255, null=True, blank=True)),
                ('uses_controlled_vocabulary', models.BooleanField(default=False)),
                ('controlled_vocabulary', models.CharField(max_length=75, null=True, blank=True)),
                ('controlled_vocabulary_url', models.CharField(max_length=155, null=True, blank=True)),
                ('uri', models.CharField(max_length=255, null=True, blank=True)),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'Term',
                'verbose_name_plural': 'Terms',
            },
        ),
        migrations.CreateModel(
            name='TermCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=50)),
                ('uri', models.CharField(max_length=255, null=True, blank=True)),
                ('description', models.CharField(max_length=4000)),
                ('is_occurrence', models.BooleanField()),
                ('tree_visibility', models.BooleanField(default=True)),
                ('parent', models.ForeignKey(blank=True, to='standard.TermCategory', null=True)),
            ],
            options={
                'ordering': ['name'],
                'db_table': 'standard_term_category',
                'verbose_name': 'Term Category',
                'verbose_name_plural': 'Term Categories',
            },
        ),
        migrations.CreateModel(
            name='TermDataType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=50)),
                ('description', models.CharField(max_length=4000)),
            ],
            options={
                'ordering': ['name'],
                'db_table': 'standard_term_data_type',
                'verbose_name': 'Term Type',
                'verbose_name_plural': 'Term Types',
            },
        ),
        migrations.CreateModel(
            name='TermStatus',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=50)),
                ('description', models.CharField(max_length=4000)),
            ],
            options={
                'ordering': ['name'],
                'db_table': 'standard_term_status',
                'verbose_name': 'Term Status',
                'verbose_name_plural': 'Term Statuses',
            },
        ),
        migrations.AddField(
            model_name='term',
            name='category',
            field=models.ForeignKey(to='standard.TermCategory', null=True),
        ),
        migrations.AddField(
            model_name='term',
            name='data_type',
            field=models.ForeignKey(to='standard.TermDataType'),
        ),
        migrations.AddField(
            model_name='term',
            name='projects',
            field=models.ManyToManyField(to='projects.Project', through='projects.ProjectTerm', blank=True),
        ),
        migrations.AddField(
            model_name='term',
            name='status',
            field=models.ForeignKey(to='standard.TermStatus'),
        ),
        migrations.AddField(
            model_name='comment',
            name='term',
            field=models.ForeignKey(to='standard.Term'),
        ),
    ]
