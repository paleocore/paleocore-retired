from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from models import *
import unicodecsv


##########################
# Custom geo admin class #
##########################

class DGGeoAdmin(OSMGeoAdmin):
    """
    Modified Geographic Admin Class using Digital Globe basemaps
    GeoModelAdmin -> OSMGeoAdmin -> DGGeoAdmin
    """
    map_template = 'gis/admin/digital_globe.html'


###########
# Inlines #
###########

class ImagesInline(admin.TabularInline):
    model = Image
    extra = 0
    readonly_fields = ("id",)


class FilesInline(admin.TabularInline):
    model = File
    extra = 0
    readonly_fields = ("id",)


##############
# Fieldsets  #
##############

occurrence_fieldsets = (
    ('Record Details', {
        'fields': [('id', 'date_last_modified',),
                   ('basis_of_record',),
                   ('problem', 'problem_comment'),
                   ('remarks',)]
    }),  # occurrence_fieldsets[0]
    ('Find Details', {
        'fields': [('date_recorded', 'year_collected',),
                   ('barcode', 'catalog_number', 'field_number'),
                   ('item_type', 'item_scientific_name', 'item_description', 'item_count', 'image'),
                   ('collector', 'finder', 'collecting_method', ),
                   ('locality', 'item_number', 'item_part', 'cat_number'),
                   ('disposition', 'preparation_status'),
                   ('collection_remarks',)]
    }),  # occurrence_fieldsets[1]
    ('Geological Context', {
        'fields': [('stratigraphic_formation', 'stratigraphic_member',),
                   ('analytical_unit_1', 'analytical_unit_2', 'analytical_unit_3'),
                   ('analytical_unit_found', 'analytical_unit_likely', 'analytical_unit_simplified'),
                   ('in_situ', 'ranked'),
                   ('geology_remarks',)]
    }),  # occurrence_fieldsets[2]
    ('Location Details', {
        'fields': [('collection_code', 'drainage_region'),
                   ('georeference_remarks',),
                   ('longitude', 'latitude'),
                   ('easting', 'northing',),
                   ('geom',)]
    }),  # occurrence_fieldsets[3]
)

biology_additional_fieldsets = (
    ('Biology Details', {'fields': [
        ('life_stage', 'sex'),
    ]}),
    ('Elements', {'fields': [
        ('element', 'element_portion', 'side', 'element_number', 'element_modifier'),

        ('uli1', 'uli2', 'ulc', 'ulp3', 'ulp4', 'ulm1', 'ulm2', 'ulm3'),
        ('uri1', 'uri2', 'urc', 'urp3', 'urp4', 'urm1', 'urm2', 'urm3'),
        ('lri1', 'lri2', 'lrc', 'lrp3', 'lrp4', 'lrm1', 'lrm2', 'lrm3'),
        ('lli1', 'lli2', 'llc', 'llp3', 'llp4', 'llm1', 'llm2', 'llm3'),
        ('indet_incisor', 'indet_canine', 'indet_premolar', 'indet_molar', 'indet_tooth'), 'deciduous',
        ('element_remarks',)]
    }),
    ('Taxonomy', {'fields': [('taxon', 'identification_qualifier'),
                             ('identified_by', 'year_identified', 'type_status'),
                             ('taxonomy_remarks',)]
                  }),
    ('Taphonomic Details', {
        'fields': [('weathering', 'surface_modification')],
        # 'classes': ['collapse'],
    }),
)

biology_fieldsets = (
    occurrence_fieldsets[0],
    occurrence_fieldsets[1],
    biology_additional_fieldsets[0],
    biology_additional_fieldsets[1],
    biology_additional_fieldsets[2],
    occurrence_fieldsets[2],
    occurrence_fieldsets[3],
)

default_list_display = ['barcode', 'catalog_number', 'cat_number', 'collection_code', 'basis_of_record',
                        'item_type', 'collecting_method', 'collector', 'item_description', 'item_scientific_name',
                        'year_collected', 'in_situ', 'problem', 'disposition', 'easting', 'northing', 'thumbnail']

default_list_filter = ['basis_of_record', 'item_type', 'year_collected', 'collection_code', 'problem']

default_search_fields = ['id', 'item_scientific_name', 'item_description', 'barcode',
                         'collection_code', 'locality__locality_number', 'item_number', 'item_part', 'cat_number']

####################
# Occurrence Admin #
####################
occurrence_fieldsets_old = (
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


class OccurrenceAdmin(DGGeoAdmin):
    default_read_only_fields = Occurrence.method_fields_to_export()
    readonly_fields = ['id', 'date_last_modified'] + default_read_only_fields
    list_display = list(default_list_display)
    fieldsets = occurrence_fieldsets
    list_filter = list(default_list_filter)
    search_fields = list(default_search_fields)
    list_per_page = 500
    actions = ['create_data_csv', 'change_xy', 'get_nearest_locality']

    # Admin Actions
    # TODO update occurrence download
    def create_data_csv(self, request, queryset):
        """
        Export data to comma separated values
        :param request:
        :param queryset:
        :return: returns a comma delimited data file
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
            if locality.geom and locality.geom.contains(queryset[0].geom):
                matching_localities.append(str(locality.collection_code) + "-" + str(locality.locality_number))
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
            if locality.geom:
                locality_name = str(locality.collection_code) + "-" + str(locality.locality_number)
                #  how are units being dealt with here?
                locality_distance_from_point = locality.geom.distance(queryset[0].geom)
                distances.update({locality_name: locality_distance_from_point})
                closest_locality_key = min(distances, key=distances.get)
        self.message_user(request, "The point is %d meters from locality %s" % (distances.get(closest_locality_key),
                                                                                closest_locality_key))


#################
# Biology Admin #
#################

class BiologyAdmin(OccurrenceAdmin):
    list_display = list(default_list_display)
    list_display.insert(10, 'taxon')
    fieldsets = biology_fieldsets
    inlines = (ImagesInline, FilesInline)
    list_filter = list(default_list_filter)
    search_fields = list(default_search_fields)

    def create_data_csv(self, request, queryset):
        """
        Export biology data to csv format. Still some issues with unicode characters.
        :param request:
        :param queryset:
        :return:
        """
        response = HttpResponse(content_type='text/csv')  # declare the response type
        # TODO generalize project file name
        response['Content-Disposition'] = 'attachment; filename="HRP_Biology.csv"'  # declare the file name
        writer = unicodecsv.writer(response)  # open a .csv writer
        b = Biology()  # create an empty instance of a biology object

        # Fetch model field names. We need to account for data originating from tables, relations and methods.
        concrete_field_names = b.get_concrete_field_names()  # fetch a list of concrete field names
        method_field_names = b.method_fields_to_export()  # fetch a list for method field names

        fk_fields = [f for f in b._meta.get_fields() if f.is_relation]  # get a list of field objects
        fk_field_names = [f.name for f in fk_fields]  # fetch a list of foreign key field names

        # Concatenate to make a master field list
        field_names = concrete_field_names + method_field_names + fk_field_names
        writer.writerow(field_names)  # write column headers

        def get_fk_values(occurrence, fk):
            """
            Get the values associated with a foreign key relation
            :param occurrence:
            :param fk:
            :return:
            """
            qs = None
            return_string = ''
            try:
                qs = [obj for obj in getattr(occurrence, fk).all()]  # if fk is one to many try getting all objects
            except AttributeError:
                return_string = str(getattr(occurrence, fk))  # if one2one or many2one get single related value

            if qs:
                try:
                    # Getting the name of related objects requires calling the file or image object.
                    # This solution may break if relation is neither file nor image.
                    return_string = '|'.join([str(os.path.basename(p.image.name)) for p in qs])
                except AttributeError:
                    return_string = '|'.join([str(os.path.basename(p.file.name)) for p in qs])

            return return_string

        for occurrence in queryset:  # iterate through the occurrence instances selected in the admin
            # The next line uses string comprehension to build a list of values for each field.
            # All values are converted to strings.
            concrete_values = [getattr(occurrence, field) for field in concrete_field_names]
            # Create a list of values from method calls. Note the parenthesis after getattr in the list comprehension.
            method_values = [getattr(occurrence, method)() for method in method_field_names]
            # Create a list of values from related tables. One to many fields have related values concatenated in str.
            fk_values = [get_fk_values(occurrence, fk) for fk in fk_field_names]

            row_data = concrete_values + method_values + fk_values
            cleaned_row_data = ['' if i in [None, False, 'None', 'False'] else i for i in row_data]  # Replace ''.
            writer.writerow(cleaned_row_data)

        return response
    create_data_csv.short_description = 'Download Selected to .csv'


class ArchaeologyAdmin(OccurrenceAdmin):
    pass


class GeologyAdmin(OccurrenceAdmin):
    pass


###################
# Hydrology Admin #
###################
class HydrologyAdmin(DGGeoAdmin):
    list_display = ("id", "size")
    search_fields = ("id",)
    list_filter = ("size",)

    options = {
        'layers': ['google.terrain']
    }

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


class LocalityAdmin(DGGeoAdmin):
    list_display = ('id', 'collection_code', 'locality_number', 'sublocality')
    list_filter = ('collection_code',)
    readonly_fields = ('point_x', 'point_y', 'longitude', 'latitude', 'easting', 'northing')
    search_fields = ('locality,', 'id')
    fieldsets = locality_fieldsets
    options = {
        'layers': ['google.terrain']
    }


##########################
# Register Admin Classes #
##########################
admin.site.register(Occurrence, OccurrenceAdmin)
admin.site.register(Archaeology, ArchaeologyAdmin)
admin.site.register(Biology, BiologyAdmin)
admin.site.register(Geology, GeologyAdmin)
admin.site.register(Locality, LocalityAdmin)
admin.site.register(Hydrology, HydrologyAdmin)
