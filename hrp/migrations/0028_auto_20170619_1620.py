# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hrp', '0027_biology_element_remarks'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='occurrence',
            field=models.ForeignKey(related_name='files', to='hrp.Occurrence'),
        ),
        migrations.AlterField(
            model_name='image',
            name='occurrence',
            field=models.ForeignKey(related_name='images', to='hrp.Occurrence'),
        ),
    ]
