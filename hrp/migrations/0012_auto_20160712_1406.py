# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('hrp', '0011_auto_20160712_1346'),
    ]

    operations = [
        migrations.RenameField(
            model_name='locality',
            old_name='description_1',
            new_name='description',
        ),
        migrations.RemoveField(
            model_name='locality',
            name='description_2',
        ),
        migrations.RemoveField(
            model_name='locality',
            name='description_3',
        ),
        migrations.AddField(
            model_name='locality',
            name='date_last_modified',
            field=models.DateTimeField(default=datetime.datetime(2016, 7, 12, 14, 6, 19, 616304), verbose_name=b'Date Last Modified', auto_now=True),
            preserve_default=False,
        ),
    ]
