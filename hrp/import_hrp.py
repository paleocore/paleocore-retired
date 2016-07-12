__author__ = 'reedd'

import sqlite3
from hrp.models import Occurrence, Locality
from django.contrib.gis.geos import Point
from django.core.exceptions import ObjectDoesNotExist
import datetime

# Global variables
barcode_list = []
hrpdb_path = '/Users/reedd/Documents/projects/PaleoCore/projects/HRP/HRP_Paleobase4_2016.sqlite'
record_limit = ('20000',)
field_list = ["OBJECTID", "Shape", "CatalogNumberNumeric",  "CatalogNumberNumeric_OLD", "BasisOfRecord", "ItemType",
              "InstitutionalCode", "CollectionCode", "PaleoLocalityNumber", "PaleoLocalityText", "PaleoSubLocality",
              "ItemNumber", "ItemPart", "CatalogNumber", "GeneralRemarks", "ItemScientificName", "ItemDescription",
              "Continent", "Country", "StateProvince", "DrainageRegion", "County", "VerbatimCoordinates",
              "VerbatimCoordinateSystem", "GeoreferenceRemarks", "UTMZone", "UTMEast", "UTMNorth", "CollectingMethod",
              "RelatedCatalogItems", "Collector", "Finder", "Disposition", "CollectionRemarks", "TimeStamp_",
              "YearCollected", "IndividualCount", "PreparationStatus", "StratigraphicMarkerUpper", "MetersFromUpper",
              "StratigraphicMarkerLower", "MetersFromLower", "StratigraphicMarkerFound", "DistanceFromFound",
              "StratigraphicMarkerLikely", "DistanceFromLikely", "StratigraphicFormation", "StratigraphicMember",
              "GeologyRemarks", "AnalyticalUnitFound", "AnalyticalUnit1", "AnalyticalUnit2", "AnalyticalUnit3",
              "AnalyticalUnitLikely", "AnalyticalUnitSimplified", "Insitu", "RankedUnit", "ImageURL",
              "RelatedInformation", "LocalityID", "StratigraphicSection", "StratigraphicHeightInMeters",
              "SpecimenImage", "Weathering", "SurfaceModification", "POINT_X", "POINT_Y", "Problem",
              "ProblemComment", "MonthCollected", "GeodeticDatum", "Barcode", "DateLastModified",
              "FieldNumber", "ProjectCode"]

HRP_collector_list = ['C.J. Campisano', 'W.H. Kimbel', 'T.K. Nalley', 'D.N. Reed', 'K.E. Reed', 'B.J. Schoville',
                      'A.E. Shapiro',  'HFS Student', 'HRP Team']

HRP_strat_member_list = ['Basal', 'Basal-Sidi Hakoma', 'Denen Dora', 'Denen Dora-Kada Hadar', 'Kada Hadar',
                         'Sidi Hakoma', 'Sidi Hakoma-Denen Dora']

# Helper Functions
def transform_point(row):
    """
    Create a point object from UTM coordinates
    :param row:
    :return point_object:
    """

    # Fetch coordinates from row data
    occurrence_coordinates = row[field_list.index('POINT_X'):field_list.index('POINT_Y') + 1]
    occurrence_id = row[field_list.index('CatalogNumberNumeric')]
    # Transform coordinates from UTM to GCS
    try:
        pt = Point(occurrence_coordinates, srid=32637)
        pt.transform(4326)
        # print "GCS coordinates: %f %f" % pt.coords
    except ValueError:
        print "Problem transforming coordinates for occurrence id %s" % occurrence_id

    return pt


def convert_date_recorded(row):
    """
    Convert date_recorded string to datetime object
    :param row:
    :return date_recorded as datetime object:
    """
    occurrence_id = row[field_list.index('CatalogNumberNumeric')]
    date_recorded_string = row[field_list.index('TimeStamp_')]

    # Import date_recorded from string
    if date_recorded_string and date_recorded_string != '':
        if len(date_recorded_string) == 9:
            date_recorded = datetime.datetime.strptime(date_recorded_string, '%d-%b-%y')
        elif len(date_recorded_string) == 19:
            date_recorded = datetime.datetime.strptime(date_recorded_string, '%Y-%m-%d %H:%M:%S')
        else:
            print "Import found Invalid date_recorded %s for Occurrence %s" % (date_recorded_string, occurrence_id)
            return False
    else:
        date_recorded = None
    return date_recorded


def convert_date_last_modified(row):
    """
    Convert row DateLastModified string to datetime object
    :param row:
    :return dlm as datetime object:
    """

    dlm = None
    dlm_string = row[field_list.index('DateLastModified')]
    if dlm_string and dlm_string != '':
        dlm = datetime.datetime.strptime(dlm_string, '%m/%d/%y %H:%M:%S')
    return dlm


def convert_in_situ(row):
    """
    Convert in_situ floats to True/False, defaults to False
    :param row:
    :return:
    """
    in_situ_float = row[field_list.index('Insitu')]
    in_situ = False
    if in_situ_float == 0.0:
        in_situ = False
    elif in_situ_float in (-1.0, 1.0):
        in_situ = True
    elif not in_situ_float:
        in_situ = False
    return in_situ


def convert_ranked(row):
    """
    Convert ranked floats to True/False, defaults to False
    :param row:
    :return:
    """
    ranked_float = row[field_list.index('RankedUnit')]
    ranked = False
    if ranked_float == 0.0:
        ranked = False
    elif ranked_float in (-1.0, 1.0):
        ranked = True
    elif not ranked_float:
        ranked = False
    return ranked


def convert_problem(row):
    """
    Convert problem integer to Yes/No
    :param row:
    :return:
    """
    problem_integer = row[field_list.index('Problem')]
    if problem_integer in (1, -1):
        return True
    elif not problem_integer or problem_integer == 0:
        return False


# Define validate function
def validate_row(row):
    """
    Validate row data, convert data types where necessary and
    return a dictionary of cleaned, validated data.
    :param row:
    :return False or row_dict:
    """
    row_dict = {}  # dictionary of row converted and clean row data

    # Validate Occurrence ID
    occurrence_id = row[field_list.index('CatalogNumberNumeric')]  # read id from row CatalogNumberNumeric in row data
    if occurrence_id and occurrence_id > 0:  # if occurrence_id is not Null and positive
        if Occurrence.objects.filter(id=occurrence_id).exists():  # if occurrence_id is duplicate
            print "Warning, Occurrence id %s already exists" % occurrence_id   # print warning
            return False  # return a failed validation
        else:  # if occurrence_id not null and not duplicate then add to dictionary
            row_dict['occurrence_id'] = occurrence_id
    else:
        print "Missing or non-positive occurrence ID!"
        return False

    # Validate coordinates
    # read coordinates from POINT_X and POINT_Y in row data
    coordinates_list = row[field_list.index('POINT_X'):field_list.index('POINT_Y') + 1]
    # Validate that UTM coordinates are proper size
    if coordinates_list and coordinates_list[0] > 100000 and coordinates_list[1] > 1000000:
        pt = transform_point(row)
        row_dict['geom'] = pt
    else:
        print "Error validating coordinates for Occurrence %s" % occurrence_id
        return False

    # Validate basis of record
    basis_of_record = row[field_list.index('BasisOfRecord')]
    if basis_of_record in ("Collection", "Observation"):
        row_dict['basis_of_record'] = basis_of_record
    else:
        print "Invalid Basis %s for Occurrence %s" % (basis_of_record, occurrence_id)
        return False

    # Validate item type
    item_type = row[field_list.index('ItemType')]
    if item_type in ("Faunal", "Floral", "Artifactual", "Geological"):
        row_dict['item_type'] = item_type
    else:
        print "Invalid item type %s for Occurrence %s" % (item_type, occurrence_id)
        return False

    # Validate collection code
    collection_code = row[field_list.index('CollectionCode')]
    if (basis_of_record == "Collection" and collection_code == 'A.L.') or \
            (basis_of_record == "Observation" and not collection_code):
        row_dict['collection_code'] = collection_code
    else:
        print "Invalid Collection Code %s for Occurrence %s" % (collection_code, occurrence_id)
        return False

    # Validate PaleoLocalityNumber
    paleolocality_number = row[field_list.index('PaleoLocalityNumber')]
    if basis_of_record == 'Collection' and int(paleolocality_number) > 0:
        row_dict['paleolocality_number'] = int(paleolocality_number)
    elif basis_of_record == 'Observation' and not paleolocality_number:
        row_dict['paleolocality_number'] = None
    else:
        print "Invalid paleolocality number %s for Occurrence %s" % (paleolocality_number, occurrence_id)
        return False

    # Validate paleo_sublocality
    paleo_sublocality = row[field_list.index('PaleoSubLocality')]
    if paleo_sublocality and not paleolocality_number:
        print "Invalid paleo_sublocality %s for Occurrence %s" % (paleo_sublocality, occurrence_id)
        return False
    else:
        row_dict['paleo_sublocality'] = paleo_sublocality

    # Validate item number
    item_number = row[field_list.index('ItemNumber')]
    if item_number and not paleolocality_number:
        print "Invalid item number %s for Occurrence %s" % (item_number, occurrence_id)
        return False
    else:
        row_dict['item_number'] = item_number

    # Validate item part
    item_part = row[field_list.index('ItemPart')]
    if item_part and not item_number:
        print "Invalid item part %s for Occurrence %s" % (item_part, occurrence_id)
        return False
    else:
        row_dict['item_part'] = item_part

    # Validate Catalog Number
    catalog_number = row[field_list.index('CatalogNumber')]
    if basis_of_record == "Collection" and not catalog_number:
        print "Invalid catalog number %s for Occurrence %s" % (catalog_number, occurrence_id)
        return False

    elif basis_of_record == "Collection" and catalog_number:
        collection_code_text = ''
        locality_text = ''
        item_text = ''

        # Validate and build collection code text
        if collection_code and collection_code != '':
            collection_code_text = collection_code + ' '

        # Validate and build locality text
        if paleolocality_number:
            if paleo_sublocality and paleo_sublocality != '':
                locality_text = str(int(paleolocality_number)) + paleo_sublocality
            else:
                locality_text = str(int(paleolocality_number))

        # Validate and build item_text
        if item_number and item_number != '':
            if item_part and item_part != '':
                item_text = '-' + item_number + item_part
            else:
                item_text = '-' + item_number

        catnum = collection_code_text + locality_text + item_text

        if catnum != catalog_number:
            print "Invalid catnum %s does not match %s for Occurrence %s" % (catnum, catalog_number, occurrence_id)
            return False
        else:
            row_dict['catalog_number'] = catalog_number

    if basis_of_record == 'Observation' and catalog_number:
        print "Invalid catalog number %s for Observation Occurrence %s" % (catalog_number, occurrence_id)
        return False

    elif basis_of_record == 'Observation' and not catalog_number:
        row_dict['catalog_number'] = None

    # Validate Drainage Region
    row_dict['drainage_region'] = row[field_list.index('DrainageRegion')]

    # Validate Remarks
    row_dict['remarks'] = row[field_list.index('GeneralRemarks')]

    # Validate Item Scientific Name
    item_scientific_name = row[field_list.index('ItemScientificName')]
    if item_scientific_name and item_scientific_name != '':
        row_dict['item_scientific_name'] = item_scientific_name
    else:
        print "Invalid ItemScientificName %s for Occurrence %s" % (item_scientific_name, occurrence_id)
        return False

    # Validate Item Description
    row_dict['item_description'] = row[field_list.index('ItemDescription')]

    # Validate Georeference Remarks
    row_dict['georeference_remarks'] = row[field_list.index('GeoreferenceRemarks')]

    # Validate Collecting Method
    collecting_method = row[field_list.index('CollectingMethod')]
    if collecting_method in ('Crawl Survey', 'dryscreen5mm', 'Dry Screen', 'Excavation', 'Survey',
                             'Transect Survey', 'Wet Screen', 'wetscreen1mm', None):
        row_dict['collecting_method'] = collecting_method
    else:
        print "Invalid Collecting Method %s for Occurrence %s" % (collecting_method, occurrence_id)
        return False

    # Validate Related Catalog Items
    row_dict['related_catalog_items'] = row[field_list.index('RelatedCatalogItems')]

    # Validate Field Number
    row_dict['field_number'] = row[field_list.index('FieldNumber')]

    # Validate Collector
    collector = row[field_list.index('Collector')]
    if not collector or (collector in HRP_collector_list):
        row_dict['collector'] = collector
    else:
        print "Invalid Collector %s for Occurrence %s" % (collector, occurrence_id)
        return False

    # Validate Finder
    row_dict['finder'] = row[field_list.index('Finder')]

    # Validate Disposition
    row_dict['disposition'] = row[field_list.index('Disposition')]

    # Validate Collection Remarks
    row_dict['collection_remarks'] = row[field_list.index('CollectionRemarks')]

    # Validate date_recordeds. Check that entries are either Null, Date, or DateTime
    date_recorded = convert_date_recorded(row)
    row_dict['date_recorded'] = date_recorded

    # Validate year collected
    year_collected_string = row[field_list.index('YearCollected')]
    try:
        year_collected = int(year_collected_string)  # try converting year collected from str to int
        if date_recorded and (int(date_recorded.year) != year_collected):
            print "Year collected %s does not match date_recorded %s for Occurrence %s" % (year_collected, date_recorded,
                                                                                       occurrence_id)
            return False
        if 1970 < year_collected <= datetime.datetime.now().year:
            row_dict['year_collected'] = year_collected
        else:
            print "Invalid year collected %s for Occurrence %s" % (year_collected, occurrence_id)
            return False
    except TypeError:  # Null raises TypeError
        if not year_collected_string:
            year_collected = None
            print "Warning year collected is Null for Occurrence %s" % (occurrence_id)
        else:  # If not null something else bad is happening, print general error
            print "Invalid year collected %s for Occurrnce %s" % (year_collected, occurrence_id)
            return False
    except ValueError:  # If string such as fubar can't be convered raises ValueError
        print "Invalid year collected %s for Occurrence %s" % (year_collected, occurrence_id)
        return False

    # Validate Individual Count
    try:
        individual_count = row[field_list.index('IndividualCount')]
        row_dict['individual_count'] = individual_count
    except TypeError:
        if not individual_count:
            row_dict['individual_count'] = None
        else:
            print "Invalid individual count %s for Occurrence %s" % (individual_count, occurrence_id)
            return False

    # Validate Preparation Status
    row_dict['preparation_status'] = row[field_list.index('PreparationStatus')]

    # Validate stratigraphic information
    row_dict['stratigraphic_marker_upper'] = row[field_list.index('StratigraphicMarkerUpper')]
    row_dict['distance_from_upper'] = row[field_list.index('MetersFromUpper')]
    row_dict['stratigraphic_marker_lower'] = row[field_list.index('StratigraphicMarkerLower')]
    row_dict['distance_from_lower'] = row[field_list.index('MetersFromLower')]
    row_dict['stratigraphic_marker_found'] = row[field_list.index('StratigraphicMarkerFound')]
    row_dict['distance_from_found'] = row[field_list.index('DistanceFromFound')]
    row_dict['stratigraphic_marker_likely'] = row[field_list.index('StratigraphicMarkerLikely')]
    row_dict['distance_from_likely'] = row[field_list.index('DistanceFromLikely')]

    # Validate Stratigraphic Formation
    stratigraphic_formation = row[field_list.index('StratigraphicFormation')]
    if (not stratigraphic_formation) or (stratigraphic_formation == ''):
        row_dict['stratigraphic_formation'] = None
    elif stratigraphic_formation in ('Hadar', 'Busidima', 'Hadar-Busidima'):
        row_dict['stratigraphic_formation'] = stratigraphic_formation
    else:
        print "Invalid stratigraphic formation %s for Occcurrence %s" % (stratigraphic_formation, occurrence_id)
        return False

    # Validate Stratigraphic Member
    stratigraphic_member = row[field_list.index('StratigraphicMember')]
    if (not stratigraphic_member) or (stratigraphic_member in HRP_strat_member_list):
        row_dict['stratigraphic_member'] = stratigraphic_member
    else:
        print "Invalid stratigraphic member %s for Occcurrence %s" % (stratigraphic_member, occurrence_id)
        return False

    # Validate Analytical Unit
    row_dict['analytical_unit'] = row[field_list.index('AnalyticalUnit1')]
    row_dict['analytical_unit_2'] = row[field_list.index('AnalyticalUnit2')]
    row_dict['analytical_unit_3'] = row[field_list.index('AnalyticalUnit3')]
    row_dict['analytical_unit_found'] = row[field_list.index('AnalyticalUnitFound')]
    row_dict['analytical_unit_likely'] = row[field_list.index('AnalyticalUnitLikely')]
    row_dict['analytical_unit_simplified'] = row[field_list.index('AnalyticalUnitSimplified')]

    # Validate In Situ
    in_situ_float = row[field_list.index('Insitu')]
    if in_situ_float in (None, -1.0, 0.0, 1.0):
        row_dict['in_situ'] = convert_in_situ(row)  # pass value to helper function
    else:
        print "Invalid in_situ %s for Occurrence %s" % (in_situ_float, occurrence_id)
        return False

    # Validate Ranked
    ranked_float = row[field_list.index('RankedUnit')]
    if ranked_float in (None, -1.0, 0.0, 1.0):
        row_dict['ranked'] = convert_ranked(row)  # pass value to helper function
    else:
        print "Invalid ranked value %s for Occurrence %s" % (ranked_float, occurrence_id)
        return False

    # Validate Weathering
    weathering = row[field_list.index('Weathering')]
    if (weathering is None) or (weathering <= 5):
        row_dict['weathering'] = weathering
    else:
        print "Invalid weathering %s for Occurrence %s" % (weathering, occurrence_id)
        return False

    # Validate Surface Modification
    row_dict['surface_modification'] = row[field_list.index('SurfaceModification')]

    # Validate Problem
    problem_integer = row[field_list.index('Problem')]
    if problem_integer in (None, 1, 0):
        row_dict['problem'] = convert_problem(row)
    else:
        print "Invalid problem %s for Occurrence %s" % (problem_integer, occurrence_id)
        return False

    # Validate Problem Comment
    row_dict['problem_comment'] = row[field_list.index('ProblemComment')]

    # Validate barcode
    # Barcodes should exist for all Collected items and not for Observations
    barcode = row[field_list.index('Barcode')]
    if basis_of_record == 'Collection':
        if not barcode:
            known_problem_tuple = (9900, 11307, 11310, 11311)
            if occurrence_id not in known_problem_tuple:  # ignore missing barcodes for known problems
                print "Missing barcode for Collection Occurrence %s" % occurrence_id
                return False
            elif occurrence_id in known_problem_tuple:
                row_dict['barcode'] = None
        elif barcode:
            if len(barcode) != 6 or barcode in barcode_list:
                print "Invalid barcode length  or duplicate barcode %s for Occurrence %s" % (barcode, occurrence_id)
                return False
            elif barcode not in barcode_list:  # check that well formed barcodes are unique
                barcode_list.append(barcode)
                row_dict['barcode'] = barcode
    elif basis_of_record == 'Observation':
        if barcode:
            print "Invalid barcode present for Observation Occurrence %s" % occurrence_id
            return False
        elif not barcode:
            row_dict['barcode'] = None

    # Validate Date Last Modified
    dlm = convert_date_last_modified(row)
    if not dlm:
        row_dict['date_last_modified'] = None

    elif dlm.year < 1970:
        print "Invalid date last modified %s for Occurrence %s" % (dlm, occurrence_id)
        return False 
    else:
        row_dict['date_last_modified'] = dlm

    # Validate length of row dictionary
    if len(row_dict.keys()) != 50:
        print "Invalid row dictionary length %s for Occurrence %s" % (len(row_dict.keys()), occurrence_id)
        print row_dict.keys()
    return row_dict


def get_locality(row):
    """
    Fetch the corresponding locality object for an occurrence and create a new one if necessary.
    :param row:
    :return locality_object:
    """

    # Validate and build locality text
    basis_of_record = row[field_list.index('BasisOfRecord')]
    collection_code = row[field_list.index('CollectionCode')]
    locality_number = row[field_list.index('PaleoLocalityNumber')]
    sublocality = row[field_list.index('PaleoSubLocality')]
    pt = transform_point(row)

    if basis_of_record == 'Collection':
        if locality_number:
            if sublocality and sublocality != '':
                locality_text = str(int(locality_number)) + sublocality
            else:
                locality_text = str(int(locality_number))

        # Check if Locality exists
        try:
            locality = Locality.objects.get(pk=locality_text)
            return locality
        except ObjectDoesNotExist:
            # If not create a new one and return it
            locality = Locality(id=locality_text,
                                collection_code=collection_code,
                                locality_number=locality_number,
                                collection_code=collection_code,
                                sublocality=sublocality,
                                date_last_modified=datetime.datetime.now(),
                                geom=pt)
            try:
                locality.save()
            except:
                print "locality save error for locality %s" % locality_number

            return locality


def import_collection(row_dict, locality):
    new_occurrence = Occurrence(id=row_dict['occurrence_id'],
                                geom=row_dict['geom'],
                                basis_of_record=row_dict['basis_of_record'],
                                item_type=row_dict['item_type'],
                                collection_code=row_dict['collection_code'],
                                locality=locality,
                                item_number=row_dict['item_number'],
                                item_part=row_dict['item_part'],
                                catalog_number=row_dict['catalog_number'],
                                remarks=row_dict['remarks'],
                                item_scientific_name=row_dict['item_scientific_name'],
                                item_description=row_dict['item_description'],
                                drainage_region=row_dict['drainage_region'],
                                georeference_remarks=row_dict['georeference_remarks'],
                                collecting_method=row_dict['collecting_method'],
                                related_catalog_items=row_dict['related_catalog_items'],
                                field_number=row_dict['field_number'],
                                collector=row_dict['collector'],
                                finder=row_dict['finder'],
                                disposition=row_dict['disposition'],
                                collection_remarks=row_dict['collection_remarks'],
                                date_recorded=row_dict['date_recorded'],
                                year_collected=row_dict['year_collected'],
                                individual_count=row_dict['individual_count'],
                                preparation_status=row_dict['preparation_status'],
                                analytical_unit=row_dict['analytical_unit'],
                                analytical_unit_2=row_dict['analytical_unit_2'],
                                analytical_unit_3=row_dict['analytical_unit_3'],
                                analytical_unit_found=row_dict['analytical_unit_found'],
                                analytical_unit_likely=row_dict['analytical_unit_likely'],
                                analytical_unit_simplified=row_dict['analytical_unit_simplified'],
                                in_situ=row_dict['in_situ'],
                                ranked=row_dict['ranked'],
                                weathering=row_dict['weathering'],
                                surface_modification=row_dict['surface_modification'],
                                problem=row_dict['problem'],
                                problem_comment=row_dict['problem_comment'],
                                barcode=row_dict['barcode'],
                                date_last_modified=row_dict['date_last_modified'],
                                )
    return new_occurrence


def import_observation(row_dict):
    new_occurrence = Occurrence(id=row_dict['occurrence_id'],
                                geom=row_dict['geom'],
                                basis_of_record=row_dict['basis_of_record'],
                                item_type=row_dict['item_type'],
                                # collection_code=row_dict['collection_code'],
                                # locality=locality,
                                # item_number=row_dict['item_number'],
                                # item_part=row_dict['item_part'],
                                # catalog_number=row_dict['catalog_number'],
                                remarks=row_dict['remarks'],
                                item_scientific_name=row_dict['item_scientific_name'],
                                item_description=row_dict['item_description'],
                                drainage_region=row_dict['drainage_region'],
                                georeference_remarks=row_dict['georeference_remarks'],
                                collecting_method=row_dict['collecting_method'],
                                related_catalog_items=row_dict['related_catalog_items'],
                                field_number=row_dict['field_number'],
                                collector=row_dict['collector'],
                                finder=row_dict['finder'],
                                disposition=row_dict['disposition'],
                                collection_remarks=row_dict['collection_remarks'],
                                date_recorded=row_dict['date_recorded'],
                                year_collected=row_dict['year_collected'],
                                individual_count=row_dict['individual_count'],
                                preparation_status=row_dict['preparation_status'],
                                analytical_unit=row_dict['analytical_unit'],
                                analytical_unit_2=row_dict['analytical_unit_2'],
                                analytical_unit_3=row_dict['analytical_unit_3'],
                                analytical_unit_found=row_dict['analytical_unit_found'],
                                analytical_unit_likely=row_dict['analytical_unit_likely'],
                                analytical_unit_simplified=row_dict['analytical_unit_simplified'],
                                in_situ=row_dict['in_situ'],
                                ranked=row_dict['ranked'],
                                weathering=row_dict['weathering'],
                                surface_modification=row_dict['surface_modification'],
                                problem=row_dict['problem'],
                                problem_comment=row_dict['problem_comment'],
                                barcode=row_dict['barcode'],
                                date_last_modified=row_dict['date_last_modified'],
                                )

    # new_occurrence.save()
    return new_occurrence


def validate_new_record(occurrence_object, row):
    if occurrence_object.id != int(row[field_list.index('CatalogNumberNumeric')]):
        print "Problem importing id for Occurrence %s" % occurrence_object.id
        return False

    if occurrence_object.basis_of_record != row[field_list.index('BasisOfRecord')]:
        print "Problem importing basis of record %s for Occurrence %s" % \
              (occurrence_object.basis_of_record,
               occurrence_object.id)
        return False

    if occurrence_object.item_type != row[field_list.index('ItemType')]:
        print "Problem importing item type %s for Occurrence %s" % \
              (occurrence_object.basis_of_record, occurrence_object.id)
        return False
    if occurrence_object.collection_code != row[field_list.index('CollectionCode')]:
        print "Problem importing collection code %s for Occurrence %s" % \
              (occurrence_object.collection_code, occurrence_object.id)
        return False
    if occurrence_object.catalog_number != row[field_list.index('CatalogNumber')]:
        print "Catalog Number %s does not match CatalogNumber %s for Occurrence %s" % \
              (occurrence_object.catalog_number, row[field_list.index('CatalogNumber')], occurrence_object.id)
        return False
    if occurrence_object.item_scientific_name != row[field_list.index('ItemScientificName')]:
        print "Item scientific name %s does not match ItemScientificName %s for Occurrence %s" % \
              (occurrence_object.item_scientific_name, row[field_list.index('ItemScientificName')], occurrence_object.id)
        return False
    if occurrence_object.item_description != row[field_list.index('ItemDescription')]:
        print "Item description %s does not match ItemDescription %s for Occurrence %s" % \
              (occurrence_object.item_description, row[field_list.index('ItemDescription')], occurrence_object.id)
        return False
    if occurrence_object.collecting_method != row[field_list.index('CollectingMethod')]:
        print "Collecting method %s does not match CollectingMethod %s for Occurrence %s" % \
              (occurrence_object.collecting_method, row[field_list.index('CollectingMethod')], occurrence_object.id)
        return False
    if occurrence_object.collector != row[field_list.index('Collector')]:
        print "Collector %s does not match Collector %s for Occurrence %s" % \
              (occurrence_object.collector, row[field_list.index('Collector')], occurrence_object.id)
        return False
    if int(occurrence_object.year_collected) != int(row[field_list.index('YearCollected')]):
        print "Year collected %s does not match YearCollected %s for Occurrence %s" % \
              (occurrence_object.year_collected, row[field_list.index('YearCollected')], occurrence_object.id)
        return False
    if occurrence_object.analytical_unit != row[field_list.index('AnalyticalUnit1')]:
        print "Analytical Unit %s does not match AnalyticalUnit1 %s for Occurrence %s" % \
              (occurrence_object.analytical_unit, row[field_list.index('AnalyticalUnit1')], occurrence_object.id)
        return False
    if occurrence_object.barcode != row[field_list.index('Barcode')]:
        print "Barcode %s does not match Barcode %s for Occurrence %s" % \
              (occurrence_object.barcode, row[field_list.index('Barcode')], occurrence_object.id)
        return False
    else:
        return True


def main():
    import_count = 0
    collection_count = 0
    observation_count = 0
    row_count = 0
    print "Fetching a maximum of %s records" % record_limit
    for row in cursor.execute('SELECT * FROM Occurrence WHERE ProjectCode = "HRP" LIMIT ?', record_limit):
        row_count += 1
        valid_row_dict = validate_row(row)
        if valid_row_dict:
            basis_of_record = valid_row_dict['basis_of_record']
            if basis_of_record == 'Collection':
                locality = get_locality(row)
                new_occurrence = import_collection(valid_row_dict, locality)
                import_count += 1
                collection_count += 1
                if validate_new_record(new_occurrence, row):
                    new_occurrence.save()
                    # try:
                    #     new_occurrence.save()
                    # except:
                    #     print "Problem saving occurrence %s" % new_occurrence.id
            elif basis_of_record == 'Observation':
                new_occurrence = import_observation(valid_row_dict)
                import_count += 1
                observation_count += 1
                if validate_new_record(new_occurrence, row):
                    try:
                        new_occurrence.save()
                    except:
                        print "Problem saving occurrence %s" % new_occurrence.id
        else:
            print "Invalid row for Occurrence %s " % row[field_list.index('CatalogNumberNumeric')]
    print "Number of rows processed: %s \nNumber of records imported: %s" % (row_count, import_count)
    print "Imported %s collections and %s observations" % (collection_count, observation_count)

# Create a connection to the SQLite DB with HRP data

# Open a connection to the local sqlite database
connection = sqlite3.connect(hrpdb_path)
cursor = connection.cursor()

# Fetch data from the database
cursor.execute('SELECT * FROM Occurrence;')
record_count = len(cursor.fetchall())
print "Total record count %s" % record_count

main()

connection.close()
