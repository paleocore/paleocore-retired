# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('standard', '0002_term_is_class'),
    ]

    operations = [
        migrations.AddField(
            model_name='term',
            name='term_ordering',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
