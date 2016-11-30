__author__ = 'reedd'
"""
This loader/importer script is designed to read data from a sqlite database storing the Hadar Research Project (HRP)
data, and load those data into the PaleoCore postgres database. It assumes that the occurrence and biology table data
has already been imported. This script reads in the data form the dentition table and adds it to the appropriate
Biology occurrences.

The script:
1)
"""

# Import libraries
import sqlite3
import os.path
from lgrp.models import Biology


# Required imports for stand-alone django scripts
# http://stackoverflow.com/questions/25244631/models-arent-loaded-yet-error-while-populating-in-django-1-8-and-python-2-7-8
import django

django.setup()

# Global variables

record_limit = ('20000',)  # a limiter setting the maximum number of records to be read from the database, for debugging
# list of fields as they occur in the HRP sqlite database dentition table. The list is used to correctly find
# specific data read in from each row of the occurrence table.
dentition_field_list = ['FaunaAttrbutesID', 'CatalogNumberNumeric', 'CatalogNumberNumberic_OLD', 'Maxilla', 'Mandible',
                        'uli1', 'uli2', 'uli3', 'uri1', 'uri2', 'uri3', 'ulc', 'urc', 'ulp1', 'ulp2', 'ulp3', 'ulp4',
                        'urp1', 'urp2', 'urp3', 'urp4', 'ulm1', 'ulm2', 'ulm3', 'ulm4', 'urm1', 'urm2', 'urm3', 'urm4',
                        'lli1', 'lli2', 'lli3', 'lri1', 'lri2', 'lri3', 'llc', 'lrc', 'llp1', 'llp2', 'llp3', 'llp4',
                        'lrp1', 'lrp2', 'lrp3', 'lrp4', 'llm1', 'llm2', 'llm3', 'llm4', 'lrm1', 'lrm2', 'lrm3', 'lrm4',
                        'indet_incisor', 'indet_canine', 'indet_premolar', 'indet_molar',
                        'indet_Tooth', 'deciduous']


# structured vocabularies for fields in the biology table.
rank_list = ['Kingdom', 'Phylum', 'Class', 'Order', 'Family']

taxon_dict = {'Kingdom': '', 'Phylum': '', 'Class': '', 'Order': '', 'Family': '',
              'Subfamily': '', 'Tribe': '', 'Genus': '', 'Species': ''}

element_list = ['astragalus', 'bacculum', 'bone (indet.)', 'calcaneus', 'canine', 'capitate', 'carapace',
                'carpal (indet.)', 'carpal/tarsal', 'carpometacarpus', 'carpus', 'chela', 'clavicle', 'coccyx',
                'coprolite', 'cranium', 'cranium w/horn core', 'cuboid', 'cubonavicular', 'cuneiform',
                'dermal plate', 'egg shell', 'endocast', 'ethmoid', 'femur', 'fibula', 'frontal', 'hamate',
                'horn core', 'humerus', 'hyoid', 'ilium', 'incisor', 'innominate', 'ischium', 'lacrimal',
                'long bone', 'lunate', 'mandible', 'manus', 'maxilla', 'metacarpal', 'metapodial',
                'metatarsal', 'molar', 'nasal', 'navicular', 'naviculocuboid', 'occipital', 'ossicone',
                'parietal', 'patella', 'pes', 'phalanx', 'pisiform', 'plastron', 'premaxilla', 'premolar',
                'pubis', 'radioulna', 'radius', 'rib', 'sacrum', 'scaphoid', 'scapholunar', 'scapula', 'scute',
                'sesamoid', 'shell', 'skeleton', 'skull', 'sphenoid', 'sternum', 'talon', 'talus',
                'tarsal (indet.)', 'tarsometatarsus', 'tarsus', 'temporal', 'tibia', 'tibiotarsus',
                'tooth (indet.)', 'trapezium', 'trapezoid', 'triquetrum', 'ulna', 'vertebra', 'vomer',
                'zygomatic']

if os.path.isfile('/Users/reedd/Documents/projects/PaleoCore/projects/LGRP/LGRP_Paleobase4_2016.sqlite'):
    lgrpdb_path = '/Users/reedd/Documents/projects/PaleoCore/projects/LGRP/LGRP_Paleobase4_2016.sqlite'
elif os.path.isfile('/home/dnr266/paleocore/lgrp/LGRP_Paleobase4_2016.sqlite'):
    lgrpdb_path = '/home/dnr266/paleocore/lgrp/LGRP_Paleobase4_2016.sqlite'


def valid_dentition(row):
    if row:  # if there is row data, many will be None
        # perhaps validate dentition data against element data in biology table.
        # if upper teeth only, element = maxilla
        # if lower teeth only, element = mandible
        # if both element is max+man
        return True
    else:
        return None


def add_dentition_data(row, obj):
    obj_field_list = obj.get_all_field_names()
    for f in dentition_field_list:
        if f in obj_field_list:
            if row[dentition_field_list.index(f)]:
                fval = True
            else:
                fval = False
            setattr(obj, f, fval)
    return obj


def get_field_names(cursor):
    # tuple of 7 element tuples where first element is field name and other elements are None
    field_tuple = cursor.description
    return [e[0] for e in field_tuple]  # get first element in each tuple


def main():
    # Open a connection to the local sqlite database
    print "Opening connection to %s" % lgrpdb_path
    connection = sqlite3.connect(lgrpdb_path)  # open a connection to the HRP sqlite database
    dentition_cursor = connection.cursor()  # cursor for reading data in the dentition table

    # Fetch all dentition and biology data, using INNER join insures matching records
    sql_string = '''SELECT dentition.* FROM dentition
INNER JOIN biology ON (dentition.CatalogNumberNumeric = biology.CatalogNumberNumeric)
INNER JOIN Occurrence ON (biology.CatalogNumberNumeric = Occurrence.CatalogNumberNumeric);'''
    ''' SELECT ULI1,
    ULI2,
    ULI3,
    URI1,
    URI2,
    URI3,
    ULC
    URC,
    ULP1,
    ULP2,
    ULP3,
    ULP4,
    URP1,
    URP2,
    URP3,
    URP4,
    ULM1,
    ULM2,
    ULM3,
    ULM4,
    URM1,
    URM2,
    URM3,
    URM4,
    LLi1,
    LLi2,
    LLi3,
    LRi1,
    LRi2,
    LRi3,
    LLc,
    LRc,
    LLp1,
    LLp2,
    LLp3,
    LLp4,
    LRp1,
    LRp2,
    LRp3,
    LRp4,
    LLm1,
    LLm2,
    LLm3,
    LLm4,
    LRm1,
    LRm2,
    LRm3,
    LRm4,
    IndeterminateIncisor,
    IndeterminateCanine,
    IndeterminatePremolar,
    IndeterminateMolar,
    IndeterminateTooth,
    Deciduous
    '''
    dentition_rs = dentition_cursor.execute(sql_string)
    field_list = get_field_names(dentition_cursor)
    row_count = 0
    update_count = 0

    # Iterate and update
    orphans = []
    excluded_fields = ('FaunaAttrbutesID', 'CatalogNumberNumeric', 'CatalogNumberNumberic_OLD',
                       'Maxilla', 'Mandible')
    camel_case_fields = (
        'IndeterminateIncisor', 'IndeterminateCanine', 'IndeterminatePremolar', 'IndeterminateMolar',
        'IndeterminateTooth')
    camel_case_dictionary = {'IndeterminateIncisor': 'indet_incisor', 'IndeterminateCanine': 'indet_canine',
                             'IndeterminatePremolar': 'indet_premolar', 'IndeterminateMolar': 'indet_premolar',
                             'IndeterminateTooth': 'indet_tooth'}
    for row in dentition_rs:
        row_count += 1
        row_id = row[field_list.index('CatalogNumberNumeric')]
        if row_count%100:
            "Processing BiologyID {}".format(row_id)

        # Find matching Biology instance
        biology_instance = Biology.objects.get(pk=row_id)

        # iterate through columns in the row
        row_index = 0
        for i in row:
            if i and i > 0:  # if not None and positive
                column_name = field_list[row_index]  # look up column name from index

                if column_name in excluded_fields:  # skip excluded fields
                    pass
                elif column_name in camel_case_fields:  # convert using dictionary and assign
                    setattr(biology_instance, camel_case_dictionary[column_name], True)
                else:  # convert string and assign
                    setattr(biology_instance, column_name.lower(), True)
            row_index += 1

        biology_instance.save()
        update_count += 1

    print "Processed {} records, and updated {} biology objects".format(row_count, update_count)
    connection.close()  # close the connection


main()  # process data in the sqlite database
