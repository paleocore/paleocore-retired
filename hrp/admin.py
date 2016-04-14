from django.contrib import admin
from models import *  # import database models from models.py
from django.forms import TextInput, Textarea  # import custom form widgets
from django.http import HttpResponse
import unicodecsv
from django.core.exceptions import ObjectDoesNotExist
from olwidget.admin import GeoModelAdmin
import base.admin


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

#################
# Biology Admin #
#################

occurrence_fieldsets = (
    ('Curatorial', {
        'fields': [('barcode', 'catalog_number', 'id'),
                   ('field_number', 'year_collected', 'date_last_modified'),
                   ("collection_code", "paleolocality_number", "item_number", "item_part")]
    }),

    ('Occurrence Details', {
        'fields': [('basis_of_record', 'item_type', 'disposition', 'preparation_status'),
                   ('collecting_method', 'finder', 'collector', 'individual_count'),
                   ('item_description', 'item_scientific_name', 'image'),
                   ('problem', 'problem_comment'),
                   ('remarks',)],
    }),
    ('Provenience', {
        'fields': [('stratigraphic_marker_upper', 'distance_from_upper'),
                   ('stratigraphic_marker_lower', 'distance_from_lower'),
                   ('stratigraphic_marker_found', 'distance_from_found'),
                   ('stratigraphic_marker_likely', 'distance_from_likely'),
                   ('analytical_unit', 'analytical_unit_2', 'analytical_unit_3'),
                   ('in_situ', 'ranked'),
                   ('stratigraphic_member',),
                   ('locality',),
                   ('point_x', 'point_y'),
                   ('easting', 'northing',),
                   ('geom',)]
    }),
)

biology_fieldsets = (
    ('Taxonomy', {'fields': (('taxon',), 'id')
                  }),
)


class BiologyInline(admin.TabularInline):
    model = Biology
    extra = 0
    readonly_fields = ("id",)
    fieldsets = biology_fieldsets


class BiologyAdmin(admin.ModelAdmin):
    list_display = ("id", "collection_code", "paleolocality_number", "item_number", "item_part",
                    'stratigraphic_member', "barcode", 'basis_of_record', 'item_type', 'taxon', )
    list_filter = ("family",)
    readonly_fields = ("id",)
    fieldsets = biology_fieldsets

    # note: autonumber fields like id are not editable, and can't be added to fieldsets unless specified as read only.
    # also, any dynamically created fields (e.g. point_X) in models.py must be declared as read only to be included
    # in fieldset or fields
    readonly_fields = ("id", "field_number", "catalog_number", "date_last_modified")

    list_filter = ["basis_of_record", "year_collected", "stratigraphic_member", "collection_code", "item_type"]
    search_fields = ("id", "item_scientific_name", "barcode", "catalog_number")
    inlines = (BiologyInline, ImagesInline, FilesInline)
    fieldsets = occurrence_fieldsets
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'25'})},
        models.TextField: {'widget': Textarea(attrs={'rows': 4, 'cols': 40})},
    }
    list_per_page = 500  # show 500 records per page
    # change_form_template = "occurrence_change_form.html"
    actions = ["move_selected", "get_nearest_locality"]  # TODO clarify actions
    actions = ["get_nearest_locality", "create_data_csv"]


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


##################
# Locality Admin #
##################

class LocalityAdmin(GeoModelAdmin):
    list_display = ("collection_code", "paleolocality_number", "paleo_sublocality")
    list_filter = ("collection_code",)
    search_fields = ("paleolocality_number",)

    options = {
        'layers': ['google.terrain']
    }

####################
# Occurrence Admin #
####################


class OccurrenceAdmin(base.admin.PaleoCoreOccurrenceAdmin):
    actions = ['create_data_csv', 'change_xy', 'get_nearest_locality']
    readonly_fields = base.admin.default_read_only_fields+('photo',)
    list_display = base.admin.default_list_display+('thumbnail',)
    fieldsets = occurrence_fieldsets
    list_filter = base.admin.default_list_filter+['collection_code']

    options = {
        'layers': ['google.terrain'], 'editable': True, 'default_lat': -122.00, 'default_lon': 38.00,
    }

    # admin action to get nearest locality
    def get_nearest_locality(self, request, queryset):
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
    list_display = ("id", "rank", "taxon")
    search_fields = ("taxon",)
    list_filter = ("rank",)


##########################
# Register Admin Classes #
##########################

admin.site.register(Biology, BiologyAdmin)
admin.site.register(Hydrology, HydrologyAdmin)
admin.site.register(Locality, LocalityAdmin)
admin.site.register(Occurrence, OccurrenceAdmin)
