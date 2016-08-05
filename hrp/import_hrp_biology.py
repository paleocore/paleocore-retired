__author__ = 'reedd'

import sqlite3
from hrp.models import Occurrence, Locality, Biology
from taxonomy.models import Taxon, TaxonRank
from django.contrib.gis.geos import Point
from django.core.exceptions import ObjectDoesNotExist
import datetime
import django

django.setup()

# Global variables
barcode_list = []
hrpdb_path = '/Users/reedd/Documents/projects/PaleoCore/projects/HRP/HRP_Paleobase4_2016.sqlite'
record_limit = ('50000',)

biology_field_list = ["CatalogNumberNumeric", "CatalogNumberNumericOLD", "Kingdom", "Phylum", "Class", "Order", "Family", "Subfamily", "Tribe",
              "Genus", "SpecificEpithet", "IdentificationQualifier", "IdentifiedBy", "DateIdentified", "TypeStatus",
              "TaxonomyRemarks", "Element", "ElementPortion", "Side", "ElementNumber", "ElementQualifier", "SizeClass",
              "LifeStage", "ElementRemarks", "DateLastModified", "Barcode", "BiologyRemarks"]

rank_list = ['Kingdom', 'Phylum', 'Class', 'Order', 'Family']

HRP_collector_list = ['C.J. Campisano', 'W.H. Kimbel', 'T.K. Nalley', 'D.N. Reed', 'K.E. Reed', 'B.J. Schoville',
                      'A.E. Shapiro',  'HFS Student', 'HRP Team']

HRP_strat_member_list = ['Basal', 'Basal-Sidi Hakoma', 'Denen Dora', 'Denen Dora-Kada Hadar', 'Kada Hadar',
                         'Sidi Hakoma', 'Sidi Hakoma-Denen Dora']

taxon_dict = {'Kingdom': '', 'Phylum': '', 'Class': '', 'Order': '', 'Family': '',
              'Subfamily': '', 'Tribe': '', 'Genus': '', 'Species': ''}


# Helper Functions
def create_taxon_dictionary(brow):
    """
    Read a DB row and load into a dictionary
    :param brow:
    :return: Return a dictionary with taxonomic information
    """
    taxa = Taxon.objects.all()
    td = taxon_dict  # initiate a new taxon dictionary
    td['Kingdom'] = brow[biology_field_list.index('Kingdom')]
    td['Phylum'] = brow[biology_field_list.index('Phylum')]
    td['Class'] = brow[biology_field_list.index('Class')]
    td['Order'] = brow[biology_field_list.index('Order')]
    td['Family'] = brow[biology_field_list.index('Family')]
    td['Subfamily'] = brow[biology_field_list.index('Subfamily')]
    td['Tribe'] = brow[biology_field_list.index('Tribe')]
    td['Genus'] = brow[biology_field_list.index('Genus')]
    td['Trivial'] = brow[biology_field_list.index('SpecificEpithet')]
    td['Qualifier'] = brow[biology_field_list.index('IdentificationQualifier')]
    if td['Genus'] != '' and td['Trivial'] != '':
        td['Species'] = td['Genus'] + ' ' + ['Trivial']
    else:
        td['Species'] = ''

    return td


def get_taxon_name_rank(brow):
    """
    Function to look up a taxon object for a row in the Biology table
    :param brow:
    :return: Returns a tuple of (taxon_name, taxon_rank_name) for taxa of Genus or higher, e.g. ('Hominidae', 'Family')
    for species the function returns a tuple with the species binomen, e.g. ('Homo sapiens', 'SpecificEpithet')
    """
    taxon_list = brow[biology_field_list.index('Kingdom'):biology_field_list.index('SpecificEpithet')+1]
    name_index = max([i for i, x in enumerate(taxon_list) if x])
    taxon_name = taxon_list[name_index]
    taxon_rank_name = biology_field_list[name_index+2]
    if taxon_rank_name == 'SpecificEpithet':
        taxon_name = taxon_list[name_index-1]+' '+taxon_list[name_index]
    return [taxon_name, taxon_rank_name]


def get_matching_taxa(row):
    # get data from all taxon fields and collect them in a list
    # e.g. ["Animalia", "Chordata", "Mammalia", "Primates", "", "Hominidae", "", "", "Homo", "sapiens"]
    taxon_list = row[biology_field_list.index('Kingdom'):biology_field_list.index('SpecificEpithet')+1]
    # get taxon name and rank
    taxon_name, taxon_rank_name = get_taxon_name_rank(row)

    if taxon_rank_name == 'SpecificEpithet':
        genus_name, species_name = taxon_list[7:]
        taxon_queryset = Taxon.objects.filter(parent__name=genus_name).filter(name=species_name)

    else:
        taxon_queryset = Taxon.objects.filter(name=taxon_name).filter(rank__name=taxon_rank_name)

    return taxon_queryset


def get_matching_parent(brow):
    """
    For a row in the DB find the lowest matching taxon.
    :param brow:
    :return: Returns a taxon object, or None
    """
    taxon_list = brow[biology_field_list.index('Kingdom'):biology_field_list.index('SpecificEpithet')+1]
    taxon_object = None
    for taxon_name in reversed(taxon_list[:-1]):
        if Taxon.objects.filter(name=taxon_name).count() == 1:  # if there's a single match, done
            taxon_object = Taxon.objects.get(name=taxon_name)
            break
    return taxon_object


def create_taxon(brow):
    """
    Creates a new taxon for taxon names not encountered in the DB. Assumes ranks already exist.
    :param brow:
    :return:
    """
    taxon_name, taxon_rank_name = get_taxon_name_rank(brow)  # get taxon name and rank
    if taxon_name:
        print "Creating new %s: %s" %(taxon_rank_name, taxon_name)
        if taxon_rank_name == 'SpecificEpithet':
            # check genus and create if necessary
            genus_name = taxon_name.split()[0]  # taxon_name is binomen for rank SpecificEpithet, use split to get genus
            trivial_name = taxon_name.split()[1]  # get species name
            if not Taxon.objects.filter(name=genus_name).exists():  # If genus name not in DB create it.
                genus = Taxon(
                    name=genus_name,
                    parent=get_matching_parent(brow),
                    rank=TaxonRank.objects.get(name='Genus')
                )
            else:
                genus = Taxon(name=genus_name) # If genus name is in DB get it.
            if not Taxon.objects.filter(name=trivial_name, parent=genus).exists():
                Taxon(
                    name=trivial_name,
                    parent=genus,
                    rank=TaxonRank.objects.get(name='Species')
                )

        else:
            if not Taxon.objects.filter(name=taxon_name).exists:
                Taxon(
                    name=taxon_name,
                    parent=get_matching_parent(brow),
                    rank=TaxonRank.objects.get(name=taxon_rank_name)
                )


def transform_point(row):
    """
    Create a point object from UTM coordinates
    :param row:
    :return point_object:
    """
    pt = None
    # Fetch coordinates from row data
    occurrence_coordinates = row[biology_field_list.index('POINT_X'):biology_field_list.index('POINT_Y') + 1]
    occurrence_id = row[biology_field_list.index('CatalogNumberNumeric')]
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
    occurrence_id = row[biology_field_list.index('CatalogNumberNumeric')]
    date_recorded_string = row[biology_field_list.index('TimeStamp_')]

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
    dlm_string = row[biology_field_list.index('DateLastModified')]
    if dlm_string and dlm_string != '':
        dlm = datetime.datetime.strptime(dlm_string, '%m/%d/%y %H:%M:%S')
    return dlm


def convert_in_situ(row):
    """
    Convert in_situ floats to True/False, defaults to False
    :param row:
    :return:
    """
    in_situ_float = row[biology_field_list.index('Insitu')]
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
    ranked_float = row[biology_field_list.index('RankedUnit')]
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
    problem_integer = row[biology_field_list.index('Problem')]
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
    occurrence_id = row[biology_field_list.index('CatalogNumberNumeric')]  # read id from row CatalogNumberNumeric in row data
    if occurrence_id and occurrence_id > 0:  # if occurrence_id is not Null and positive
        if not Occurrence.objects.filter(id=occurrence_id).exists():  # if occurrence_id does not exist
            print "Warning, Occurrence id %s does not exist" % occurrence_id   # print warning
            return False  # return a failed validation
        else:  # if occurrence_id not null and does exist then add to dictionary
            row_dict['occurrence_id'] = occurrence_id
    else:
        print "Missing or non-positive occurrence ID!"
        return False

    # Validate Date Last Modified
    dlm = convert_date_last_modified(row)
    if not dlm:
        row_dict['date_last_modified'] = None

    elif dlm.year < 1970:
        print "Invalid date last modified %s for Occurrence %s" % (dlm, occurrence_id)
        return False 
    else:
        row_dict['date_last_modified'] = dlm

    # Validate taxon
    tq = get_matching_taxa(row)
    taxon_name_rank = get_taxon_name_rank(row)
    # taxon_list = row[field_list.index('Kingdom'):field_list.index('SpecificEpithet')+1]
    if not tq:
        create_taxon(row)
    else:
        print tq


def get_locality(row_dict):
    """
    Fetch the corresponding locality object for an occurrence and create a new one if necessary.
    :param row:
    :return locality_object:
    """

    # Validate and build locality text
    basis_of_record = row_dict['basis_of_record']
    collection_code = row_dict['collection_code']
    locality_number = row_dict['locality_number']
    sublocality = row_dict['sublocality']
    geom = row_dict['geom']
    locality_text = ''

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
                                sublocality=sublocality,
                                date_last_modified=datetime.datetime.now(),
                                geom=geom)

            locality.save()
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
    if occurrence_object.id != int(row[biology_field_list.index('CatalogNumberNumeric')]):
        print "Problem importing id for Occurrence %s" % occurrence_object.id
        return False
    if occurrence_object.basis_of_record != row[biology_field_list.index('BasisOfRecord')]:
        print "Problem importing basis of record %s for Occurrence %s" % \
              (occurrence_object.basis_of_record,
               occurrence_object.id)
        return False
    if occurrence_object.item_type != row[biology_field_list.index('ItemType')]:
        print "Problem importing item type %s for Occurrence %s" % \
              (occurrence_object.basis_of_record, occurrence_object.id)
        return False
    if occurrence_object.collection_code != row[biology_field_list.index('CollectionCode')]:
        print "Problem importing collection code %s for Occurrence %s" % \
              (occurrence_object.collection_code, occurrence_object.id)
        return False
    if occurrence_object.catalog_number() != row[biology_field_list.index('CatalogNumber')]:
        print "Catalog Number %s does not match CatalogNumber %s for Occurrence %s" % \
              (occurrence_object.catalog_number(), row[biology_field_list.index('CatalogNumber')], occurrence_object.id)
        return False
    if occurrence_object.item_scientific_name != row[biology_field_list.index('ItemScientificName')]:
        print "Item scientific name %s does not match ItemScientificName %s for Occurrence %s" % \
              (occurrence_object.item_scientific_name, row[biology_field_list.index('ItemScientificName')],
               occurrence_object.id)
        return False
    if occurrence_object.item_description != row[biology_field_list.index('ItemDescription')]:
        print "Item description %s does not match ItemDescription %s for Occurrence %s" % \
              (occurrence_object.item_description, row[biology_field_list.index('ItemDescription')], occurrence_object.id)
        return False
    if occurrence_object.collecting_method != row[biology_field_list.index('CollectingMethod')]:
        print "Collecting method %s does not match CollectingMethod %s for Occurrence %s" % \
              (occurrence_object.collecting_method, row[biology_field_list.index('CollectingMethod')], occurrence_object.id)
        return False
    if occurrence_object.collector != row[biology_field_list.index('Collector')]:
        print "Collector %s does not match Collector %s for Occurrence %s" % \
              (occurrence_object.collector, row[biology_field_list.index('Collector')], occurrence_object.id)
        return False
    if int(occurrence_object.year_collected) != int(row[biology_field_list.index('YearCollected')]):
        print "Year collected %s does not match YearCollected %s for Occurrence %s" % \
              (occurrence_object.year_collected, row[biology_field_list.index('YearCollected')], occurrence_object.id)
        return False
    if occurrence_object.analytical_unit != row[biology_field_list.index('AnalyticalUnit1')]:
        print "Analytical Unit %s does not match AnalyticalUnit1 %s for Occurrence %s" % \
              (occurrence_object.analytical_unit, row[biology_field_list.index('AnalyticalUnit1')], occurrence_object.id)
        return False
    if occurrence_object.barcode != row[biology_field_list.index('Barcode')]:
        print "Barcode %s does not match Barcode %s for Occurrence %s" % \
              (occurrence_object.barcode, row[biology_field_list.index('Barcode')], occurrence_object.id)
        return False
    else:
        return True


def main():
    import_count = 0
    collection_count = 0
    observation_count = 0
    row_count = 0
    print "Fetching a maximum of %s records \n" % record_limit
    for row in cursor.execute('SELECT * FROM Biology Where CatalogNumberNumeric=11378 LIMIT ?', record_limit):
        row_count += 1
        print str(row_count) + " "

        valid_row_dict = validate_row(row)

        # if valid_row_dict:
        #     basis_of_record = valid_row_dict['basis_of_record']
        #     if basis_of_record == 'Collection':
        #         locality = get_locality(valid_row_dict)
        #         new_occurrence = import_collection(valid_row_dict, locality)
        #         import_count += 1
        #         collection_count += 1
        #         if validate_new_record(new_occurrence, row):
        #             new_occurrence.save()
        #             # try:
        #             #     new_occurrence.save()
        #             # except:
        #             #     print "Problem saving occurrence %s" % new_occurrence.id
        #     elif basis_of_record == 'Observation':
        #         new_occurrence = import_observation(valid_row_dict)
        #         import_count += 1
        #         observation_count += 1
        #         if validate_new_record(new_occurrence, row):
        #             new_occurrence.save()
        # else:
        #     print "Invalid row for Occurrence %s " % row[field_list.index('CatalogNumberNumeric')]

    print "\nNumber of rows processed: %s \nNumber of records imported: %s" % (row_count, import_count)
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
