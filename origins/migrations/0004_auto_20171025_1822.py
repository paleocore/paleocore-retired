# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import django.utils.datetime_safe
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('origins', '0003_auto_20171024_1738'),
    ]

    operations = [
        migrations.AddField(
            model_name='fossil',
            name='country',
            field=models.CharField(max_length=10, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='fossil',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 25, 18, 22, 22, 320203), verbose_name=b'Modified', auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='fossil',
            name='created_by',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='fossil',
            name='guid',
            field=models.URLField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='fossil',
            name='lifestage',
            field=models.CharField(max_length=20, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='fossil',
            name='locality',
            field=models.CharField(max_length=40, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='fossil',
            name='modified',
            field=models.DateTimeField(default=django.utils.datetime_safe.datetime.now, auto_now=True, help_text=b'The date and time this resource was last altered.', verbose_name=b'Modified'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='fossil',
            name='organism_id',
            field=models.CharField(max_length=40, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='fossil',
            name='sex',
            field=models.CharField(max_length=10, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='fossil',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4),
        ),
    ]
