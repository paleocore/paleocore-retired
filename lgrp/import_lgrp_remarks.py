"""
This script includes functions to connect to a local sqlite DB, read specific data and write it to the paleocore DB
"""
# Import libraries
import sqlite3
import os.path
from lgrp.models import Biology, Occurrence
from django.core.exceptions import ObjectDoesNotExist

# Required imports for stand-alone django scripts
# http://stackoverflow.com/questions/25244631/models-arent-loaded-yet-error-while-populating-in-django-1-8-and-python-2-7-8
import django
django.setup()

# Global variables
record_limit = ('20000',)  # a limiter setting the maximum number of records to be read from the database, for debugging

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


def get_field_names(cursor):
    """
    Helper function to get a clean list of field names from a cursor's record set
    :param cursor: an active cursor
    :return: list of field names
    """
    # cursor.description returns a tuple of 7-element tuples where first element is field name and other
    # elements are None
    field_tuple = cursor.description
    return [e[0] for e in field_tuple]  # return a list with first element in each tuple, i.e. a list of field names


def import_lgrp_remarks():
    print("Opening connection to %s" % lgrpdb_path)
    connection = sqlite3.connect(lgrpdb_path)
    cursor = connection.cursor()  # connect to the LGRP sqlite DB

    # Fetch all Occurrence records and associated biology if present, get only records for which there is a comment
    sql_string = '''
SELECT Occurrence.CatalogNumberNumeric,
Occurrence.Barcode,
Occurrence.BasisOfRecord,
Occurrence.ItemType,
Occurrence.GeologyRemarks,
biology.ElementRemarks,
biology.TaxonomyRemarks,
biology.BiologyRemarks
FROM Occurrence LEFT JOIN biology ON (Occurrence.CatalogNumberNumeric = biology.CatalogNumberNumeric)
WHERE NOT (Occurrence.GeologyRemarks IS NULL AND biology.ElementRemarks IS NULL AND biology.TaxonomyRemarks
IS NULL AND biology.BiologyRemarks IS NULL);
'''

    rs = cursor.execute(sql_string)  # get a record set using the SQL string
    field_list = get_field_names(cursor)  # get a list of the field names in the record set
    row_count = 0  # initialize row count
    update_count = 0  # initialize update count

    # Iterate and update
    for row in rs:
        row_count += 1
        row_id = row[field_list.index('CatalogNumberNumeric')]  # get the occurrence id
        item_type = row[field_list.index('ItemType')]  # get the item type
        if row_count%100:
            "Processing ID {}".format(row_id)  # Send update every 100 rows as they are processed

        # Find matching Biology instance
        if item_type in ('Faunal', 'Floral'):
            try:
                instance = Biology.objects.get(pk=row_id)
                instance.geology_remarks = row[field_list.index('GeologyRemarks')]
                instance.element_remarks = row[field_list.index('ElementRemarks')]
                instance.taxonomy_remarks = row[field_list.index('TaxonomyRemarks')]
                instance.biology_remarks = row[field_list.index('BiologyRemarks')]
                instance.save()
                update_count += 1
            except ObjectDoesNotExist:
                print("No matching biology instance for ID {}".format(row_id))
        elif item_type in ('Artifactual', 'Geological'):
            try:
                instance = Occurrence.objects.get(pk=row_id)
                instance.geology_remarks = row[field_list.index('GeologyRemarks')]
                instance.save()
                update_count += 1
            except ObjectDoesNotExist:
                print("No matching Occurrence instance for ID {}".format(row_id))
        else:
            print("Error matching instance")


    #
    #     # iterate through columns in the row
    #     row_index = 0
    #     for i in row:
    #         if i and i > 0:  # if not None and positive
    #             column_name = field_list[row_index]  # look up column name from index
    #
    #             if column_name in excluded_fields:  # skip excluded fields
    #                 pass
    #             elif column_name in camel_case_fields:  # convert using dictionary and assign
    #                 setattr(biology_instance, camel_case_dictionary[column_name], True)
    #             else:  # convert string and assign
    #                 setattr(biology_instance, column_name.lower(), True)
    #         row_index += 1
    #
    #     biology_instance.save()
    #     update_count += 1

    print("Processed {} records, and updated {} biology objects".format(row_count, update_count))
    connection.close()  # close the connection


import_lgrp_remarks()
