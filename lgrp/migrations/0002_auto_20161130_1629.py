# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lgrp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='occurrence',
            old_name='analytical_unit',
            new_name='analytical_unit_1',
        ),
        migrations.AddField(
            model_name='biology',
            name='biology_remarks',
            field=models.TextField(max_length=500, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='biology',
            name='element_number',
            field=models.CharField(blank=True, max_length=50, null=True, choices=[(b'1', b'1'), (b'2', b'2'), (b'3', b'3'), (b'3(medial)', b'3(medial)'), (b'4', b'4'), (b'4(lateral)', b'4(lateral)'), (b'5', b'5'), (b'6', b'6'), (b'7', b'7'), (b'8', b'8'), (b'9', b'9'), (b'10', b'10'), (b'11', b'11'), (b'12', b'12'), (b'2-7', b'2-7'), (b'8-12', b'8-12'), (b'indeterminate', b'indeterminate')]),
        ),
        migrations.AddField(
            model_name='biology',
            name='element_portion',
            field=models.CharField(blank=True, max_length=50, null=True, choices=[(b'almost complete', b'almost complete'), (b'anterior', b'anterior'), (b'basal', b'basal'), (b'complete', b'complete'), (b'diaphysis', b'diaphysis'), (b'diaphysis+distal', b'diaphysis+distal'), (b'diaphysis+proximal', b'diaphysis+proximal'), (b'distal', b'distal'), (b'dorsal', b'dorsal'), (b'epiphysis', b'epiphysis'), (b'fragment', b'fragment'), (b'fragments', b'fragments'), (b'indeterminate', b'indeterminate'), (b'lateral', b'lateral'), (b'medial', b'medial'), (b'midsection', b'midsection'), (b'midsection+basal', b'midsection+basal'), (b'midsection+distal', b'midsection+distal'), (b'posterior', b'posterior'), (b'proximal', b'proximal'), (b'symphysis', b'symphysis'), (b'ventral', b'ventral')]),
        ),
        migrations.AddField(
            model_name='biology',
            name='element_remarks',
            field=models.TextField(max_length=500, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='biology',
            name='taxonomy_remarks',
            field=models.TextField(max_length=500, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='occurrence',
            name='geology_remarks',
            field=models.TextField(max_length=500, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='biology',
            name='element',
            field=models.CharField(blank=True, max_length=50, null=True, choices=[(b'astragalus', b'astragalus'), (b'bacculum', b'bacculum'), (b'bone (indet.)', b'bone (indet.)'), (b'calcaneus', b'calcaneus'), (b'canine', b'canine'), (b'capitate', b'capitate'), (b'carapace', b'carapace'), (b'carpal (indet.)', b'carpal (indet.)'), (b'carpal/tarsal', b'carpal/tarsal'), (b'carpometacarpus', b'carpometacarpus'), (b'carpus', b'carpus'), (b'chela', b'chela'), (b'clavicle', b'clavicle'), (b'coccyx', b'coccyx'), (b'coprolite', b'coprolite'), (b'cranium', b'cranium'), (b'cranium w/horn core', b'cranium w/horn core'), (b'cuboid', b'cuboid'), (b'cubonavicular', b'cubonavicular'), (b'cuneiform', b'cuneiform'), (b'dermal plate', b'dermal plate'), (b'egg shell', b'egg shell'), (b'endocast', b'endocast'), (b'ethmoid', b'ethmoid'), (b'femur', b'femur'), (b'fibula', b'fibula'), (b'frontal', b'frontal'), (b'hamate', b'hamate'), (b'horn core', b'horn core'), (b'humerus', b'humerus'), (b'hyoid', b'hyoid'), (b'Ilium', b'Ilium'), (b'incisor', b'incisor'), (b'innominate', b'innominate'), (b'ischium', b'ischium'), (b'lacrimal', b'lacrimal'), (b'long bone ', b'long bone '), (b'lunate', b'lunate'), (b'mandible', b'mandible'), (b'manus', b'manus'), (b'maxilla', b'maxilla'), (b'metacarpal', b'metacarpal'), (b'metapodial', b'metapodial'), (b'metatarsal', b'metatarsal'), (b'molar', b'molar'), (b'nasal', b'nasal'), (b'navicular', b'navicular'), (b'naviculocuboid', b'naviculocuboid'), (b'occipital', b'occipital'), (b'ossicone', b'ossicone'), (b'parietal', b'parietal'), (b'patella', b'patella'), (b'pes', b'pes'), (b'phalanx', b'phalanx'), (b'pisiform', b'pisiform'), (b'plastron', b'plastron'), (b'premaxilla', b'premaxilla'), (b'premolar', b'premolar'), (b'pubis', b'pubis'), (b'radioulna', b'radioulna'), (b'radius', b'radius'), (b'rib', b'rib'), (b'sacrum', b'sacrum'), (b'scaphoid', b'scaphoid'), (b'scapholunar', b'scapholunar'), (b'scapula', b'scapula'), (b'scute', b'scute'), (b'sesamoid', b'sesamoid'), (b'shell', b'shell'), (b'skeleton', b'skeleton'), (b'skull', b'skull'), (b'sphenoid', b'sphenoid'), (b'sternum', b'sternum'), (b'talon', b'talon'), (b'talus', b'talus'), (b'tarsal (indet.)', b'tarsal (indet.)'), (b'tarsometatarsus', b'tarsometatarsus'), (b'tarsus', b'tarsus'), (b'temporal', b'temporal'), (b'tibia', b'tibia'), (b'tibiotarsus', b'tibiotarsus'), (b'tooth (indet.)', b'tooth (indet.)'), (b'trapezium', b'trapezium'), (b'trapezoid', b'trapezoid'), (b'triquetrum', b'triquetrum'), (b'ulna', b'ulna'), (b'vertebra', b'vertebra'), (b'vomer', b'vomer'), (b'zygomatic', b'zygomatic')]),
        ),
        migrations.AlterField(
            model_name='biology',
            name='element_modifier',
            field=models.CharField(blank=True, max_length=50, null=True, choices=[(b'articulated', b'articulated'), (b'caudal', b'caudal'), (b'cervical', b'cervical'), (b'coccygeal', b'coccygeal'), (b'distal', b'distal'), (b'intermediate', b'intermediate'), (b'lower', b'lower'), (b'lumbar', b'lumbar'), (b'manual', b'manual'), (b'manual distal', b'manual distal'), (b'manual intermediate', b'manual intermediate'), (b'manual proximal', b'manual proximal'), (b'pedal', b'pedal'), (b'pedal distal', b'pedal distal'), (b'pedal intermediate', b'pedal intermediate'), (b'pedal proximal', b'pedal proximal'), (b'proximal', b'proximal'), (b'sacral', b'sacral'), (b'thoracic', b'thoracic'), (b'upper', b'upper'), (b'indeterminate', b'indeterminate')]),
        ),
        migrations.AlterField(
            model_name='biology',
            name='identified_by',
            field=models.CharField(blank=True, max_length=100, null=True, choices=[('D. Braun', 'D. Braun'), ('J. Thompson', 'J. Thompson'), ('E. Scott', 'E. Scott'), ('E. Locke', 'E. Locke'), ('A.E. Shapiro', 'A.E. Shapiro'), ('A.W. Gentry', 'A.W. Gentry'), ('B.J. Schoville', 'B.J. Schoville'), ('B.M. Latimer', 'B.M. Latimer'), ('C. Denys', 'C. Denys'), ('C.A. Lockwood', 'C.A. Lockwood'), ('D. Geraads', 'D. Geraads'), ('D.C. Johanson', 'D.C. Johanson'), ('E. Delson', 'E. Delson'), ('E.S. Vrba', 'E.S. Vrba'), ('F.C. Howell', 'F.C. Howell'), ('G. Petter', 'G. Petter'), ('G. Suwa', 'G. Suwa'), ('G.G. Eck', 'G.G. Eck'), ('H.B. Krentza', 'H.B. Krentza'), ('H.B. Wesselman', 'H.B. Wesselman'), ('H.B.S. Cooke', 'H.B.S. Cooke'), ('Institute Staff', 'Institute Staff'), ('J.C. Rage', 'J.C. Rage'), ('K.E. Reed', 'K.E. Reed'), ('L.A. Werdelin', 'L.A. Werdelin'), ('L.J. Flynn', 'L.J. Flynn'), ('M. Sabatier', 'M. Sabatier'), ('M.E. Lewis', 'M.E. Lewis'), ('N. Fessaha', 'N. Fessaha'), ('P. Brodkorb', 'P. Brodkorb'), ('R. Bobe-Quinteros', 'R. Bobe-Quinteros'), ('R. Geze', 'R. Geze'), ('R.L. Bernor', 'R.L. Bernor'), ('S.R. Frost', 'S.R. Frost'), ('T.D. White', 'T.D. White'), ('T.K. Nalley', 'T.K. Nalley'), ('V. Eisenmann', 'V. Eisenmann'), ('W.H. Kimbel', 'W.H. Kimbel'), ('Z. Alemseged', 'Z. Alemseged'), ('S. Oestmo', 'S. Oestmo'), ('J. Rowan', 'J. Rowan'), ('C.J. Campisano', 'C.J. Campisano'), ('J. Robinson', 'J. Robinson'), ('I. Smail', 'I. Smail'), ('I. Lazagabaster', 'I. Lazagabaster')]),
        ),
        migrations.AlterField(
            model_name='biology',
            name='side',
            field=models.CharField(blank=True, max_length=50, null=True, choices=[('L', 'L'), ('R', 'R'), ('Indeterminate', 'Indeterminate'), ('L+R', 'L+R')]),
        ),
        migrations.AlterField(
            model_name='occurrence',
            name='collection_remarks',
            field=models.TextField(max_length=500, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='occurrence',
            name='finder',
            field=models.CharField(blank=True, max_length=50, null=True, choices=[(b'Afar', b'Afar')]),
        ),
        migrations.AlterField(
            model_name='occurrence',
            name='georeference_remarks',
            field=models.TextField(max_length=500, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='occurrence',
            name='remarks',
            field=models.TextField(max_length=500, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='occurrence',
            name='weathering',
            field=models.SmallIntegerField(blank=True, null=True, choices=[(0, b'0 - unweathered'), (1, b'1 - parallel cracking'), (2, b'2 - flaking'), (3, b'3 - rough'), (4, b'4 - fibrous'), (5, b'5 - crumbling')]),
        ),
    ]
