# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('origins', '0005_auto_20171025_1829'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(upload_to=b'uploads/images/origins', null=True, verbose_name=b'Image', blank=True)),
                ('fossil', models.ForeignKey(to='origins.Fossil', null=True)),
            ],
            options={
                'verbose_name': 'Image',
                'managed': True,
                'verbose_name_plural': 'Images',
            },
        ),
    ]
