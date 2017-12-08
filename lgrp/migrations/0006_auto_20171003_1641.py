# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lgrp', '0005_auto_20170601_2359'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='biology',
            name='attributes',
        ),
        migrations.RemoveField(
            model_name='biology',
            name='morphobank_number',
        ),
        migrations.RemoveField(
            model_name='biology',
            name='preparations',
        ),
        migrations.AlterField(
            model_name='biology',
            name='element',
            field=models.CharField(blank=True, max_length=50, null=True, choices=[(b'astragalus', b'astragalus'), (b'bacculum', b'bacculum'), (b'bone (indet.)', b'bone (indet.)'), (b'calcaneus', b'calcaneus'), (b'canine', b'canine'), (b'capitate', b'capitate'), (b'carapace', b'carapace'), (b'carpal (indet.)', b'carpal (indet.)'), (b'carpal/tarsal', b'carpal/tarsal'), (b'carpometacarpus', b'carpometacarpus'), (b'carpus', b'carpus'), (b'chela', b'chela'), (b'clavicle', b'clavicle'), (b'coccyx', b'coccyx'), (b'coprolite', b'coprolite'), (b'cranium', b'cranium'), (b'cranium w/horn core', b'cranium w/horn core'), (b'cuboid', b'cuboid'), (b'cubonavicular', b'cubonavicular'), (b'cuneiform', b'cuneiform'), (b'dermal plate', b'dermal plate'), (b'egg shell', b'egg shell'), (b'endocast', b'endocast'), (b'ethmoid', b'ethmoid'), (b'femur', b'femur'), (b'fibula', b'fibula'), (b'frontal', b'frontal'), (b'hamate', b'hamate'), (b'horn core', b'horn core'), (b'humerus', b'humerus'), (b'hyoid', b'hyoid'), (b'Ilium', b'Ilium'), (b'incisor', b'incisor'), (b'innominate', b'innominate'), (b'ischium', b'ischium'), (b'lacrimal', b'lacrimal'), (b'long bone ', b'long bone '), (b'lunate', b'lunate'), (b'mandible', b'mandible'), (b'manus', b'manus'), (b'maxilla', b'maxilla'), (b'metacarpal', b'metacarpal'), (b'metapodial', b'metapodial'), (b'metatarsal', b'metatarsal'), (b'molar', b'molar'), (b'nasal', b'nasal'), (b'navicular', b'navicular'), (b'naviculocuboid', b'naviculocuboid'), (b'occipital', b'occipital'), (b'ossicone', b'ossicone'), (b'parietal', b'parietal'), (b'patella', b'patella'), (b'pes', b'pes'), (b'phalanx', b'phalanx'), (b'pisiform', b'pisiform'), (b'plastron', b'plastron'), (b'premaxilla', b'premaxilla'), (b'premolar', b'premolar'), (b'pubis', b'pubis'), (b'radioulna', b'radioulna'), (b'radius', b'radius'), (b'rib', b'rib'), (b'sacrum', b'sacrum'), (b'scaphoid', b'scaphoid'), (b'scapholunar', b'scapholunar'), (b'scapula', b'scapula'), (b'scute', b'scute'), (b'sesamoid', b'sesamoid'), (b'shell', b'shell'), (b'skeleton', b'skeleton'), (b'skull', b'skull'), (b'sphenoid', b'sphenoid'), (b'sternum', b'sternum'), (b'talon', b'talon'), (b'talus', b'talus'), (b'tarsal (indet.)', b'tarsal (indet.)'), (b'tarsometatarsus', b'tarsometatarsus'), (b'tarsus', b'tarsus'), (b'temporal', b'temporal'), (b'tibia', b'tibia'), (b'tibiotarsus', b'tibiotarsus'), (b'tooth (indet.)', b'tooth (indet.)'), (b'trapezium', b'trapezium'), (b'trapezoid', b'trapezoid'), (b'triquetrum', b'triquetrum'), (b'ulna', b'ulna'), (b'vertebra', b'vertebra'), (b'vomer', b'vomer'), (b'zygomatic', b'zygomatic'), (b'pharyngeal teeth', b'pharyngeal teeth'), (b'molars', b'molars'), (b'tusk', b'tusk'), (b'horn corn', b'horn corn'), (b'spine', b'spine'), (b'silicified wood', b'silicified wood'), (b'dentary', b'dentary'), (b'cleithrum', b'cleithrum'), (b'skull plate', b'skull plate'), (b'basicranium', b'basicranium'), (b'angulararticular', b'angulararticular'), (b'ribs', b'ribs'), (b'lateral ethmoid', b'lateral ethmoid'), (b'pterotic', b'pterotic'), (b'tooth roots', b'tooth roots'), (b'shells', b'shells'), (b'pharyngeal tooth', b'pharyngeal tooth'), (b'ilium', b'ilium'), (b'hemimandible', b'hemimandible'), (b'pectoral spine', b'pectoral spine'), (b'palate', b'palate'), (b'pelvis', b'pelvis'), (b'long bone', b'long bone'), (b'axis', b'axis'), (b'acetabulum', b'acetabulum'), (b'magnum', b'magnum'), (b'hemi-mandible', b'hemi-mandible'), (b'weberian', b'weberian'), (b'supraoccipital', b'supraoccipital'), (b'anguloarticular', b'anguloarticular')]),
        ),
        migrations.AlterField(
            model_name='biology',
            name='identified_by',
            field=models.CharField(blank=True, max_length=100, null=True, choices=[(b'I. Lazagabaster', b'I. Lazagabaster'), (b'K.E. Reed', b'K.E. Reed'), (b'C. Seyoum', b'C. Seyoum'), (b'B. Villamoare', b'B. Villamoare'), (b'J. Robinson', b'J. Robinson'), (b'I. Smail', b'I. Smail'), (b'L.A. Werdelin', b'L.A. Werdelin'), (b'E. Scott', b'E. Scott'), (b'J. Rowan', b'J. Rowan'), (b'W.H. Kimbel', b'W.H. Kimbel'), (b'J.A. Harris', b'J.A. Harris'), (b'E. Locke', b'E. Locke')]),
        ),
        migrations.AlterField(
            model_name='occurrence',
            name='collector',
            field=models.CharField(blank=True, max_length=50, null=True, choices=[(b'LGRP Team', b'LGRP Team'), (b'K.E. Reed', b'K.E. Reed'), (b'S. Oestmo', b'S. Oestmo'), (b'L. Werdelin', b'L. Werdelin'), (b'C.J. Campisano', b'C.J. Campisano'), (b'D.R. Braun', b'D.R. Braun'), (b'Tomas', b'Tomas'), (b'J. Rowan', b'J. Rowan'), (b'B. Villamoare', b'B. Villamoare'), (b'C. Seyoum', b'C. Seyoum'), (b'E. Scott', b'E. Scott'), (b'E. Locke', b'E. Locke'), (b'J. Harris', b'J. Harris'), (b'I. Lazagabaster', b'I. Lazagabaster'), (b'I. Smail', b'I. Smail'), (b'D. Garello', b'D. Garello'), (b'E.N. DiMaggio', b'E.N. DiMaggio'), (b'W.H. Kimbel', b'W.H. Kimbel'), (b'J. Robinson', b'J. Robinson'), (b'M. Bamford', b'M. Bamford'), (b'Zinash', b'Zinash'), (b'D.A. Feary', b'D.A. Feary'), (b'D. I. Garello', b'D. I. Garello')]),
        ),
        migrations.AlterField(
            model_name='occurrence',
            name='date_recorded',
            field=models.DateTimeField(help_text=b'Date and time the item was observed or collected.', null=True, verbose_name=b'Date Rec', blank=True),
        ),
        migrations.AlterField(
            model_name='occurrence',
            name='finder',
            field=models.CharField(blank=True, max_length=50, null=True, choices=[(b'LGRP Team', b'LGRP Team'), (b'K.E. Reed', b'K.E. Reed'), (b'S. Oestmo', b'S. Oestmo'), (b'L. Werdelin', b'L. Werdelin'), (b'C.J. Campisano', b'C.J. Campisano'), (b'D.R. Braun', b'D.R. Braun'), (b'Tomas', b'Tomas'), (b'J. Rowan', b'J. Rowan'), (b'B. Villamoare', b'B. Villamoare'), (b'C. Seyoum', b'C. Seyoum'), (b'E. Scott', b'E. Scott'), (b'E. Locke', b'E. Locke'), (b'J. Harris', b'J. Harris'), (b'I. Lazagabaster', b'I. Lazagabaster'), (b'I. Smail', b'I. Smail'), (b'D. Garello', b'D. Garello'), (b'E.N. DiMaggio', b'E.N. DiMaggio'), (b'W.H. Kimbel', b'W.H. Kimbel'), (b'J. Robinson', b'J. Robinson'), (b'M. Bamford', b'M. Bamford'), (b'Zinash', b'Zinash'), (b'D.A. Feary', b'D.A. Feary'), (b'D. I. Garello', b'D. I. Garello'), (b'Afar Team', b'Afar Team'), (b'ARCCH Rep', b'ARCCH Rep'), (b'J.R. Arrowsmith', b'J.R. Arrowsmith'), (b'TA', b'TA')]),
        ),
        migrations.AlterField(
            model_name='occurrence',
            name='item_type',
            field=models.CharField(blank=True, max_length=255, choices=[(b'Artifactual', b'Artifactual'), (b'Faunal', b'Faunal'), (b'Floral', b'Floral'), (b'Geological', b'Geological')]),
        ),
        migrations.AlterField(
            model_name='occurrence',
            name='year_collected',
            field=models.IntegerField(help_text=b'The year, event or field campaign during which the item was found.', null=True, verbose_name=b'Year', blank=True),
        ),
    ]
