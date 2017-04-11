from django.contrib import admin
from models import *  # import database models from models.py
from django.forms import TextInput, Textarea  # import custom form widgets
from olwidget.admin import GeoModelAdmin
import base.admin
import unicodecsv
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse


###############
# Media Admin #
###############


class ImagesInline(admin.TabularInline):
    model = Image
    extra = 0
    readonly_fields = ("id",)


class FilesInline(admin.TabularInline):
    model = File
    extra = 0
    readonly_fields = ("id",)




##################
# Locality Admin #
##################
locality_fieldsets = (
    ('Record Details', {
        'fields': [('id',)]
    }),
    ('Item Details', {
        'fields': [('collection_code', 'locality_number', 'sublocality')]
    }),

    ('Occurrence Details', {
        'fields': [('description',)]
    }),
    ('Geological Context', {
        'fields': [('upper_limit_in_section', 'lower_limit_in_section'),
                   ('error_notes', 'notes')]
    }),

    ('Location Details', {
        'fields': [('longitude', 'latitude'),
                   ('easting', 'northing',),
                   ('geom',)]
    }),
)


class LocalityAdmin(GeoModelAdmin):
    list_display = ['id', 'collection_code']
    list_filter = ['collection_code']
    readonly_fields = ('point_x', 'point_y', 'longitude', 'latitude', 'easting', 'northing')
    search_fields = ('locality_number,', 'id')
    fieldsets = locality_fieldsets
    options = {
        'layers': ['google.terrain']
    }


####################
# Occurrence Admin #
####################
occurrence_fieldsets = (
    ('Record Details', {
        'fields': [('id', 'modified',)]
    }),
    ('Item Details', {
        'fields': [('catalog_number',),
                   ('date_recorded',),
                   ("collection_code", "locality", "item_number", "item_part")]
    }),

    ('Occurrence Details', {
        'fields': [('basis_of_record', 'item_type', 'disposition', 'preparation_status'),
                   ('collecting_method', 'collected_by', 'individual_count'),
                   ('remarks',)]
    }),

    ('Location Details', {
        'fields': [('longitude', 'latitude'),
                   ('easting', 'northing',),
                   ('geom',)]
    }),
)


class OccurrenceAdmin(base.admin.PaleoCoreOccurrenceAdmin):
    readonly_fields = ['id', 'point_x', 'point_y', 'easting', 'northing', 'modified', 'longitude', 'latitude']
    list_display = ['catalog_number', 'locality', 'basis_of_record', 'item_type', 'collecting_method', 'recorded_by',
                    'date_recorded', 'disposition', 'easting', 'northing']
    list_display_links = ['catalog_number', ]
    fieldsets = occurrence_fieldsets
    list_filter = ['basis_of_record', 'date_recorded', 'item_type', 'recorded_by', 'problem', 'disposition']
    search_fields = ['id', 'catalog_number']
    list_per_page = 500
    options = {
        'layers': ['google.terrain'], 'editable': False, 'default_lat': -122.00, 'default_lon': 38.00,
    }
    # Admin Actions
    actions = ['create_data_csv', 'change_xy', 'get_nearest_locality']

    def create_data_csv(self, request, queryset):
        """
        Export data to comma separated values
        :param request:
        :param queryset:
        :return:
        """
        response = HttpResponse(content_type='text/csv')  # declare the response type
        response['Content-Disposition'] = 'attachment; filename="HRP_Occurrences.csv"'  # declare the file name
        writer = unicodecsv.writer(response)  # open a .csv writer
        o = Occurrence()  # create an empty instance of an occurrence object

        occurrence_field_list = o.__dict__.keys()  # fetch the fields names from the instance dictionary
        try:  # try removing the state field from the list
            occurrence_field_list.remove('_state')  # remove the _state field
        except ValueError:  # raised if _state field is not in the dictionary list
            pass
        try:  # try removing the geom field from the list
            occurrence_field_list.remove('geom')
        except ValueError:  # raised if geom field is not in the dictionary list
            pass
        # Replace the geom field with new fields
        occurrence_field_list.append("longitude")  # add new fields for coordinates of the geom object
        occurrence_field_list.append("latitude")
        occurrence_field_list.append("easting")
        occurrence_field_list.append("northing")

        writer.writerow(occurrence_field_list)  # write column headers

        for occurrence in queryset:  # iterate through the occurrence instances selected in the admin
            # The next line uses string comprehension to build a list of values for each field
            occurrence_dict = occurrence.__dict__
            # Check that instance has geom
            try:
                occurrence_dict['longitude'] = occurrence.longitude()  # translate the occurrence geom object
                occurrence_dict['latitude'] = occurrence.latitude()
                occurrence_dict['easting'] = occurrence.easting()
                occurrence_dict['northing'] = occurrence.northing()
            except AttributeError:  # If no geom data exists write None to the dictionary
                occurrence_dict['longitude'] = None
                occurrence_dict['latitude'] = None
                occurrence_dict['easting'] = None
                occurrence_dict['northing'] = None

            # Next we use the field list to fetch the values from the dictionary.
            # Dictionaries do not have a reliable ordering. This code insures we get the values
            # in the same order as the field list.
            try:  # Try writing values for all keys listed in both the occurrence and biology tables
                writer.writerow([occurrence.__dict__.get(k) for k in occurrence_field_list])
            except ObjectDoesNotExist:  # Django specific exception
                writer.writerow([occurrence.__dict__.get(k) for k in occurrence_field_list])
            except AttributeError:  # Django specific exception
                writer.writerow([occurrence.__dict__.get(k) for k in occurrence_field_list])

        return response
    create_data_csv.short_description = "Download Selected to .csv"

    # admin action to get nearest locality
    def get_nearest_locality(self, request, queryset):
        """
        Find the locality polygon closest to a selected point
        :param request:
        :param queryset:
        :return:
        """
        # first make sure we are only dealing with one point
        if queryset.count() > 1:
            self.message_user(request, "You can't get the nearest locality for multiple points at once. "
                                       "Please select a single point.", level='error')
            return
        # check if point is within any localities
        matching_localities = []
        for locality in Locality.objects.all():
            if locality.geom.contains(queryset[0].geom):
                matching_localities.append(str(locality.collection_code) + "-" + str(locality.paleolocality_number))
        if matching_localities:
            # warning to user if the point is within multiple localities
            if len(matching_localities) > 1:
                self.message_user(request, "The point falls within multiple localities (localities %s). "
                                           "Please consider redefining your localities so they don't overlap."
                                  % str(matching_localities).replace("[", ""))
                return
            # Message user with the nearest locality
            self.message_user(request, "The point is in %s" % (matching_localities[0]))

        # if the point is not within any locality, get the nearest locality
        distances = {}  # dictionary which will contain {<localityString>:key} entries
        for locality in Locality.objects.all():
            locality_name = str(locality.collection_code) + "-" + str(locality.paleolocality_number)
            #  how are units being dealt with here?
            locality_distance_from_point = locality.geom.distance(queryset[0].geom)
            distances.update({locality_name: locality_distance_from_point})
            closest_locality_key = min(distances, key=distances.get)
        self.message_user(request, "The point is %d meters from locality %s" % (distances.get(closest_locality_key),
                                                                                closest_locality_key))


###################
# Taxonomy Admin  #
###################

class TaxonomyAdmin(admin.ModelAdmin):
    list_display = ("id", "rank", "taxon", "full_lineage")
    search_fields = ("taxon",)
    list_filter = ("rank",)
    readonly_fields = "full_lineage"

#################
# Biology Admin #
#################


biology_inline_fieldsets = (
    ('Taxonomy', {'fields': (('taxon',), 'id')}),
)

biology_element_fieldsets = (
    ('Elements', {'fields': (
        ('element', 'element_modifier'),
        ('uli1', 'uli2', 'ulc', 'ulp3', 'ulp4', 'ulm1', 'ulm2', 'ulm3'),
        ('uri1', 'uri2', 'urc', 'urp3', 'urp4', 'urm1', 'urm2', 'urm3'),
        ('lri1', 'lri2', 'lrc', 'lrp3', 'lrp4', 'lrm1', 'lrm2', 'lrm3'),
        ('lli1', 'lli2', 'llc', 'llp3', 'llp4', 'llm1', 'llm2', 'llm3'),
        ('indet_incisor', 'indet_canine', 'indet_premolar', 'indet_molar', 'indet_tooth'),
        'deciduous'
    )}),
)


biology_fieldsets = (
    ('Record Details', {
        'fields': [('id', 'date_last_modified',)]
    }),
    ('Item Details', {
        'fields': [('barcode', 'catalog_number',),
                   ('date_recorded', 'year_collected',),
                   ("collection_code", "locality", "item_number", "item_part")]
    }),

    ('Occurrence Details', {
        'fields': [('basis_of_record', 'item_type', 'disposition', 'preparation_status'),
                   ('collecting_method', 'finder', 'collector', 'individual_count'),
                   ('item_description', 'item_scientific_name', 'image'),
                   ('problem', 'problem_comment'),
                   ('remarks',)]
    }),
    biology_element_fieldsets[0],
    ('Geological Context', {
        'fields': [('stratigraphic_marker_upper', 'distance_from_upper'),
                   ('stratigraphic_marker_lower', 'distance_from_lower'),
                   ('stratigraphic_marker_found', 'distance_from_found'),
                   ('stratigraphic_marker_likely', 'distance_from_likely'),
                   ('analytical_unit', 'analytical_unit_2', 'analytical_unit_3'),
                   ('in_situ', 'ranked'),
                   ('stratigraphic_member',),
                   ('locality', 'drainage_region')]
    }),

    ('Location Details', {
        'fields': [('longitude', 'latitude'),
                   ('easting', 'northing',),
                   ('geom',)]
    }),
)


class BiologyInline(admin.TabularInline):
    model = Biology
    extra = 0
    readonly_fields = ("id",)
    fieldsets = biology_inline_fieldsets


class ElementInLine(admin.StackedInline):
    model = Biology
    extra = 0
    fieldsets = biology_element_fieldsets


class BiologyAdmin(OccurrenceAdmin):
    fieldsets = biology_fieldsets
    inlines = (BiologyInline, ImagesInline, FilesInline)
    list_filter = ['basis_of_record', 'date_recorded', 'recorded_by', 'problem', 'element']

    def create_data_csv(self, request, queryset):
        response = HttpResponse(content_type='text/csv')  # declare the response type
        response['Content-Disposition'] = 'attachment; filename="LGRP_Biology.csv"'  # declare the file name
        writer = unicodecsv.writer(response)  # open a .csv writer
        o = Occurrence()  # create an empty instance of an occurrence object
        b = Biology()  # create an empty instance of a biology object

        occurrence_field_list = o.__dict__.keys()  # fetch the fields names from the instance dictionary
        try:  # try removing the state field from the list
            occurrence_field_list.remove('_state')  # remove the _state field
        except ValueError:  # raised if _state field is not in the dictionary list
            pass
        try:  # try removing the geom field from the list
            occurrence_field_list.remove('geom')
        except ValueError:  # raised if geom field is not in the dictionary list
            pass
        # Replace the geom field with new fields
        occurrence_field_list.append("longitude")  # add new fields for coordinates of the geom object
        occurrence_field_list.append("latitude")
        occurrence_field_list.append("easting")
        occurrence_field_list.append("northing")

        biology_field_list = b.__dict__.keys()  # get biology fields
        try:  # try removing the state field
            biology_field_list.remove('_state')
        except ValueError:  # raised if _state field is not in the dictionary list
            pass

        #################################################################
        # For now this method handles all occurrences and corresponding #
        # data from the biology table for faunal occurrences.           #
        #################################################################
        writer.writerow(occurrence_field_list + biology_field_list)  # write column headers

        for occurrence in queryset:  # iterate through the occurrence instances selected in the admin
            # The next line uses string comprehension to build a list of values for each field
            occurrence_dict = occurrence.__dict__
            # Check that instance has geom
            try:
                occurrence_dict['longitude'] = occurrence.longitude()  # translate the occurrence geom object
                occurrence_dict['latitude'] = occurrence.latitude()
                occurrence_dict['easting'] = occurrence.easting()
                occurrence_dict['northing'] = occurrence.northing()
            except AttributeError:  # If no geom data exists write None to the dictionary
                occurrence_dict['longitude'] = None
                occurrence_dict['latitude'] = None
                occurrence_dict['easting'] = None
                occurrence_dict['northing'] = None

            # Next we use the field list to fetch the values from the dictionary.
            # Dictionaries do not have a reliable ordering. This code insures we get the values
            # in the same order as the field list.
            try:  # Try writing values for all keys listed in both the occurrence and biology tables
                writer.writerow([occurrence.__dict__.get(k) for k in occurrence_field_list] +
                                [occurrence.Biology.__dict__.get(k) for k in biology_field_list])
            except ObjectDoesNotExist:  # Django specific exception
                writer.writerow([occurrence.__dict__.get(k) for k in occurrence_field_list])
            except AttributeError:  # Django specific exception
                writer.writerow([occurrence.__dict__.get(k) for k in occurrence_field_list])

        return response
    create_data_csv.short_description = "Download Selected to .csv"


class ArchaeologyAdmin(OccurrenceAdmin):
    pass


class GeologyAdmin(OccurrenceAdmin):
    pass



##########################
# Register Admin Classes #
##########################

admin.site.register(Biology, BiologyAdmin)
admin.site.register(Archaeology, ArchaeologyAdmin)
admin.site.register(Geology, GeologyAdmin)
admin.site.register(Locality, LocalityAdmin)
admin.site.register(Occurrence, OccurrenceAdmin)
