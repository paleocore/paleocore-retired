"""
This loader/importer script is designed to read data from a sqlite database storing the Ledi-Geraru Research Project
(LGRP) data, and load those data into the PaleoCore postgres database. The script:
1) reads and validates the raw data read in from the occurrence table in the sqlite database and loads the data into
a dictionary (row_dict).  The validation function cleans the data and converts the data to an appropriate format
where necessar;
2) reads and validates related data from the biology table in the LGRP sqlite database where appropriate and adds those
data to separate dictionary (bio_dict);
3) creates a new object of the appropriate subclass (e.g. Biology, Archaeology, Geology), validates the data in the
new object against the original data and if valid saves the new object.
4) the script reports the number of records processed, the number of objects of each class created and reports these at
the end.
"""

# Import libraries
import sqlite3
import os.path
from taxonomy.models import Taxon, TaxonRank, IdentificationQualifier
from lgrp.models import Occurrence, Archaeology, Biology, Geology
from django.contrib.gis.geos import Point
from django.core.exceptions import ObjectDoesNotExist
import datetime
import re
from lgrp.ontologies import LGRP_COLLECTION_CODES
from lgrp.ontologies import LGRP_COLLECTOR_CHOICES, LGRP_ELEMENT_CHOICES, LGRP_ELEMENT_MODIFIER_CHOICES, \
    LGRP_ELEMENT_PORTION_CHOICES, LGRP_ELEMENT_NUMBER_CHOICES


# Required imports for stand-alone django scripts
# http://stackoverflow.com/questions/25244631/models-arent-loaded-yet-error-while-populating-in-django-1-8-and-python-2-7-8
import django
django.setup()

# Global variables
# initiate a list of barcodes used to verify that each barcode added in the validate_row function is unique
barcode_list = []
# absolute file path to the lgrp sqlite database from which we are reading data
if os.path.isfile('/Users/reedd/Documents/projects/PaleoCore/projects/LGRP/LGRP_Paleobase4_2016.sqlite'):
    lgrpdb_path = '/Users/reedd/Documents/projects/PaleoCore/projects/LGRP/LGRP_Paleobase4_2016.sqlite'
elif os.path.isfile('/home/dnr266/paleocore/lgrp/LGRP_Paleobase4_2016.sqlite'):
    lgrpdb_path = '/home/dnr266/paleocore/lgrp/LGRP_Paleobase4_2016.sqlite'
record_limit = ('5000',)  # a limiter setting the maximum number of records to be read from the database, for debugging
# list of fields as they occur in the lgrp sqlite database occurrence table. The list is used to correctly find
# specific data read in from each row of the occurrence table.
occurrence_field_list = ["OBJECTID", "Shape", "CatalogNumberNumeric", "CatalogNumberNumeric_OLD", "BasisOfRecord",
                         "ItemType", "InstitutionalCode", "CollectionCode", "PaleoLocalityNumber", "PaleoLocalityText",
                         "PaleoSubLocality", "ItemNumber", "ItemPart", "CatalogNumber", "GeneralRemarks",
                         "ItemScientificName", "ItemDescription",
                         "Continent", "Country", "StateProvince", "DrainageRegion", "County", "VerbatimCoordinates",
                         "VerbatimCoordinateSystem", "GeoreferenceRemarks", "UTMZone", "UTMEast", "UTMNorth",
                         "CollectingMethod",
                         "RelatedCatalogItems", "Collector", "Finder", "Disposition", "CollectionRemarks", "TimeStamp_",
                         "YearCollected", "IndividualCount", "PreparationStatus", "StratigraphicMarkerUpper",
                         "MetersFromUpper",
                         "StratigraphicMarkerLower", "MetersFromLower", "StratigraphicMarkerFound", "DistanceFromFound",
                         "StratigraphicMarkerLikely", "DistanceFromLikely", "StratigraphicFormation",
                         "StratigraphicMember",
                         "GeologyRemarks", "AnalyticalUnitFound", "AnalyticalUnit1", "AnalyticalUnit2",
                         "AnalyticalUnit3",
                         "AnalyticalUnitLikely", "AnalyticalUnitSimplified", "Insitu", "RankedUnit", "ImageURL",
                         "RelatedInformation", "LocalityID", "StratigraphicSection", "StratigraphicHeightInMeters",
                         "SpecimenImage", "Weathering", "SurfaceModification", "POINT_X", "POINT_Y", "Problem",
                         "ProblemComment", "MonthCollected", "GeodeticDatum", "Barcode", "DateLastModified",
                         "FieldNumber", "ProjectCode"]
# list of lgrp collectors used as a structured vocabulary for the collector field and
# to validate the data in this field.
LGRP_collector_list = [x[0] for x in LGRP_COLLECTOR_CHOICES[0:]]
# list of LGRP stratigraphic members used as structured vocabulary for the member field
LGRP_strat_member_list = ['Basal', 'Basal-Sidi Hakoma', 'Denen Dora', 'Denen Dora-Kada Hadar', 'Kada Hadar',
                         'Sidi Hakoma', 'Sidi Hakoma-Denen Dora']
# list of fields as they occur in the LGRP sqlite database biology table.
biology_field_list = ["CatalogNumberNumeric", "CatalogNumberNumericOLD", "Kingdom", "Phylum", "Class", "Order",
                      "Family", "Subfamily", "Tribe", "Genus", "SpecificEpithet", "IdentificationQualifier",
                      "IdentifiedBy", "DateIdentified", "TypeStatus", "TaxonomyRemarks",
                      "Element", "ElementPortion", "Side", "ElementNumber", "ElementQualifier", "SizeClass",
                      "LifeStage", "ElementRemarks", "DateLastModified", "Barcode", "BiologyRemarks"]
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


def get_field_names(cursor):
    # tuple of 7 element tuples where first element is field name and other elements are None
    field_tuple = cursor.description
    return [e[0] for e in field_tuple]  # get first element in each tuple


def main():
    # Open a connection to the local sqlite database
    print "Opening connection to %s" % lgrpdb_path
    connection = sqlite3.connect(lgrpdb_path)
    occurrence_cursor = connection.cursor()  # cursor for reading data in the occurrence table
    biology_cursor = connection.cursor()  # cursor for reading data in the biology table

    # Fetch all lgrp biology records that need updating from the DB
    selection_string = "select * from biology LEFT JOIN Occurrence USING (CatalogNumberNumeric) WHERE Occurrence.ProjectCode='LGRP';"
    biology_record_set = biology_cursor.execute(selection_string)
    field_list = get_field_names(biology_cursor)
    row_count = 0

    # Iterate and update
    orphans = []
    portion_problems = []
    number_problems = []
    modifier_problems = []
    for row in biology_record_set:
        row_count += 1
        row_id = row[field_list.index('CatalogNumberNumeric')]

        try:
            biology_instance = Biology.objects.get(pk=row_id)
        except ObjectDoesNotExist:
            orphans.append(row_id)
            # print "Record {} has no match in Occurrence".format(row_id)

        el = row[field_list.index('Element')]
        desc = row[field_list.index('ItemDescription')]
        # if el is None and desc is not None:
        #     print "Populating Element {} with Description {} for ID {}".format(el, desc, row_id)
        # if el != desc:
        #     print "Element {} does not match Item Description {} for ID {}".format(el, desc, row_id)


        ep = row[biology_field_list.index('ElementPortion')]
        if ep is None or (ep in [x[0] for x in LGRP_ELEMENT_PORTION_CHOICES[0:]]):
            biology_instance.element_portion = ep
        else:
            portion_problems.append(row_id)
            # print "Portion {} for id {} not in choice list".format(ep, row_id)

        en = row[biology_field_list.index('ElementNumber')]
        if en is None or (en in [x[0] for x in LGRP_ELEMENT_NUMBER_CHOICES[0:]]):
            biology_instance.element_number = en
        else:
            number_problems.append(row_id)
            print "Number {} for id {} not in choice_list".format(en, row_id)

        em = row[biology_field_list.index('ElementQualifier')]
        if em is None or (em in [x[0] for x in LGRP_ELEMENT_MODIFIER_CHOICES[0:]]):
            biology_instance.element_modifier = em
        else:
            modifier_problems.append(row_id)
            print "Modifier {} for id {} not in choice list".format(em, row_id)


        biology_instance.save()

    print "Finished updating {} records \n".format(row_count)
    print "Found {} Orphans:".format(len(orphans))
    #print orphans
    print "Found {} Portion Problems".format(len(portion_problems))
    #print portion_problems

    print "Found {} Number Problems".format(len(number_problems))
    print "Found {} Modifier Problems".format(len(modifier_problems))
    connection.close()
