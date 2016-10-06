from django.contrib import admin
from models import *  # import database models from models.py
from django.forms import TextInput, Textarea  # import custom form widgets
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
        'fields': [('barcode', 'catalog_number',),
                   ('date_recorded', 'year_collected',),
                   ("collection_code", "locality_number", "item_number", "item_part")]
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
                   ('drainage_region',)]
    }),

    ('Location Details', {
        'fields': [('longitude', 'latitude'),
                   ('easting', 'northing',),
                   ('geom',)]
    }),
)


class OccurrenceAdmin(base.admin.PaleoCoreOccurrenceAdmin):
    actions = ['create_data_csv', 'change_xy']
    readonly_fields = base.admin.default_read_only_fields+('photo', 'catalog_number', 'longitude', 'latitude')
    list_display = list(base.admin.default_list_display+('thumbnail',))
    field_number_index = list_display.index('field_number')
    list_display.pop(field_number_index)
    list_display.insert(2,'collection_code')
    list_display.insert(3, 'locality_number')
    list_display.insert(4, 'item_number')
    list_display.insert(5, 'item_part')
    fieldsets = occurrence_fieldsets
    list_filter = ['basis_of_record', 'item_type', 'year_collected', 'collector', 'collection_code', 'problem']
    search_fields = list(base.admin.default_search_fields)+['id']
    search_fields.pop(search_fields.index('catalog_number'))
    list_per_page = 500
    # options = {
    #     'layers': ['google.terrain'], 'editable': False, 'default_lat': -122.00, 'default_lon': 38.00,
    # }


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
                   ("collection_code", "locality_number", "item_number", "item_part")]
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
                   ('drainage_region',)]
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
    list_display = list(base.admin.default_list_display) + ['thumbnail', 'element']
    list_display.pop(list_display.index('item_type'))
    list_display.pop(list_display.index('field_number'))

    list_filter = ['basis_of_record', 'year_collected', 'collector', 'problem', 'element']


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
