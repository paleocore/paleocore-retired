# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hrp', '0028_auto_20170619_1620'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='biology',
            name='biology_remarks',
        ),
        migrations.AddField(
            model_name='biology',
            name='size_class',
            field=models.CharField(blank=True, max_length=50, null=True, choices=[(b'indeterminate', b'indeterminate'), (b'1', b'1'), (b'2', b'2'), (b'3', b'3'), (b'4', b'4'), (b'5', b'5')]),
        ),
        migrations.AlterField(
            model_name='biology',
            name='element',
            field=models.CharField(blank=True, max_length=50, null=True, choices=[(b'astragalus', b'astragalus'), (b'bacculum', b'bacculum'), (b'bone (indet.)', b'bone (indet.)'), (b'calcaneus', b'calcaneus'), (b'canine', b'canine'), (b'capitate', b'capitate'), (b'carapace', b'carapace'), (b'carpal (indet.)', b'carpal (indet.)'), (b'carpal/tarsal', b'carpal/tarsal'), (b'carpometacarpus', b'carpometacarpus'), (b'carpus', b'carpus'), (b'chela', b'chela'), (b'clavicle', b'clavicle'), (b'coccyx', b'coccyx'), (b'coprolite', b'coprolite'), (b'cranium', b'cranium'), (b'cranium w/horn core', b'cranium w/horn core'), (b'cuboid', b'cuboid'), (b'cubonavicular', b'cubonavicular'), (b'cuneiform', b'cuneiform'), (b'dermal plate', b'dermal plate'), (b'egg shell', b'egg shell'), (b'endocast', b'endocast'), (b'ethmoid', b'ethmoid'), (b'femur', b'femur'), (b'fibula', b'fibula'), (b'frontal', b'frontal'), (b'hamate', b'hamate'), (b'horn core', b'horn core'), (b'humerus', b'humerus'), (b'hyoid', b'hyoid'), (b'Ilium', b'Ilium'), (b'incisor', b'incisor'), (b'innominate', b'innominate'), (b'ischium', b'ischium'), (b'lacrimal', b'lacrimal'), (b'long bone ', b'long bone '), (b'lunate', b'lunate'), (b'mandible', b'mandible'), (b'manus', b'manus'), (b'maxilla', b'maxilla'), (b'metacarpal', b'metacarpal'), (b'metapodial', b'metapodial'), (b'metatarsal', b'metatarsal'), (b'molar', b'molar'), (b'nasal', b'nasal'), (b'navicular', b'navicular'), (b'naviculocuboid', b'naviculocuboid'), (b'occipital', b'occipital'), (b'ossicone', b'ossicone'), (b'parietal', b'parietal'), (b'patella', b'patella'), (b'pes', b'pes'), (b'phalanx', b'phalanx'), (b'pisiform', b'pisiform'), (b'plastron', b'plastron'), (b'premaxilla', b'premaxilla'), (b'premolar', b'premolar'), (b'pubis', b'pubis'), (b'radioulna', b'radioulna'), (b'radius', b'radius'), (b'rib', b'rib'), (b'sacrum', b'sacrum'), (b'scaphoid', b'scaphoid'), (b'scapholunar', b'scapholunar'), (b'scapula', b'scapula'), (b'scute', b'scute'), (b'sesamoid', b'sesamoid'), (b'shell', b'shell'), (b'skeleton', b'skeleton'), (b'skull', b'skull'), (b'sphenoid', b'sphenoid'), (b'sternum', b'sternum'), (b'talon', b'talon'), (b'talus', b'talus'), (b'tarsal (indet.)', b'tarsal (indet.)'), (b'tarsometatarsus', b'tarsometatarsus'), (b'tarsus', b'tarsus'), (b'temporal', b'temporal'), (b'tibia', b'tibia'), (b'tibiotarsus', b'tibiotarsus'), (b'tooth (indet.)', b'tooth (indet.)'), (b'trapezium', b'trapezium'), (b'trapezoid', b'trapezoid'), (b'triquetrum', b'triquetrum'), (b'ulna', b'ulna'), (b'vertebra', b'vertebra'), (b'vomer', b'vomer'), (b'zygomatic', b'zygomatic'), (b'pharyngeal teeth', b'pharyngeal teeth'), (b'molars', b'molars'), (b'tusk', b'tusk'), (b'horn corn', b'horn corn'), (b'spine', b'spine'), (b'silicified wood', b'silicified wood'), (b'dentary', b'dentary'), (b'cleithrum', b'cleithrum'), (b'skull plate', b'skull plate'), (b'basicranium', b'basicranium'), (b'angulararticular', b'angulararticular'), (b'ribs', b'ribs'), (b'lateral ethmoid', b'lateral ethmoid'), (b'pterotic', b'pterotic'), (b'tooth roots', b'tooth roots'), (b'shells', b'shells'), (b'pharyngeal tooth', b'pharyngeal tooth'), (b'ilium', b'ilium'), (b'hemimandible', b'hemimandible'), (b'pectoral spine', b'pectoral spine'), (b'palate', b'palate'), (b'pelvis', b'pelvis'), (b'long bone', b'long bone'), (b'axis', b'axis'), (b'acetabulum', b'acetabulum'), (b'magnum', b'magnum'), (b'hemi-mandible', b'hemi-mandible'), (b'weberian', b'weberian'), (b'supraoccipital', b'supraoccipital'), (b'anguloarticular', b'anguloarticular')]),
        ),
        migrations.AlterField(
            model_name='biology',
            name='element_modifier',
            field=models.CharField(blank=True, max_length=50, null=True, choices=[(b'articulated', b'articulated'), (b'caudal', b'caudal'), (b'cervical', b'cervical'), (b'coccygeal', b'coccygeal'), (b'distal', b'distal'), (b'intermediate', b'intermediate'), (b'lower', b'lower'), (b'lumbar', b'lumbar'), (b'manual', b'manual'), (b'manual distal', b'manual distal'), (b'manual intermediate', b'manual intermediate'), (b'manual proximal', b'manual proximal'), (b'medial', b'medial'), (b'pedal', b'pedal'), (b'pedal distal', b'pedal distal'), (b'pedal intermediate', b'pedal intermediate'), (b'pedal proximal', b'pedal proximal'), (b'proximal', b'proximal'), (b'sacral', b'sacral'), (b'thoracic', b'thoracic'), (b'upper', b'upper'), (b'indeterminate', b'indeterminate')]),
        ),
        migrations.AlterField(
            model_name='biology',
            name='element_number',
            field=models.CharField(blank=True, max_length=50, null=True, choices=[(b'1', b'1'), (b'2', b'2'), (b'3', b'3'), (b'3(medial)', b'3(medial)'), (b'4', b'4'), (b'4(lateral)', b'4(lateral)'), (b'5', b'5'), (b'6', b'6'), (b'7', b'7'), (b'8', b'8'), (b'9', b'9'), (b'10', b'10'), (b'11', b'11'), (b'12', b'12'), (b'13', b'13'), (b'14', b'14'), (b'15', b'15'), (b'16', b'16'), (b'17', b'17'), (b'2-7', b'2-7'), (b'8-12', b'8-12'), (b'indeterminate', b'indeterminate')]),
        ),
        migrations.AlterField(
            model_name='biology',
            name='element_portion',
            field=models.CharField(blank=True, max_length=50, null=True, choices=[(b'almost complete', b'almost complete'), (b'anterior', b'anterior'), (b'basal', b'basal'), (b'caudal', b'caudal'), (b'complete', b'complete'), (b'cranial', b'cranial'), (b'diaphysis', b'diaphysis'), (b'diaphysis+distal', b'diaphysis+distal'), (b'diaphysis+proximal', b'diaphysis+proximal'), (b'distal', b'distal'), (b'dorsal', b'dorsal'), (b'epiphysis', b'epiphysis'), (b'fragment', b'fragment'), (b'fragments', b'fragments'), (b'indeterminate', b'indeterminate'), (b'lateral', b'lateral'), (b'medial', b'medial'), (b'midsection', b'midsection'), (b'midsection+basal', b'midsection+basal'), (b'midsection+distal', b'midsection+distal'), (b'posterior', b'posterior'), (b'proximal', b'proximal'), (b'symphysis', b'symphysis'), (b'ventral', b'ventral')]),
        ),
        migrations.AlterField(
            model_name='biology',
            name='identified_by',
            field=models.CharField(blank=True, max_length=100, null=True, choices=[(b'Z. Alemseged', b'Z. Alemseged'), (b'R.L. Bernor', b'R.L. Bernor'), (b'R. Bobe-Quinteros', b'R. Bobe-Quinteros'), (b'P. Brodkorb', b'P. Brodkorb'), (b'H.B.S. Cooke', b'H.B.S. Cooke'), (b'E. Delson', b'E. Delson'), (b'C. Denys', b'C. Denys'), (b'G.G. Eck', b'G.G. Eck'), (b'V. Eisenmann', b'V. Eisenmann'), (b'N. Fessaha', b'N. Fessaha'), (b'L.J. Flynn', b'L.J. Flynn'), (b'S.R. Frost', b'S.R. Frost'), (b'A.W. Gentry', b'A.W. Gentry'), (b'D. Geraads', b'D. Geraads'), (b'R. Geze', b'R. Geze'), (b'F.C. Howell', b'F.C. Howell'), (b'Institute Staff', b'Institute Staff'), (b'D.C. Johanson', b'D.C. Johanson'), (b'W.H. Kimbel', b'W.H. Kimbel'), (b'H.B. Krentza', b'H.B. Krentza'), (b'B.M. Latimer', b'B.M. Latimer'), (b'M.E. Lewis', b'M.E. Lewis'), (b'C.A. Lockwood', b'C.A. Lockwood'), (b'T.K. Nalley', b'T.K. Nalley'), (b'G. Petter', b'G. Petter'), (b'J.C. Rage', b'J.C. Rage'), (b'D. Reed', b'D. Reed'), (b'K.E. Reed', b'K.E. Reed'), (b'J. Rowan', b'J. Rowan'), (b'M. Sabatier', b'M. Sabatier'), (b'B.J. Schoville', b'B.J. Schoville'), (b'A.E. Shapiro', b'A.E. Shapiro'), (b'G. Suwa', b'G. Suwa'), (b'E.S. Vrba', b'E.S. Vrba'), (b'L.A. Werdelin', b'L.A. Werdelin'), (b'H.B. Wesselman', b'H.B. Wesselman'), (b'T.D. White', b'T.D. White')]),
        ),
        migrations.AlterField(
            model_name='biology',
            name='life_stage',
            field=models.CharField(blank=True, max_length=50, null=True, choices=[(b'infant', b'infant'), (b'juvenile', b'juvenile')]),
        ),
        migrations.AlterField(
            model_name='occurrence',
            name='collection_remarks',
            field=models.TextField(max_length=255, null=True, verbose_name=b'Collection Remarks', blank=True),
        ),
        migrations.AlterField(
            model_name='occurrence',
            name='collector',
            field=models.CharField(blank=True, max_length=50, null=True, choices=[(b'C.J. Campisano', b'C.J. Campisano'), (b'W.H. Kimbel', b'W.H. Kimbel'), (b'T.K. Nalley', b'T.K. Nalley'), (b'D.N. Reed', b'D.N. Reed'), (b'K.E. Reed', b'K.E. Reed'), (b'B.J. Schoville', b'B.J. Schoville'), (b'A.E. Shapiro', b'A.E. Shapiro'), (b'HFS Student', b'HFS Student'), (b'HRP Team', b'HRP Team'), (b'Afar Team', b'Afar Team')]),
        ),
        migrations.AlterField(
            model_name='occurrence',
            name='finder',
            field=models.CharField(blank=True, max_length=50, null=True, choices=[(b'C.J. Campisano', b'C.J. Campisano'), (b'W.H. Kimbel', b'W.H. Kimbel'), (b'T.K. Nalley', b'T.K. Nalley'), (b'D.N. Reed', b'D.N. Reed'), (b'K.E. Reed', b'K.E. Reed'), (b'B.J. Schoville', b'B.J. Schoville'), (b'A.E. Shapiro', b'A.E. Shapiro'), (b'HFS Student', b'HFS Student'), (b'HRP Team', b'HRP Team'), (b'Afar Team', b'Afar Team')]),
        ),
    ]
