# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lgrp', '0004_occurrence_old_cat_number'),
    ]

    operations = [
        migrations.RenameField(
            model_name='occurrence',
            old_name='individual_count',
            new_name='item_count',
        ),
        migrations.RemoveField(
            model_name='occurrence',
            name='distance_from_found',
        ),
        migrations.RemoveField(
            model_name='occurrence',
            name='distance_from_likely',
        ),
        migrations.RemoveField(
            model_name='occurrence',
            name='distance_from_lower',
        ),
        migrations.RemoveField(
            model_name='occurrence',
            name='distance_from_upper',
        ),
        migrations.RemoveField(
            model_name='occurrence',
            name='related_catalog_items',
        ),
        migrations.RemoveField(
            model_name='occurrence',
            name='stratigraphic_marker_found',
        ),
        migrations.RemoveField(
            model_name='occurrence',
            name='stratigraphic_marker_likely',
        ),
        migrations.RemoveField(
            model_name='occurrence',
            name='stratigraphic_marker_lower',
        ),
        migrations.RemoveField(
            model_name='occurrence',
            name='stratigraphic_marker_upper',
        ),
        migrations.AlterField(
            model_name='file',
            name='file',
            field=models.FileField(null=True, upload_to=b'uploads/files/lgrp', blank=True),
        ),
        migrations.AlterField(
            model_name='file',
            name='occurrence',
            field=models.ForeignKey(related_name='files', to='lgrp.Occurrence'),
        ),
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(null=True, upload_to=b'uploads/images/lgrp', blank=True),
        ),
        migrations.AlterField(
            model_name='image',
            name='occurrence',
            field=models.ForeignKey(related_name='images', to='lgrp.Occurrence'),
        ),
        migrations.AlterField(
            model_name='occurrence',
            name='barcode',
            field=models.IntegerField(help_text=b'For collected items only.', null=True, verbose_name=b'Barcode', blank=True),
        ),
        migrations.AlterField(
            model_name='occurrence',
            name='basis_of_record',
            field=models.CharField(blank=True, help_text=b'e.g. Observed item or Collected item', max_length=50, verbose_name=b'Basis of Record', choices=[(b'Collection', b'Collection'), (b'Observation', b'Observation')]),
        ),
        migrations.AlterField(
            model_name='occurrence',
            name='collecting_method',
            field=models.CharField(blank=True, max_length=50, null=True, choices=[(b'Survey', b'Survey'), (b'Wet Screen', b'Wet Screen'), (b'Crawl Survey', b'Crawl Survey'), (b'Transect Survey', b'Transect Survey'), (b'Dry Screen', b'Dry Screen'), (b'Excavation', b'Excavation')]),
        ),
        migrations.AlterField(
            model_name='occurrence',
            name='collection_code',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name=b'Coll Code', choices=[(b'AA', b'AA'), (b'AM', b'AM'), (b'AM12', b'AM12'), (b'AS', b'AS'), (b'AT', b'AT'), (b'BD', b'BD'), (b'BG', b'BG'), (b'BR', b'BR'), (b'DK', b'DK'), (b'FD', b'FD'), (b'GR', b'GR'), (b'HD', b'HD'), (b'HS', b'HS'), (b'KG', b'KG'), (b'KL', b'KL'), (b'KT', b'KT'), (b'LD', b'LD'), (b'LG', b'LG'), (b'LN', b'LN'), (b'LS', b'LS'), (b'MF', b'MF'), (b'NL', b'NL'), (b'OI', b'OI'), (b'SS', b'SS')]),
        ),
        migrations.AlterField(
            model_name='occurrence',
            name='date_last_modified',
            field=models.DateTimeField(help_text=b'The date and time this resource was last altered.', verbose_name=b'Modified', auto_now=True),
        ),
        migrations.AlterField(
            model_name='occurrence',
            name='date_recorded',
            field=models.DateTimeField(help_text=b'Date and time the item was observed or collected.', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='occurrence',
            name='old_cat_number',
            field=models.CharField(max_length=255, null=True, verbose_name=b'Old Cat Number', blank=True),
        ),
        migrations.AlterField(
            model_name='occurrence',
            name='problem',
            field=models.BooleanField(default=False, help_text=b'Is there a problem with this record that needs attention?'),
        ),
        migrations.AlterField(
            model_name='occurrence',
            name='problem_comment',
            field=models.TextField(help_text=b'Description of the problem.', max_length=255, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='occurrence',
            name='remarks',
            field=models.TextField(help_text=b'General remarks about this database record.', max_length=500, null=True, verbose_name=b'Record Remarks', blank=True),
        ),
        migrations.AlterField(
            model_name='occurrence',
            name='stratigraphic_formation',
            field=models.CharField(max_length=255, null=True, verbose_name=b'Formation', blank=True),
        ),
        migrations.AlterField(
            model_name='occurrence',
            name='stratigraphic_member',
            field=models.CharField(max_length=255, null=True, verbose_name=b'Member', blank=True),
        ),
        migrations.AlterField(
            model_name='occurrence',
            name='year_collected',
            field=models.IntegerField(help_text=b'The year, event or field campaign during which the item was found.', null=True, blank=True),
        ),
    ]
