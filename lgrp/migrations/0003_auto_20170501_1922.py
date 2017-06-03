# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lgrp', '0002_auto_20161130_1629'),
    ]

    operations = [
        migrations.AlterField(
            model_name='biology',
            name='identification_qualifier',
            field=models.ForeignKey(related_name='lgrp_id_qualifier_bio_occurrences', on_delete=django.db.models.deletion.SET_NULL, blank=True, to='taxonomy.IdentificationQualifier', null=True),
        ),
        migrations.AlterField(
            model_name='biology',
            name='qualifier_taxon',
            field=models.ForeignKey(related_name='lgrp_qualifier_taxon_bio_occurrences', on_delete=django.db.models.deletion.SET_NULL, blank=True, to='taxonomy.Taxon', null=True),
        ),
        migrations.AlterField(
            model_name='biology',
            name='taxon',
            field=models.ForeignKey(related_name='lgrp_taxon_bio_occurrences', on_delete=django.db.models.deletion.SET_DEFAULT, default=0, to='taxonomy.Taxon'),
        ),
        migrations.AlterField(
            model_name='occurrence',
            name='finder',
            field=models.CharField(blank=True, max_length=50, null=True, choices=[(b'LGRP Team', b'LGRP Team'), (b'K.E. Reed', b'K.E. Reed'), (b'S. Oestmo', b'S. Oestmo'), (b'L. Werdelin', b'L. Werdelin'), (b'C.J. Campisano', b'C.J. Campisano'), (b'D.R. Braun', b'D.R. Braun'), (b'Tomas', b'Tomas'), (b'J. Rowan', b'J. Rowan'), (b'B. Villamoare', b'B. Villamoare'), (b'C. Seyoum', b'C. Seyoum'), (b'E. Scott', b'E. Scott'), (b'E. Locke', b'E. Locke'), (b'J. Harris', b'J. Harris'), (b'I. Lazagabaster', b'I. Lazagabaster'), (b'I. Smail', b'I. Smail'), (b'D. Garello', b'D. Garello'), (b'E.N. DiMaggio', b'E.N. DiMaggio'), (b'W.H. Kimbel', b'W.H. Kimbel'), (b'J. Robinson', b'J. Robinson'), (b'M. Bamford', b'M. Bamford'), (b'Zinash', b'Zinash'), (b'D. Feary', b'D. Feary'), (b'D. I. Garello', b'D. I. Garello'), (b'Afar', b'Afar')]),
        ),
    ]
