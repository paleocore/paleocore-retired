# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hrp', '0006_auto_20160705_1836'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='occurrence',
            options={'ordering': ['collection_code', 'locality', 'item_number', 'item_part'], 'verbose_name': 'HRP Occurrence', 'verbose_name_plural': 'HRP Occurrences'},
        ),
        migrations.RenameField(
            model_name='occurrence',
            old_name='timestamp',
            new_name='date_recorded',
        ),
        migrations.AlterField(
            model_name='locality',
            name='collection_code',
            field=models.CharField(blank=True, max_length=10, null=True, choices=[(b'A.L.', b'A.L.')]),
        ),
        migrations.AlterField(
            model_name='occurrence',
            name='collecting_method',
            field=models.CharField(max_length=50, choices=[(b'Survey', b'Survey'), (b'dryscreen5mm', b'dryscreen5mm'), (b'wetscreen1mm', b'wetscreen1mm')]),
        ),
        migrations.AlterField(
            model_name='occurrence',
            name='collector',
            field=models.CharField(blank=True, max_length=50, null=True, choices=[(b'C.J. Campisano', b'C.J. Campisano'), (b'W.H. Kimbel', b'W.H. Kimbel'), (b'T.K. Nalley', b'T.K. Nalley'), (b'D.N. Reed', b'D.N. Reed'), (b'Kaye Reed', b'Kaye Reed'), (b'B.J. Schoville', b'B.J. Schoville'), (b'A.E. Shapiro', b'A.E. Shapiro'), (b'HFS Student', b'HFS Student'), (b'HRP Team', b'HRP Team')]),
        ),
    ]
