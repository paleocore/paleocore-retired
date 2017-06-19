# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hrp', '0024_auto_20170619_1210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='biology',
            name='element',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='biology',
            name='element_modifier',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='occurrence',
            name='collector',
            field=models.CharField(blank=True, max_length=50, null=True, choices=[(b'C.J. Campisano', b'C.J. Campisano'), (b'W.H. Kimbel', b'W.H. Kimbel'), (b'T.K. Nalley', b'T.K. Nalley'), (b'D.N. Reed', b'D.N. Reed'), (b'K.E. Reed', b'K.E. Reed'), (b'B.J. Schoville', b'B.J. Schoville'), (b'A.E. Shapiro', b'A.E. Shapiro'), (b'HFS Student', b'HFS Student'), (b'HRP Team', b'HRP Team')]),
        ),
    ]
