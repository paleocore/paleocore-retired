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
from update_taxonomy import id_test_list, occurrence_test_list


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


def get_taxon_from_scientific_name(scientific_name):
    """
    Function retrieves a taxon object from a colon delimited item_scientific_name string
    :param scientific_name: colon delimited item_scientific_name string, e.g. 'Rodentia:Muridae:Golunda gurai'
    :return: returns a taxon object.
    """
    clean_name = scientific_name.strip()  # remove leading or trailing spaces
    taxon = None  # initiate taxon return
    id_qualifier = None  # initiate identification_qualifier return

    # split colon delimited string into list e.g. Rodentia:Muridae to ['Rodentia', 'Muridae']
    taxon_name_list = re.split('\s|:|_|,', clean_name)  # split using space, colon, underscore or comma delimeters
    taxon_name_list_length = len(taxon_name_list)
    if taxon_name_list_length == 0:
        taxon = None
    if taxon_name_list_length >= 1:
        taxon_string = taxon_name_list[-1]
        try:
            taxon = Taxon.objects.get(name__exact=taxon_string)
        except MultipleObjectsReturned:
            parent = Taxon.objects.get(name__exact=taxon_name_list[-2])
            taxon = Taxon.objects.filter(name__exact=taxon_string).filter(parent=parent)
    return taxon


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
    taxon = Life.
    :param oi: occurrence instance
    :return: returns nothing.
    """

    if oi.item_type == 'Faunal':  # convert only faunal items to Biology
        # Intiate variables
        default_taxon = Taxon.objects.get(name__exact='Life')
        defaulat_identification_qualifier=IdentificationQualifier.objects.get(name="None")

        taxon = get_taxon_from_scientific_name(oi.item_scientific_name)

        try:
            taxon=Taxon.objects.get(name=oi.item_scientific_name.strip())  # try getting the taxon based on item sci name
        except ObjectDoesNotExist:
            try:
                taxon_name = oi.item_scientific_name.split(' ')[1]  # if no match try matching just the last word
                taxon = Taxon.objects.get(name=taxon_name)
            except ObjectDoesNotExist:
                return "Error: Cannot match taxonomic information for id:{} barcode:{}".format(oi.id, oi.barcode)
            except IndexError:
                try:
                    taxon = Taxon.objects.get(name=oi.item_scientific_name)
                except ObjectDoesNotExist:
                    taxon = Taxon.objects.get(name='Animalia')
        if len(oi.item_scientific_name.split(' ')) > 1:  # test if item sci name is 2 words or more
            id_qual_name = oi.item_scientific_name.split(' ')[0]  # take first element as the id qualifier
            try:
                id_qual = IdentificationQualifier.objects.get(name=id_qual_name)  # try to get the id qualifier
            except ObjectDoesNotExist:
                print "Error: Cannot match Identification qualifier info for id %s" % oi.id
        else:
            id_qual=IdentificationQualifier.objects.get(name="None")  # if item sci name is 1 word, assign none to id qual

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
    mlp_fossils = Occurrence.objects.filter(item_type__exact="Faunal").filter(basis_of_record__exact="FossilSpecimen")
    for f in mlp_fossils:
        try:
            mlpb = Biology.objects.get(pk=f.id)
            print "Occurence barcode:{} is already a Biology object.".format(f.barcode)
        except ObjectDoesNotExist:
            print "converting Occrrence with barcode:{} to Biology.".format(f.barcode)
            return occurrence2biology(f)


def find_unmatched_barcodes():
    mlp_fossils  = Occurrence.objects.filter(basis_of_record='FossilSpecimen')
    problem_list = []
    for f in mlp_fossils:
        if f.barcode != f.item_number:
            problem_list.append(f.barcode)
    return problem_list


def import_dg_updates():
    file_location = os.path.join('/', 'Users', 'reedd', 'Desktop', 'MLP_database_all.csv')
    dbfile = open(file_location)
    data = dbfile.readlines()
    dbfile.close()
    data_list = []
    index = 0
    for row in data[1:]:
        data_list.append(row[:-2].split(';'))  # split data by semicolon separators and remove line terminators
    for row in data_list:
        if row[2] == 'January2014':
            row[2] = 'January 2014'  # fix bad date format
    # remove duplicate entries
    unique_data_list = [list(x) for x in set(tuple(x) for x in data_list)]
    for row in unique_data_list:
        row.insert(0, index)  # add a row id starting at 0
        index += 1
    print 'Importing data from {}'.format(file_location)
    print 'Removing {} duplicate records from raw data list,'.format(len(data_list)-len(unique_data_list))
    return unique_data_list


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
            occurrence_obj = Occurrence.objects.get(catalog_number__exact=cleaned_catalog_number)
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
    result = Occurrence.objects.filter(geom__distance_lte=(pnt, Distance(m=1)))
    match_result = (False, None)
    if (len(result)) == 1:
        match_result = (True, result)
    elif len(result) >= 1:
        match_result = (False, result)
    elif len(result) == 0:
        match_result = (False, None)
    return match_result


def match(data_list):
    """
    Function to match Occurrence objects based on barcode or coordinates.
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
        cat_number_string = row[12]
        match_catalog_number_result = match_catalog_number(cat_number_string)  # try to match by catalog number
        if match_catalog_number_result[0]:  # if there is a successful match by catalog number ...
            match_tuple = (row, match_catalog_number_result[1])  # tuple with original row data and matched occur obj
            match_list.append(match_tuple)  # add the row data to the match list
        elif not match_catalog_number_result[0]:  # next try matching by coordinates
            coordinate_match_result = match_coordinates(row[16], row[17])
            if coordinate_match_result[0]:
                coordinate_match_tuple = (row, coordinate_match_result[1])
                coordinate_match_list.append(coordinate_match_tuple)
            elif not coordinate_match_result[0]:
                problem_tuple = (row, coordinate_match_result[1])
                problem_list.append(problem_tuple)
    print 'Matched {} records using catalog numbers'.format(len(match_list))
    print 'Matched {} records using coordinates'.format(len(coordinate_match_list))
    print 'There are {} remaining unmatched records\n'.format(len(problem_list))
    result_tuple = (match_list, coordinate_match_list, problem_list)
    return result_tuple


def display_match(match_tuple):
    row, obj = match_tuple[0], match_tuple[1]

    # row data
    id = row[0]
    label = row[1]
    collector = row[2]
    date = row[3]
    month = date.split(' ')[0]
    year = date.split(' ')[1]
    description = row[4]
    basis = row[5]
    sciname = row[6]
    highrank = row[7]
    ordfam = row[8]
    famtribe = row[9]
    gensp = row[10]
    uncert = row[11]
    catalog_number = row[12]
    dg_notes = row[13]
    northing = float(row[15])
    easting = float(row[14])
    longitude = float(row[16])
    latitude = float(row[17])
    notes = row[18]
    taxon_string = highrank+':'+ordfam+':'+famtribe+':'+gensp

    # object data
    omonth = calendar.month_name[obj.field_number.month]
    oyear = obj.field_number.year

    print '{:5}  {:8}  {:10}  {:10.1f} {:10.1f}  {:10.10f} {:10.10f}  {:20}  {:8}  {:4}  {:20}  {} {} {:10}'.format(id,
                                                                                catalog_number, basis,
                                                                                easting, northing, longitude, latitude,
                                                                                collector, month, year,
                                                                   description, taxon_string, uncert, notes)
    print '{:5}  {:8}  {:10}  {:10.1f} {:10.1f}  {:10.10f} {:10.10f}  {:20}  {:8}  {:4}  {:20}  {}\n'.format(obj.id, obj.catalog_number,
                                                                               obj.basis_of_record,
                                                                               obj.easting(), obj.northing(),
                                                                                obj.point_x(), obj.point_y(),
                                                                  obj.collector, omonth, oyear,
                                                                  obj.item_description, obj.item_scientific_name, obj.remarks)


def validate_matches(result_tuple):
    cat_matches = result_tuple[0]
    coord_matches = result_tuple[1]
    problem_matches = result_tuple[2]
    match_no = 1
    for p in cat_matches[0:10]:
        print 'Match {}'.format(match_no)
        match_no += 1
        display_match(p)



def main():
    udl = import_dg_updates()
    matches = match(udl)
    validate_matches(matches)



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


def test_match(list=occurrence_test_list):
    print 'Starting run on {} items in list'.format(len(list))
    count = 0
    full_match_count = 0
    coordinate_match_count = 0
    bad_match_count = 0
    for t in list:
        catno = t[0]
        lon = t[1]
        lat = t[2]
        cat_match_result = match_catalog_number(catno)
        coord_match_result = match_coordinates(lon, lat)
        if cat_match_result[0] and coord_match_result[0] and cat_match_result[1] == coord_match_result[1][0]:
            matched_object = cat_match_result[1]
            #print "{count}. Catalog number {catno} and coordinates {lon} {lat}, matched to occurrence object id:{id} barcode {barcode}".format(count=count, catno=catno, lon=lon, lat=lat, id=matched_object.id, barcode=matched_object.barcode)
            full_match_count += 1
        elif coord_match_result[0] and not cat_match_result[0]:
            matched_object = coord_match_result[1][0]
            #print "{} {} Remarks:{}".format(catno, matched_object.barcode, matched_object.remarks)
            coordinate_match_count += 1
        elif cat_match_result[0] and len(coord_match_result[1])>=2:
            matched_object = cat_match_result[1]
            if matched_object in coord_match_result[1]:
                #print "{} {} Remarks:{}".format(catno, matched_object.barcode, matched_object.remarks)
                coordinate_match_count += 1
        else:
            print "{}. Catalog number {} and coordinates {} {}, bad match.".format(count, catno, lon, lat)
            bad_match_count += 1
        count += 1
    print "Matches: {}\nCoordinate Matches: {}\nBad Matches: {}".format(full_match_count, coordinate_match_count, bad_match_count)


