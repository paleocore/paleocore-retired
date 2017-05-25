# -*- coding: utf-8 -*-


from django.db import models, migrations
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Occurrence',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('global_id', models.IntegerField(null=True, blank=True)),
                ('reference', models.CharField(max_length=255, null=True, verbose_name=b'Reference', blank=True)),
                ('basis_of_record', models.CharField(blank=True, max_length=255, verbose_name=b'Basis of Record', choices=[(b'FossilSpecimen', b'Fossil'), (b'HumanObservation', b'Observation')])),
                ('item_type', models.CharField(blank=True, max_length=255, null=True, verbose_name=b'Item Type', choices=[(b'Artifactual', b'Artifactual'), (b'Faunal', b'Faunal'), (b'Floral', b'Floral'), (b'Geological', b'Geological')])),
                ('collection_code', models.CharField(default=b'MLP', max_length=255, null=True, verbose_name=b'Collection Code', blank=True)),
                ('institution_code', models.CharField(max_length=255, null=True, verbose_name=b'Institution Code', blank=True)),
                ('item_number', models.IntegerField(null=True, verbose_name=b'Item #', blank=True)),
                ('item_part', models.CharField(max_length=255, null=True, verbose_name=b'Item Part', blank=True)),
                ('catalog_number', models.CharField(max_length=255, null=True, verbose_name=b'Catalog #', blank=True)),
                ('paleo_locality', models.CharField(max_length=255, null=True, verbose_name=b'Paleo Locality', blank=True)),
                ('paleo_locality_number', models.IntegerField(null=True, verbose_name=b'Paleo Locality Number', blank=True)),
                ('sampling_protocol', models.CharField(max_length=255, null=True, verbose_name=b'Sampling Protocol', blank=True)),
                ('occurrence_remarks', models.TextField(max_length=255, null=True, verbose_name=b'Occurrence Remarks', blank=True)),
                ('item_scientific_name', models.CharField(max_length=255, null=True, verbose_name=b'Sci Name', blank=True)),
                ('item_description', models.CharField(max_length=255, null=True, verbose_name=b'Item Description', blank=True)),
                ('continent', models.CharField(max_length=255, null=True, verbose_name=b'Continent', blank=True)),
                ('country', models.CharField(max_length=255, null=True, verbose_name=b'Country', blank=True)),
                ('state_province', models.CharField(max_length=255, null=True, verbose_name=b'State or Province', blank=True)),
                ('locality', models.CharField(max_length=255, null=True, verbose_name=b'Locality', blank=True)),
                ('verbatim_locality', models.CharField(max_length=255, null=True, verbose_name=b'Verbatim Locality', blank=True)),
                ('location_remarks', models.CharField(max_length=255, null=True, verbose_name=b'Location Remarks', blank=True)),
                ('verbatim_coordinates', models.CharField(max_length=255, null=True, verbose_name=b'Verbatim Coordinates', blank=True)),
                ('verbatim_coordinate_system', models.CharField(max_length=255, null=True, verbose_name=b'Verbatim Coordinate System', blank=True)),
                ('decimal_longitude', models.DecimalField(null=True, verbose_name=b'Longitude', max_digits=38, decimal_places=8, blank=True)),
                ('decimal_latitude', models.DecimalField(null=True, verbose_name=b'Latitude', max_digits=38, decimal_places=8, blank=True)),
                ('geodetic_datum', models.CharField(max_length=255, null=True, verbose_name=b'Geodetic Datum', blank=True)),
                ('coordinate_uncertainty_in_meters', models.IntegerField(null=True, verbose_name=b'Coordinate Uncertainty', blank=True)),
                ('georeference_remarks', models.CharField(max_length=255, null=True, verbose_name=b'Georeferencing Remarks', blank=True)),
                ('collecting_method', models.CharField(blank=True, max_length=255, null=True, verbose_name=b'Collecting Method', choices=[(b'Surface Standard', b'Surface Standard'), (b'Surface Intensive', b'Surface Intensive'), (b'Surface Complete', b'Surface Complete'), (b'Exploratory Survey', b'Exploratory Survey'), (b'Dry Screen 5mm', b'Dry Screen 5mm'), (b'Dry Screen 2mm', b'Dry Screen 2mm'), (b'Wet Screen 1mm', b'Wet Screen 1mm')])),
                ('related_catalog_items', models.CharField(max_length=255, null=True, verbose_name=b'Related Catalog Items', blank=True)),
                ('collector', models.CharField(blank=True, max_length=255, null=True, choices=[(b'Zeresenay Alemseged', b'Zeresenay Alemseged'), (b'Rene Bobe', b'Rene Bobe'), (b'Denis Geraads', b'Denis Geraads'), (b'Shannon McPherron', b'Shannon McPherron'), (b'Denne Reed', b'Denne Reed'), (b'Jonathan Wynn', b'Jonathan Wynn')])),
                ('found_by', models.CharField(max_length=255, null=True, verbose_name=b'Found By', blank=True)),
                ('event_date', models.DateField(null=True, verbose_name=b'Date', blank=True)),
                ('event_year', models.IntegerField(null=True, verbose_name=b'Year', blank=True)),
                ('event_month', models.CharField(max_length=255, null=True, verbose_name=b'Month', blank=True)),
                ('event_day', models.CharField(max_length=255, null=True, verbose_name=b'Day', blank=True)),
                ('event_remarks', models.CharField(max_length=255, null=True, verbose_name=b'Event Remarks', blank=True)),
                ('stratigraphic_marker_upper', models.CharField(max_length=255, null=True, verbose_name=b'Stratigraphic Marker Upper', blank=True)),
                ('distance_from_upper', models.DecimalField(null=True, verbose_name=b'Distance From Upper', max_digits=38, decimal_places=8, blank=True)),
                ('stratigraphic_marker_lower', models.CharField(max_length=255, null=True, verbose_name=b'Stratigraphic Marker Lower', blank=True)),
                ('distance_from_lower', models.DecimalField(null=True, verbose_name=b'Distance From Lower', max_digits=38, decimal_places=8, blank=True)),
                ('stratigraphic_group', models.CharField(max_length=255, null=True, verbose_name=b'Stratigraphic Group', blank=True)),
                ('stratigraphic_formation', models.CharField(max_length=255, null=True, verbose_name=b'Stratigraphic Formation', blank=True)),
                ('stratigraphic_member', models.CharField(max_length=255, null=True, verbose_name=b'Stratigraphic Member', blank=True)),
                ('stratigraphic_bed', models.CharField(max_length=255, null=True, verbose_name=b'Stratigraphic Bed', blank=True)),
                ('geochronological_age', models.IntegerField(null=True, verbose_name=b'Geochronological Age', blank=True)),
                ('image', models.FileField(max_length=255, null=True, upload_to=b'uploads/images/san_francisco', blank=True)),
                ('geom', django.contrib.gis.db.models.fields.GeometryField(srid=4326, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='PaleoSite',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('setting', models.CharField(blank=True, max_length=255, null=True, choices=[(b'open-air', b'open-air'), (b'cave', b'cave'), (b'rockshelter', b'rockshelter')])),
                ('continent', models.CharField(blank=True, max_length=255, null=True, choices=[(b'Africa', b'Africa'), (b'Europe', b'Europe'), (b'Asia', b'Asia'), (b'North America', b'North America'), (b'South America', b'South America'), (b'Australia', b'Australia'), (b'Antarctica', b'Antarctica')])),
                ('country', models.CharField(blank=True, max_length=255, null=True, choices=[(b'United States of America', b'United States of America'), (b'Afghanistan', b'Afghanistan'), (b'Aland Islands', b'Aland Islands'), (b'Albania', b'Albania'), (b'Algeria', b'Algeria'), (b'American Samoa', b'American Samoa'), (b'Andorra', b'Andorra'), (b'Angola', b'Angola'), (b'Anguilla', b'Anguilla'), (b'Antigua and Barbuda', b'Antigua and Barbuda'), (b'Argentina', b'Argentina'), (b'Armenia', b'Armenia'), (b'Aruba', b'Aruba'), (b'Australia', b'Australia'), (b'Austria', b'Austria'), (b'Azerbaijan', b'Azerbaijan'), (b'Bahamas', b'Bahamas'), (b'Bahrain', b'Bahrain'), (b'Bangladesh', b'Bangladesh'), (b'Barbados', b'Barbados'), (b'Belarus', b'Belarus'), (b'Belgium', b'Belgium'), (b'Belize', b'Belize'), (b'Benin', b'Benin'), (b'Bermuda', b'Bermuda'), (b'Bhutan', b'Bhutan'), (b'Bolivia', b'Bolivia'), (b'Bosnia and Herzegovina', b'Bosnia and Herzegovina'), (b'Botswana', b'Botswana'), (b'Brazil', b'Brazil'), (b'British Virgin Islands', b'British Virgin Islands'), (b'Brunei Darussalam', b'Brunei Darussalam'), (b'Bulgaria', b'Bulgaria'), (b'Burkina Faso', b'Burkina Faso'), (b'Burundi', b'Burundi'), (b'Cambodia', b'Cambodia'), (b'Cameroon', b'Cameroon'), (b'Canada', b'Canada'), (b'Cape Verde', b'Cape Verde'), (b'Cayman Islands', b'Cayman Islands'), (b'Central African Republic', b'Central African Republic'), (b'Chad', b'Chad'), (b'Channel Islands', b'Channel Islands'), (b'Chile', b'Chile'), (b'China', b'China'), (b'China - Hong Kong', b'China - Hong Kong'), (b'China - Macao', b'China - Macao'), (b'Colombia', b'Colombia'), (b'Comoros', b'Comoros'), (b'Congo', b'Congo'), (b'Cook Islands', b'Cook Islands'), (b'Costa Rica', b'Costa Rica'), (b"Cote d'Ivoire", b"Cote d'Ivoire"), (b'Croatia', b'Croatia'), (b'Cuba', b'Cuba'), (b'Cyprus', b'Cyprus'), (b'Czech Republic', b'Czech Republic'), (b"Democratic People's Republic of Korea", b"Democratic People's Republic of Korea"), (b'Democratic Republic of the Congo', b'Democratic Republic of the Congo'), (b'Denmark', b'Denmark'), (b'Djibouti', b'Djibouti'), (b'Dominica', b'Dominica'), (b'Dominican Republic', b'Dominican Republic'), (b'Ecuador', b'Ecuador'), (b'Egypt', b'Egypt'), (b'El Salvador', b'El Salvador'), (b'Equatorial Guinea', b'Equatorial Guinea'), (b'Eritrea', b'Eritrea'), (b'Estonia', b'Estonia'), (b'Ethiopia', b'Ethiopia'), (b'Faeroe Islands', b'Faeroe Islands'), (b'Falkland Islands (Malvinas)', b'Falkland Islands (Malvinas)'), (b'Fiji', b'Fiji'), (b'Finland', b'Finland'), (b'France', b'France'), (b'French Guiana', b'French Guiana'), (b'French Polynesia', b'French Polynesia'), (b'Gabon', b'Gabon'), (b'Gambia', b'Gambia'), (b'Georgia', b'Georgia'), (b'Germany', b'Germany'), (b'Ghana', b'Ghana'), (b'Gibraltar', b'Gibraltar'), (b'Greece', b'Greece'), (b'Greenland', b'Greenland'), (b'Grenada', b'Grenada'), (b'Guadeloupe', b'Guadeloupe'), (b'Guam', b'Guam'), (b'Guatemala', b'Guatemala'), (b'Guernsey', b'Guernsey'), (b'Guinea', b'Guinea'), (b'Guinea-Bissau', b'Guinea-Bissau'), (b'Guyana', b'Guyana'), (b'Haiti', b'Haiti'), (b'Holy See (Vatican City)', b'Holy See (Vatican City)'), (b'Honduras', b'Honduras'), (b'Hungary', b'Hungary'), (b'Iceland', b'Iceland'), (b'India', b'India'), (b'Indonesia', b'Indonesia'), (b'Iran', b'Iran'), (b'Iraq', b'Iraq'), (b'Ireland', b'Ireland'), (b'Isle of Man', b'Isle of Man'), (b'Israel', b'Israel'), (b'Italy', b'Italy'), (b'Jamaica', b'Jamaica'), (b'Japan', b'Japan'), (b'Jersey', b'Jersey'), (b'Jordan', b'Jordan'), (b'Kazakhstan', b'Kazakhstan'), (b'Kenya', b'Kenya'), (b'Kiribati', b'Kiribati'), (b'Kuwait', b'Kuwait'), (b'Kyrgyzstan', b'Kyrgyzstan'), (b"Lao People's Democratic Republic", b"Lao People's Democratic Republic"), (b'Latvia', b'Latvia'), (b'Lebanon', b'Lebanon'), (b'Lesotho', b'Lesotho'), (b'Liberia', b'Liberia'), (b'Libyan Arab Jamahiriya', b'Libyan Arab Jamahiriya'), (b'Liechtenstein', b'Liechtenstein'), (b'Lithuania', b'Lithuania'), (b'Luxembourg', b'Luxembourg'), (b'Macedonia', b'Macedonia'), (b'Madagascar', b'Madagascar'), (b'Malawi', b'Malawi'), (b'Malaysia', b'Malaysia'), (b'Maldives', b'Maldives'), (b'Mali', b'Mali'), (b'Malta', b'Malta'), (b'Marshall Islands', b'Marshall Islands'), (b'Martinique', b'Martinique'), (b'Mauritania', b'Mauritania'), (b'Mauritius', b'Mauritius'), (b'Mayotte', b'Mayotte'), (b'Mexico', b'Mayotte'), (b'Micronesia, Federated States of', b'Micronesia, Federated States of'), (b'Monaco', b'Monaco'), (b'Mongolia', b'Mongolia'), (b'Montenegro', b'Montenegro'), (b'Montserrat', b'Montserrat'), (b'Morocco', b'Morocco'), (b'Mozambique', b'Mozambique'), (b'Myanmar', b'Myanmar'), (b'Namibia', b'Namibia'), (b'Nauru', b'Nauru'), (b'Nepal', b'Nepal'), (b'Netherlands', b'Netherlands'), (b'Netherlands Antilles', b'Netherlands Antilles'), (b'New Caledonia', b'New Caledonia'), (b'New Zealand', b'New Zealand'), (b'Nicaragua', b'Nicaragua'), (b'Niger', b'Niger'), (b'Nigeria', b'Nigeria'), (b'Niue', b'Niue'), (b'Norfolk Island', b'Norfolk Island'), (b'Northern Mariana Islands', b'Northern Mariana Islands'), (b'Norway', b'Norway'), (b'Occupied Palestinian Territory', b'Occupied Palestinian Territory'), (b'Oman', b'Oman'), (b'Pakistan', b'Pakistan'), (b'Palau', b'Palau'), (b'Panama', b'Panama'), (b'Papua New Guinea', b'Papua New Guinea'), (b'Paraguay', b'Paraguay'), (b'Peru', b'Peru'), (b'Philippines', b'Philippines'), (b'Pitcairn', b'Pitcairn'), (b'Poland', b'Poland'), (b'Portugal', b'Portugal'), (b'Puerto Rico', b'Puerto Rico'), (b'Qatar', b'Qatar'), (b'Republic of Korea', b'Republic of Korea'), (b'Republic of Moldova', b'Republic of Moldova'), (b'Reunion', b'Reunion'), (b'Romania', b'Romania'), (b'Russian Federation', b'Russian Federation'), (b'Rwanda', b'Rwanda'), (b'Saint-Barthelemy', b'Saint-Barthelemy'), (b'Saint Helena', b'Saint Helena'), (b'Saint Kitts and Nevis', b'Saint Kitts and Nevis'), (b'Saint Lucia', b'Saint Lucia'), (b'Saint-Martin (French part)', b'Saint-Martin (French part)'), (b'Saint Pierre and Miquelon', b'Saint Pierre and Miquelon'), (b'Saint Vincent and the Grenadines', b'Saint Vincent and the Grenadines'), (b'Samoa', b'Samoa'), (b'San Marino', b'San Marino'), (b'Sao Tome and Principe', b'Sao Tome and Principe'), (b'Saudi Arabia', b'Saudi Arabia'), (b'Senegal', b'Senegal'), (b'Serbia', b'Serbia'), (b'Seychelles', b'Seychelles'), (b'Sierra Leone', b'Sierra Leone'), (b'Singapore', b'Singapore'), (b'Slovakia', b'Slovakia'), (b'Slovenia', b'Slovenia'), (b'Solomon Islands', b'Solomon Islands'), (b'Somalia', b'Somalia'), (b'South Africa', b'South Africa'), (b'Spain', b'Spain'), (b'Sri Lanka', b'Sri Lanka'), (b'Sudan', b'Sudan'), (b'Suriname', b'Suriname'), (b'Svalbard and Jan Mayen Islands', b'Svalbard and Jan Mayen Islands'), (b'Swaziland', b'Swaziland'), (b'Sweden', b'Sweden'), (b'Switzerland', b'Switzerland'), (b'Syrian Arab Republic', b'Syrian Arab Republic'), (b'Tajikistan', b'Tajikistan'), (b'Thailand', b'Thailand'), (b'Timor-Leste', b'Timor-Leste'), (b'Togo', b'Togo'), (b'Tokelau', b'Tokelau'), (b'Tonga', b'Tonga'), (b'Trinidad and Tobago', b'Trinidad and Tobago'), (b'Tunisia', b'Tunisia'), (b'Turkey', b'Turkey'), (b'Turkmenistan', b'Turkmenistan'), (b'Turks and Caicos Islands', b'Turks and Caicos Islands'), (b'Tuvalu', b'Tuvalu'), (b'Uganda', b'Uganda'), (b'Ukraine', b'Ukraine'), (b'United Arab Emirates', b'United Arab Emirates'), (b'United Kingdom', b'United Kingdom'), (b'United Republic of Tanzania', b'United Republic of Tanzania'), (b'United States of America', b'United States of America'), (b'United States Virgin Islands', b'United States Virgin Islands'), (b'Uruguay', b'Uruguay'), (b'Uzbekistan', b'Uzbekistan'), (b'Vanuatu', b'Vanuatu'), (b'Venezuela (Bolivarian Republic of)', b'Venezuela (Bolivarian Republic of)'), (b'Viet Nam', b'Viet Nam'), (b'Wallis and Futuna Islands', b'Wallis and Futuna Islands'), (b'Western Sahara', b'Western Sahara'), (b'Yemen', b'Yemen'), (b'Zambia', b'Zambia'), (b'Zimbabwe', b'Zimbabwe')])),
                ('region', models.CharField(blank=True, max_length=255, null=True, choices=[(b'southern_africa', b'southern Africa'), (b'eastern_africa', b'eastern Africa'), (b'northern_africa', b'northern Africa'), (b'', b''), (b'', b'')])),
                ('research_project', models.CharField(max_length=255, null=True, blank=True)),
                ('collection_code', models.CharField(max_length=20, null=True, blank=True)),
                ('geological_member', models.CharField(max_length=255, null=True, blank=True)),
                ('cultural_term', models.CharField(max_length=255, null=True, blank=True)),
                ('technology_period', models.CharField(max_length=255, null=True, blank=True)),
                ('start_date', models.CharField(max_length=255, null=True, blank=True)),
                ('end_date', models.CharField(max_length=255, null=True, blank=True)),
                ('geological_epoch', models.CharField(blank=True, max_length=255, null=True, choices=[(b'Pliocene', b'Pliocene'), (b'Pleistocene', b'Pleistocene'), (b'Holocene', b'Holocene')])),
                ('date_description', models.CharField(max_length=255, null=True, blank=True)),
                ('material', models.CharField(blank=True, max_length=255, null=True, choices=[(b'basketry', b'basketry'), (b'building material', b'building material'), (b'ceramic', b'ceramic'), (b'chipped stone', b'chipped stone'), (b'dating sample', b'dating sample'), (b'fauna', b'fauna'), (b'fire-cracked rock', b'fire-cracked rock'), (b'glass', b'glass'), (b'ground stone', b'ground stone'), (b'hide', b'hide'), (b'human remains', b'human remains'), (b'macrobotanical', b'macrobotanical'), (b'metal', b'metal'), (b'mineral', b'mineral'), (b'pollen', b'pollen'), (b'shell', b'shell'), (b'textile', b'textile'), (b'wood', b'wood')])),
                ('references', models.TextField(max_length=2500, null=True, blank=True)),
                ('remarks', models.TextField(max_length=2500, null=True, blank=True)),
                ('geom', django.contrib.gis.db.models.fields.PointField(srid=4326)),
            ],
        ),
    ]
