# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PaleocoreUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('institution', models.CharField(max_length=255, null=True, blank=True)),
                ('department', models.CharField(max_length=255, null=True, blank=True)),
                ('send_emails', models.BooleanField(default=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['user__last_name'],
                'db_table': 'paleocore_user',
                'verbose_name': 'User Info',
                'verbose_name_plural': 'User Info',
            },
        ),
    ]
