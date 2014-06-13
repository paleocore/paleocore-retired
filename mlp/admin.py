from django.contrib import admin
from models import Occurrence, Biology
from django.forms import TextInput, Textarea  # import custom form widgets
from django.contrib.gis.db import models
from django.http import HttpResponse
import unicodecsv
from django.core.exceptions import ObjectDoesNotExist

# Register your models here.
###################
## Biology Admin ##
###################

biology_fieldsets = (
    (None, {'fields':(('occurrence',))}),
    ('Element', {'fields':(('side',))}),
('Taxonomy', {
'fields': (('tax_class',),('tax_order',),('family',),('subfamily',),('tribe',),('genus','specificepithet'),("id"))
}),
)


class BiologyInline(admin.TabularInline):
    model = Biology
    extra = 0
    readonly_fields = ("id",)
    fieldsets = biology_fieldsets


class BiologyAdmin(admin.ModelAdmin):
    list_display = ("id", "side", "occurrence", "tax_class","tax_order","family","subfamily","tribe","genus","specificepithet","lowest_level_identification")
    list_filter = ("family", "side")
    search_fields = ("lowest_level_identification",)
    readonly_fields = ("id",)
    fieldsets = biology_fieldsets

######################
## Occurrence Admin ##
######################

occurrence_fieldsets =(
    ('Curatorial', {
        'fields': (('barcode', 'catalog_number'),
                   ('id', 'field_number', 'year_collected', 'date_last_modified'),
                   ("collection_code", "item_number", "item_part"))
    }),

    ('Occurrence Details', {
        'fields': (('basis_of_record', 'item_type', 'disposition', 'preparation_status'),
                   ('collecting_method', 'finder', 'collector', 'individual_count'),
                   ('item_description', 'item_scientific_name', 'image'),
                   ('problem', 'problem_comment'),
                   ('remarks'))
    }),
    ('Taphonomic Details', {
        'fields': (
            ('weathering', 'surface_modification')
        )
    }),
    ('Provenience', {
        'fields': (('analytical_unit',),
                   ('in_situ', 'ranked'),
                   ('point_X', 'point_Y'),
                   ('geom'))
    })
)


class OccurrenceAdmin(admin.ModelAdmin):
    list_display = ('id', 'catalog_number', 'barcode', 'basis_of_record', 'item_type', 'collecting_method',
                    'collector', 'item_scientific_name', 'item_description', 'point_X', 'point_Y', 'year_collected',
                    'field_number', 'date_last_modified', 'in_situ', 'problem')

    """
    Autonumber fields like id are not editable, and can't be added to fieldsets unless specified as read only.
    also, any dynamically created fields (e.g. point_X) in models.py must be declared as read only to be included in
    fieldset or fields
    """
    readonly_fields = ('id', 'field_number', 'point_X', 'point_Y', 'date_last_modified')
    list_editable = ['problem']

    list_filter = ['basis_of_record', 'year_collected', 'item_type', 'collector', 'problem']
    search_fields = ('id', 'item_scientific_name', 'item_description', 'barcode', 'catalog_number')
    inlines = [BiologyInline, ]
    fieldsets = occurrence_fieldsets
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '25'})},
        models.TextField: {'widget': Textarea(attrs={'rows': 4, 'cols': 40})},
    }

    # Set pagination to show 500 entries per page
    list_per_page = 1000

    actions = ["create_data_csv"]
    #admin action to download data in csv format
    def create_data_csv(self, request, queryset):
        response = HttpResponse(content_type='text/csv')  # declare the response type
        response['Content-Disposition'] = 'attachment; filename="MLP_data.csv"'  # declare the file name
        writer = unicodecsv.writer(response)  # open a .csv writer
        o = Occurrence()  # create an empty instance of an occurrence object
        b = Biology()  # create an empty instance of a biology object

        occurrence_fields = o.__dict__.keys()  # fetch the fields names from the instance dictionary
        try:  # try removing the state field
            occurrence_fields.remove('_state')  # remove the _state field
        except ValueError:  # raised if _state field is not in the dictionary list
            pass

        biology_fields = b.__dict__.keys()  # get biology fields
        try:  # try removing the state field
            biology_fields.remove('_state')
        except ValueError:  # raised if _state field is not in the dictionary list
            pass

        """
        For now this method handles all occurrences and corresponding
        data from the biology table for faunal occurrences.
        """
        writer.writerow(occurrence_fields+biology_fields)  # fetch field names and write to the first row

        for occurrence in queryset.all():  # iterate through the occurrence instances selected in the admin
            occurrence_values = [occurrence.__dict__.get(k) for k in occurrence_fields]

            try:  # Try writieng values for all keys listed in both the occurrence and biology tables
                writer.writerow([occurrence.__dict__.get(k) for k in occurrence_fields] +
                                [occurrence.Biology.__dict__.get(k) for k in biology_fields])
            except ObjectDoesNotExist:  # Django specific exception
                writer.writerow([occurrence.__dict__.get(k) for k in occurrence_fields])
            except AttributeError:  # Django specific exception
                writer.writerow([occurrence.__dict__.get(k) for k in occurrence_fields])

        return response

    create_data_csv.short_description = "Download Selected to .csv"

############################
## Register Admin Classes ##
############################
admin.site.register(Occurrence, OccurrenceAdmin)
admin.site.register(Biology, BiologyAdmin)
