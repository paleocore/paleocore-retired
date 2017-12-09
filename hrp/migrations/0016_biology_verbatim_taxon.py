# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hrp', '0015_auto_20160809_1644'),
    ]

    operations = [
        migrations.AddField(
            model_name='biology',
            name='verbatim_taxon',
            field=models.CharField(max_length=1024, null=True, blank=True),
        ),
    ]
