from django.contrib import admin
from models import *  # import database models from models.py
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from olwidget.admin import GeoModelAdmin
import base.admin
import unicodecsv

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


###################
# Hydrology Admin #
###################
class HydrologyAdmin(GeoModelAdmin):
    list_display = ("id", "size")
    search_fields = ("id",)
    list_filter = ("size",)

    options = {
        'layers': ['google.terrain']
    }


####################
# Occurrence Admin #
####################
occurrence_fieldsets = (
    ('Record Details', {
        'fields': [('id', 'date_last_modified',)]
    }),
    ('Item Details', {
        'fields': [('barcode', 'catalog_number'),
                   ('date_recorded', 'year_collected',),
                   ('collection_code', 'locality_number', 'item_number', 'item_part'),
                   ('collection_remarks',)]
    }),

    ('Occurrence Details', {
        'fields': [('basis_of_record', 'item_type', 'disposition', 'preparation_status'),
                   ('collecting_method', 'finder', 'collector', 'individual_count'),
                   ('item_description', 'item_scientific_name', 'image'),
                   ('problem', 'problem_comment'),
                   ('remarks',)]
    }),
    ('Geological Context', {
        'fields': [('stratigraphic_marker_upper', 'distance_from_upper'),
                   ('stratigraphic_marker_lower', 'distance_from_lower'),
                   ('stratigraphic_marker_found', 'distance_from_found'),
                   ('stratigraphic_marker_likely', 'distance_from_likely'),
                   ('analytical_unit_1', 'analytical_unit_2', 'analytical_unit_3'),
                   ('analytical_unit_found', 'analytical_unit_likely', 'analytical_unit_simplified'),
                   ('in_situ', 'ranked'),
                   ('stratigraphic_member',),
                   ('drainage_region',),
                   ('geology_remarks',)]
    }),

    ('Location Details', {
        'fields': [('georeference_remarks',),
                   ('longitude', 'latitude'),
                   ('easting', 'northing',),
                   ('geom',)]
    }),
)


class OccurrenceAdmin(base.admin.PaleoCoreOccurrenceAdmin):
    actions = ['create_data_csv', 'change_xy']
    readonly_fields = base.admin.default_read_only_fields+('photo', 'catalog_number',
                                                           'longitude', 'latitude')
    # list_display = list(base.admin.default_list_display+('thumbnail',))
    list_display = ['barcode', 'catalog_number', 'old_cat_number', 'collection_code', 'basis_of_record',
                    'item_type', 'item_scientific_name', 'item_description', 'collector', 'year_collected',
                    'collecting_method', 'thumbnail', 'date_last_modified', 'easting', 'northing']
    fieldsets = occurrence_fieldsets
    list_filter = ['basis_of_record', 'item_type', 'year_collected', 'collector', 'collection_code', 'problem',
                   'weathering']
    additional_search_fields = ['id', 'collection_code', 'locality_number', 'item_number', 'item_part', 'old_cat_number']
    search_fields = list(base.admin.default_search_fields)+additional_search_fields
    search_fields.pop(search_fields.index('catalog_number'))  # can't search on methods
    list_per_page = 500
    # options = {
    #     'layers': ['google.terrain'], 'editable': False, 'default_lat': -122.00, 'default_lon': 38.00,
    # }

    # admin action to download data in csv format
    def create_data_csv(self, request, queryset):
        response = HttpResponse(content_type='text/csv')  # declare the response type
        response['Content-Disposition'] = 'attachment; filename="LGRP_Occurrences.csv"'  # declare the file name
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
        occurrence_field_list.append('longitude')  # add new fields for coordinates of the geom object
        occurrence_field_list.append('latitude')
        occurrence_field_list.append('easting')
        occurrence_field_list.append('northing')

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

    create_data_csv.short_description = 'Download Selected to .csv'


###################
# Taxonomy Admin  #
###################

class TaxonomyAdmin(admin.ModelAdmin):
    list_display = ('id', 'rank', 'taxon', 'full_lineage')
    search_fields = ('taxon',)
    list_filter = ('rank',)
    readonly_fields = 'full_lineage'

#################
# Biology Admin #
#################


biology_inline_fieldsets = (
    ('Taxonomy', {'fields': [('taxon', 'identification_qualifier'),
                             ('identified_by', 'year_identified', 'type_status'),
                             ('taxonomy_remarks',)]
                  }),
)

biology_element_fieldsets = (
    ('Elements', {'fields': (
        ('element', 'element_portion', 'side', 'element_number', 'element_modifier'),
        ('uli1', 'uli2', 'ulc', 'ulp3', 'ulp4', 'ulm1', 'ulm2', 'ulm3'),
        ('uri1', 'uri2', 'urc', 'urp3', 'urp4', 'urm1', 'urm2', 'urm3'),
        ('lri1', 'lri2', 'lrc', 'lrp3', 'lrp4', 'lrm1', 'lrm2', 'lrm3'),
        ('lli1', 'lli2', 'llc', 'llp3', 'llp4', 'llm1', 'llm2', 'llm3'),
        ('indet_incisor', 'indet_canine', 'indet_premolar', 'indet_molar', 'indet_tooth'), 'deciduous',
        ('element_remarks',)),

    }),
)


biology_fieldsets = (
    ('Record Details', {
        'fields': [('id', 'date_last_modified',)]
    }),
    ('Item Details', {
        'fields': [('barcode', 'catalog_number',),
                   ('date_recorded', 'year_collected',),
                   ('collection_code', 'locality_number', 'item_number', 'item_part'),
                   ('collection_remarks',)]
    }),

    ('Occurrence Details', {
        'fields': [('basis_of_record', 'item_type', 'disposition', 'preparation_status'),
                   ('collecting_method', 'finder', 'collector', 'individual_count'),
                   ('item_description', 'item_scientific_name', 'image'),
                   ('problem', 'problem_comment'),
                   ('remarks',),
                   ('sex', 'life_stage'),
                   ('biology_remarks',)
                   ]
    }),
    biology_element_fieldsets[0],
    ('Taphonomic Details', {
        'fields': [('weathering', 'surface_modification')],
        # 'classes': ['collapse'],
    }),
    ('Geological Context', {
        'fields': [('stratigraphic_marker_upper', 'distance_from_upper'),
                   ('stratigraphic_marker_lower', 'distance_from_lower'),
                   ('stratigraphic_marker_found', 'distance_from_found'),
                   ('stratigraphic_marker_likely', 'distance_from_likely'),
                   ('analytical_unit_1', 'analytical_unit_2', 'analytical_unit_3'),
                   ('analytical_unit_found', 'analytical_unit_likely', 'analytical_unit_simplified'),
                   ('in_situ', 'ranked'),
                   ('stratigraphic_member',),
                   ('drainage_region',),
                   ('geology_remarks',)]
    }),

    ('Location Details', {
        'fields': [('georeference_remarks',),
                   ('longitude', 'latitude'),
                   ('easting', 'northing',),
                   ('geom',)]
    }),
)


class BiologyInline(admin.TabularInline):
    model = Biology
    extra = 0
    readonly_fields = ('id',)
    fieldsets = biology_inline_fieldsets


class ElementInLine(admin.StackedInline):
    model = Biology
    extra = 0
    fieldsets = biology_element_fieldsets


class BiologyAdmin(OccurrenceAdmin):
    fieldsets = biology_fieldsets
    inlines = (BiologyInline, ImagesInline, FilesInline)
    list_filter = ['basis_of_record', 'year_collected', 'collector', 'collection_code', 'problem', 'element', 'weathering']

    def create_data_csv(self, request, queryset):
        response = HttpResponse(content_type='text/csv')  # declare the response type
        response['Content-Disposition'] = 'attachment; filename="LGRP_Biology.csv"'  # declare the file name
        writer = unicodecsv.writer(response)  # open a .csv writer
        b = Biology()  # create an empty instance of a biology object

        field_list = b._meta.get_fields()  # fetch the fields from the instance meta information
        field_names = [f.name for f in field_list]  # iterate through field objects and get field names
        try:  # try removing the state field from the list
            field_names.remove('_state')  # remove the _state field
        except ValueError:  # raised if _state field is not in the dictionary list
            pass
        try:  # try removing the geom field from the list
            field_names.remove('geom')
        except ValueError:  # raised if geom field is not in the dictionary list
            pass
        # Replace the geom field with new fields
        field_names.append('longitude')  # add new fields for coordinates of the geom object
        field_names.append('latitude')
        field_names.append('easting')
        field_names.append('northing')
        field_names.insert(field_names.index('taxon'), 'taxon_id')

        writer.writerow(field_names)  # write column headers

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

            try:  # Try writing the taxon name in the taxon field
                occurrence_dict['taxon'] = occurrence.taxon.name
                occurrence_dict['taxon_id'] = occurrence.taxon.id
            except ObjectDoesNotExist:
                occurrence_dict['taxon'] = None
                occurrence_dict['taxon_id'] = None
            except AttributeError:  # Django specific exception
                occurrence_dict['taxon'] = None
                occurrence_dict['taxon_id'] = None



            # Next we use the field list to fetch the values from the dictionary.
            # Dictionaries do not have a reliable ordering. This code insures we get the values
            # in the same order as the field list.
            try:  # Try writing values for all keys listed in both the occurrence and biology tables
                writer.writerow([occurrence_dict.get(k) for k in field_names])
            except ObjectDoesNotExist:  # Django specific exception
                writer.writerow([occurrence_dict.get(k) for k in field_names])
            except AttributeError:  # Django specific exception
                writer.writerow([occurrence_dict.get(k) for k in field_names])



        return response

    create_data_csv.short_description = 'Download Selected to .csv'


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
admin.site.register(Hydrology, HydrologyAdmin)
admin.site.register(Occurrence, OccurrenceAdmin)
