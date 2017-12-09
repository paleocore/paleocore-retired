# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hrp', '0019_auto_20160815_1926'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='archaeology',
            options={'verbose_name': 'HRP Archaeology', 'verbose_name_plural': 'HRP Archaeology'},
        ),
        migrations.AlterModelOptions(
            name='geology',
            options={'verbose_name': 'HRP Geology', 'verbose_name_plural': 'HRP Geology'},
        ),
        migrations.AddField(
            model_name='biology',
            name='deciduous',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='biology',
            name='indet_canine',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='biology',
            name='indet_incisor',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='biology',
            name='indet_molar',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='biology',
            name='indet_premolar',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='biology',
            name='indet_tooth',
            field=models.BooleanField(default=False),
        ),
    ]
