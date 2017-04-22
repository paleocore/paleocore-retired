__author__ = 'reedd'

from models import Occurrence, Biology
from taxonomy.models import Taxon, IdentificationQualifier
from django.core.files import File
from django.core.exceptions import MultipleObjectsReturned, ObjectDoesNotExist
import collections
from update_taxonomy import update_tuple_list
import os, re
from django.contrib.gis.geos import Point
from django.contrib.gis.measure import Distance
import calendar
from update_taxonomy import id_test_list, occurrence_test_list, cat_number_list


image_folder_path = "/Users/reedd/Documents/projects/PaleoCore/projects/Omo Mursi/Final_Import/omo_mursi_data/omo_mursi_data/"


def find_mlp_duplicate_biological_barcodes():
    all_mlp_collected_bio_occurrences = Occurrence.objects.filter(item_type__exact="Faunal").filter(basis_of_record__exact="FossilSpecimen")
    barcode_list = []
    duplicate_list = []
    for item in all_mlp_collected_bio_occurrences:
        try:
            barcode_list.append(item.barcode)
        except:
            print "Error"
    for item, count in collections.Counter(barcode_list).items():
                if count > 1:
                    duplicate_list.append(item)
    return duplicate_list


def find_mlp_duplicate_biological_catalog_numbers():
    all_mlp_collected_bio_occurrences = Occurrence.objects.filter(item_type__exact="Faunal").filter(basis_of_record__exact="FossilSpecimen")
    catalog_list = []
    duplicate_list = []
    for item in all_mlp_collected_bio_occurrences:
        try:
            catalog_list.append(item.catalog_number)
        except:
            print "Error"
    for item, count in collections.Counter(catalog_list).items():
                if count > 1:
                    duplicate_list.append(item)
    return duplicate_list


def find_mlp_missing_coordinates():
    all_mlp_occurrences = Occurrence.objects.all()
    missing_coordinates_id_list=[]
    for o in all_mlp_occurrences:
        try: o.geom.x
        except AttributeError:
            missing_coordinates_id_list.append(o.id)
    return missing_coordinates_id_list


def update_mlp_bio(updatelist=update_tuple_list):
    for o in updatelist:  # iterate through record tuples in list
        cat, tax, des = o  # unpack tuple values
        #print cat+" "+tax+" "+des  # do something with them

        try:
            occurrence = Occurrence.objects.get(catalog_number=cat)  # fetch the object with the catalog number
            occurrence.item_scientific_name = tax  # update item scientific name
            occurrence.item_description = des  # update item_description
            occurrence.save()  # save updates
        except ObjectDoesNotExist:  # handle if object is not found or is duplicate returning more than 1 match
            print "Does Not Exist or Duplicate:"+cat


def split_scientific_name(scientific_name):
    # split colon delimited string into list e.g. Rodentia:Muridae to ['Rodentia', 'Muridae']
    clean_name = scientific_name.strip()
    taxon_name_list = re.split('\s|:|_|,', clean_name)  # split using space, colon, underscore or comma delimeters
    taxon_name_list = [i for i in taxon_name_list if i != '']  # remove empty string resulting from extra spaces
    return clean_name, taxon_name_list


def get_identification_qualifier_from_scientific_name(scientific_name):
    clean_name, taxon_name_list = split_scientific_name(scientific_name)
    id_qual_name_list = [i.name for i in IdentificationQualifier.objects.all()]  # list of all IdQal names
    id_qual_name = [val for val in taxon_name_list if val in id_qual_name_list]  # get id_qual from taxon name list
    return IdentificationQualifier.objects.get(name__exact=id_qual_name)


def get_taxon_from_scientific_name(scientific_name):
    """
    Function retrieves a taxon object from a colon delimited item_scientific_name string
    :param scientific_name: colon delimited item_scientific_name string, e.g. 'Rodentia:Muridae:Golunda gurai'
    :return: returns a taxon object.
    """
    clean_name, taxon_name_list = split_scientific_name(scientific_name)
    taxon_name_list_length = len(taxon_name_list)
    taxon = Taxon.objects.get(name__exact='Life')  # default taxon
    id_qual_names = [i.name for i in IdentificationQualifier.objects.all()]  # get list of id qualifier names
    # If there is no scientific name, the taxon name list will be empty and default, 'Life' will be returned
    if taxon_name_list_length >= 1:  # if there is a scientific name...
        taxon_string = taxon_name_list[-1]  # get the last element
        try:
            # This method of getting the taxon risks matching the wrong species name
            # If the taxonomy table only inlcudes Mammalia:Suidae:Kolpochoeris afarensis
            # trying to match Mammalia:Primates:Australopithecus afarensis will succeed in error
            taxon = Taxon.objects.get(name__exact=taxon_string)
        except MultipleObjectsReturned:  # if multiple taxa match a species name
            index = -2
            parent_name = taxon_name_list[index]  # get the next name in the list
            while parent_name in id_qual_names:  # if the name is an id qualifier ignore it and advance to next item
                index -=1
                parent_name = taxon_name_list[index]  # get first parent item in list that is not an id qualifier
            parent = Taxon.objects.get(name__exact=parent_name)  # find the matching parent object
            taxon = Taxon.objects.filter(name__exact=taxon_string).filter(parent=parent)[0]
        except ObjectDoesNotExist:
            print "No taxon found to match {}".format(taxon_string)
    return taxon


def test_get_taxon_from_scientific_name(test_list=id_test_list):
    count=0
    for i in test_list:
        try:
            taxon = get_taxon_from_scientific_name(i)
            #print '{}, {} = {}'.format(count, i, taxon)
        except ObjectDoesNotExist:
            print '{}, {} = {}'.format(count, i, "Does Not Exist")
        except MultipleObjectsReturned:
            '{}, {} = {}'.format(count, i, 'Multiple Objects Returned')
        count+=1


def mlp_missing_biology_occurrences():
    """
    Function to identify occurrences that should also be biology but are missing from biology table
    :return: returns a list of occurrence object ids.
    """
    result_list = []  # Initialize result list
    # Biology occurrences should be all occurrences that are item_type "Faunal" or "Floral"
    biology_occurrences = Occurrence.objects.filter(item_type__in=['Faunal', 'Floral'])
    for occurrence in biology_occurrences:
        try: Biology.objects.get(occurrence_ptr_id__exact=occurrence.id)  # Find matching occurrence in bio
        except ObjectDoesNotExist:
            result_list.append(occurrence.id)
    return result_list


def occurrence2biology(oi):
    """
    Function to convert Occurrence instances to Biology instances. The new Biology instances are given a default
    taxon = Life, and identification qualifier = None.
    :param oi: occurrence instance
    :return: returns nothing.
    """

    if oi.item_type in ['Faunal', 'Floral']:  # convert only faunal or floral items to Biology
        # Intiate variables
        # taxon = get_taxon_from_scientific_name(oi.item_scientific_name)
        taxon = Taxon.objects.get(name__exact='Life')
        id_qual = IdentificationQualifier.objects.get(name__exact='None')
        # Create a new biology object
        new_biology = Biology(barcode=oi.barcode,
                                 item_type=oi.item_type,
                                 basis_of_record=oi.basis_of_record,
                                 collecting_method=oi.collecting_method,
                                 field_number=oi.field_number,
                                 taxon=taxon,
                                 identification_qualifier=id_qual,
                                 geom=oi.geom
                                 )
        for key in oi.__dict__.keys():
            new_biology.__dict__[key]=oi.__dict__[key]

        oi.delete()
        new_biology.save()


def update_occurrence2biology():
    mlp_fossils = Occurrence.objects.filter(item_type__in=["Faunal", "Floral"])
    print 'Processing {} Occurrence records'.format(mlp_fossils.count())
    count = 0
    existing = []
    converted = []
    for f in mlp_fossils:
        try:
            Biology.objects.get(pk=f.id)
            # print "{}. Occurence {} barcode: {} is already a Biology object.".format(count, f.id, f.barcode)
            existing.append(f.id)
        except ObjectDoesNotExist:
            print "{}. Converting Occrrence id: {} barcode: {} to Biology.".format(count, f.id, f.barcode)
            occurrence2biology(f)
            converted.append(f.id)
        count += 1
    print "Run completed. {} occurrences already existed. {} were converted.".format(len(existing), len(converted))
    return existing, converted


def find_unmatched_barcodes():
    mlp_fossils  = Occurrence.objects.filter(basis_of_record='FossilSpecimen')
    problem_list = []
    for f in mlp_fossils:
        if f.barcode != f.item_number:
            problem_list.append(f.barcode)
    return problem_list


def import_dg_updates(file_path='/Users/reedd/Documents/projects/PaleoCore/projects/mlp/data_cleaining_170412/DG_updates.txt'):
    """
    Function to read data from a delimited text file
    :return: list of header values, list of row data lists
    """
    dbfile = open(file_path)
    data = dbfile.readlines()
    dbfile.close()
    data_list = []
    header_list = data[0][:-2].split('|')  # list of column headers
    # populate data list
    for row in data[1:]:  # skip header row
        data_list.append(row[:-2].split('|'))  # remove newlines and split by delimiter
    print 'Importing data from {}'.format(file_path)
    return header_list, data_list


def show_duplicate_rows(data_list):
    print "\nChecking for duplicate records."
    unique_data_list = []
    duplicates = []
    data_list_set = [list(x) for x in set(tuple(x) for x in data_list)]
    for row in data_list:
        if row not in unique_data_list:
            unique_data_list.append(row)
        else:
            duplicates.append(row)
    rowcount = 0
    for row in unique_data_list:
        row.insert(0, rowcount)
        rowcount += 1
    print "Unique rows: {} ?= Row set: {}\nDuplicate rows: {}".format(len(unique_data_list), len(data_list_set), len(duplicates))
    return unique_data_list, duplicates, data_list_set


def set_data_list(data_list):
    return [list(x) for x in set(tuple(x) for x in data_list)]


def match_catalog_number(catalog_number_string):
    """
    Function to get occurrence objects from MLP catalog number in the form MLP-001
    the function splits the catalog number at the dash and strips leading zeros from the numberic portion of the
    catalog number. It then searches for a matching catalog number.
    :param catalog_number_string:
    :return:
    """
    cn_split = catalog_number_string.split('-')
    try:
        catalog_number_integer = int(cn_split[1])
        cleaned_catalog_number = 'MLP-' + str(catalog_number_integer)
        try:
            occurrence_obj = Biology.objects.get(catalog_number__exact=cleaned_catalog_number)
            return (True, occurrence_obj)
        except(ObjectDoesNotExist):
            return (False, catalog_number_string)
    except(IndexError):
        return (False, catalog_number_string)


def match_coordinates(longitude, latitude):
    """
    Function to match an Occurrence instance given coordinates
    :param longitude: in decimal degrees
    :param latitude: in decimal degrees
    :return: returns a two element tuple. The first element is True/False indicating whether there was a single match
    The second element in None by default, or a list of queryset of matches based on coordinates.
    """

    lon = float(longitude)
    lat = float(latitude)
    pnt = Point(lon, lat)
    result = Biology.objects.filter(geom__distance_lte=(pnt, Distance(m=1)))
    match_result = (False, None)
    if (len(result)) == 1:
        match_result = (True, result)
    elif len(result) >= 1:
        match_result = (False, result)
    elif len(result) == 0:
        match_result = (False, None)
    return match_result


def old_match(data_list):
    """
    Function to match Biology objects based on barcode or coordinates.
    :param data_list:
    :return:
    """
    counter = 0
    row_counter = 0
    match_list = []
    coordinate_match_list = []
    problem_list = []
    for row in data_list:
        row_counter += 1
        cat_number_string = row[0]
        match_catalog_number_result = match_catalog_number(cat_number_string)  # try to match by catalog number
        if match_catalog_number_result[0]:  # if there is a successful match by catalog number ...
            match_tuple = (row, match_catalog_number_result[1])  # tuple with original row data and matched occur obj
            match_list.append(match_tuple)  # add the row data to the match list
        elif not match_catalog_number_result[0]:  # next try matching by coordinates
            coordinate_match_result = match_coordinates(row[1], row[2])
            if coordinate_match_result[0]:
                coordinate_match_tuple = (row, coordinate_match_result[1])
                coordinate_match_list.append(coordinate_match_tuple)
            elif not coordinate_match_result[0]:
                problem_tuple = (row, coordinate_match_result[1])
                problem_list.append(problem_tuple)
    print 'Matched {} records using catalog numbers'.format(len(match_list))
    print 'Matched {} records using coordinates'.format(len(coordinate_match_list))
    print 'There are {} remaining unmatched records\n'.format(len(problem_list))

    return match_list, coordinate_match_list, problem_list


def match(data_list):
    print '\nMatching {} items in list'.format(len(data_list))
    full_match_list = []
    coordinate_match_list = []
    bad_match_list = []
    for row in data_list:
        catno = row[1]  # catalog number
        lon = row[2]  # longitude
        lat = row[3]  # latitude
        basis = row[7]  # basis of record
        cat_match_result = match_catalog_number(catno)
        coord_match_result = match_coordinates(lon, lat)
        # catalog match == coordinate match (only one object)
        if cat_match_result[0] and coord_match_result[0] and cat_match_result[1] == coord_match_result[1][0]:
            match_tuple = (row, cat_match_result[1])
            full_match_list.append(match_tuple)
        # coordinate match != catalog match, e.g. because there is an old or erroneous catalog number
        elif coord_match_result[0] and not cat_match_result[0]:
            match_tuple = (row, coord_match_result[1][0])
            coordinate_match_list.append(match_tuple)
        # catalog match in coordinate match list (more than one coordinate match)
        elif cat_match_result[0] and len(coord_match_result[1]) >= 2:
            matched_object = cat_match_result[1]
            if matched_object in coord_match_result[1]:
                match_tuple = (row, matched_object)
                coordinate_match_list.append(match_tuple)
        # No cat match and multiple coord matches, see if one is human observation
        elif (not cat_match_result[0]) and (not coord_match_result[0]) and basis == 'HumanObservation':
            if coord_match_result[1]:  # if there is a coordinate match result
                if len(coord_match_result[1]) >= 2:
                    matched_objects = [i for i in coord_match_result[1] if i.catalog_number == 'MLP-0']
                    if len(matched_objects) == 1:
                        match_tuple = (row, matched_objects[0])
                        coordinate_match_list.append(match_tuple)
        else:
            # print "{}. Catalog number {} and coordinates {} {}, bad match.".format(count, catno, lon, lat)
            match_tuple = (row, None)
            bad_match_list.append(match_tuple)
            #print match_tuple

    print "Matches: {}\nCoordinate Matches: {}\nBad Matches: {}".format(len(full_match_list),
                                                                        len(coordinate_match_list),
                                                                        len(bad_match_list))
    return full_match_list, coordinate_match_list, bad_match_list


def display_match(match_tuple):
    row, obj = match_tuple[0], match_tuple[1]

    # row data
    id = row[0]
    catalog_number = row[1]
    longitude = float(row[2])
    latitude = float(row[3])
    collector = row[4]
    date_list = row[5].split(' ')
    month = date_list[0]
    year = date_list[1]
    description = row[6]
    basis = row[7]
    sciname = row[8]
    taxon_string = row[11]
    id_qualifier = row[12]
    notes = row[10]
    taxon_obj = get_taxon_from_scientific_name(taxon_string)

    # object data
    omonth = calendar.month_name[obj.field_number.month]
    oyear = obj.field_number.year
    #                   row   id  catno  basis    lon        lat     coll   mo     yr   desc   sci   tname qual
    row_print_string = '{:3}:{:5}  {:8}  {:10}  {:10.10f} {:10.10f}  {:20}  {:8}  {:4}  {:30}  {:30}  {:30} {:5} {}\n'
    #                      bio:  id  catno  basis   lon         lat     coll   mo    yr    desc    sci  tname qual  rem
    object_print_string = '{:3}:{:5}  {:8}  {:10}  {:10.10f} {:10.10f}  {:20}  {:8}  {:4}  {:30}  {:30}  {:30} {:5} {}'

    print object_print_string.format('bio', obj.id, obj.catalog_number,
                                     obj.basis_of_record,
                                     obj.point_x(), obj.point_y(),
                                     obj.collector, omonth, oyear,
                                     obj.item_description, obj.item_scientific_name, obj.taxon,
                                     obj.identification_qualifier,
                                     obj.remarks)
    print row_print_string.format('row', id, catalog_number, basis,
                                  longitude, latitude,
                                  collector,
                                  month, year,
                                  description,
                                  taxon_string, taxon_obj,
                                  id_qualifier,
                                  notes)


def validate_matches(match_list, coordinate_match_list, problem_match_list):
    print "\n## Summary of Matches ##\n"
    match_no = 1

    print "\n Catalog Number Matches\n"
    for p in match_list:
        print 'Match {}'.format(match_no)
        match_no += 1
        display_match(p)




def main():
    #existing, converted = update_occurrence2biology()  # convert all faunal and floral occurrences to biology
    hl, dl = import_dg_updates()  # import header and data list from file
    udl, du, dls = show_duplicate_rows(dl)  # check for duplicates
    ml, cl, pl = match(udl)
    validate_matches(ml, cl, pl)







def find_duplicate_catalog_number(list):
    unique_list = []
    duplicate_list = []
    for i in list:
        if i not in unique_list:
            unique_list.append(i)
        else:
            duplicate_list.append(i)
    return unique_list, duplicate_list


def get_parent_name(taxon_name_list):
    index = -2
    parent_name = taxon_name_list[index]
    id_qual_names = [i.name for i in IdentificationQualifier.objects.all()]
    while parent_name in id_qual_names:
        index -= 1
        parent_name = taxon_name_list[index]
    return parent_name
