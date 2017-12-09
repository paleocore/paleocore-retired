# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hrp', '0018_archaeology_geology'),
    ]

    operations = [
        migrations.RenameField(
            model_name='biology',
            old_name='vertbatim_identification_qualifier',
            new_name='verbatim_identification_qualifier',
        ),
    ]
