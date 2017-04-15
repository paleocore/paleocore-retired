from django.contrib import admin
import base.admin  # import default PaleoCore admin classes
from models import Occurrence, Biology
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
import unicodecsv
from django.core.exceptions import ObjectDoesNotExist


class BiologyInline(admin.TabularInline):
    model = Biology
    extra = 0
    readonly_fields = ("id",)
    fieldsets = base.admin.default_biology_inline_fieldsets


class BiologyAdmin(base.admin.PaleoCoreBiologyAdmin):
    models = Biology


class OccurrenceAdmin(base.admin.PaleoCoreOccurrenceAdmin):
    actions = ["create_data_csv", "change_xy", "change_occurrence2biology"]
    readonly_fields = base.admin.default_read_only_fields+('photo',)
    list_display = base.admin.default_list_display+('thumbnail',)

    fieldsets = (
        ('Curatorial', {
            'fields': [('barcode', 'catalog_number', 'id'),
                       ('field_number', 'year_collected', 'date_last_modified'),
                       ('collection_code', 'item_number', 'item_part')]
        }),

        ('Occurrence Details', {
            'fields': [('basis_of_record', 'item_type', 'disposition', 'preparation_status'),
                       ('collecting_method', 'finder', 'collector', 'individual_count'),
                       ('item_description', 'item_scientific_name',),
                       ('problem', 'problem_comment'),
                       ('remarks',)],
            # 'classes': ['collapse']
        }),
        ('Photos', {
            'fields': [('photo', 'image')],
            # 'classes': ['collapse'],
        }),
        ('Taphonomic Details', {
            'fields': [('weathering', 'surface_modification')],
            # 'classes': ['collapse'],
        }),
        ('Provenience', {
            'fields': [('analytical_unit',),
                       ('in_situ',),
                       # The following fields are based on methods and must be included in the read only field list
                       ('point_x', 'point_y'),
                       ('easting', 'northing'),
                       ('geom',)],
            # 'classes': ['collapse'],
        })
    )

    # admin action to manually enter coordinates
    def change_xy(self, request, queryset):
        selected = request.POST.getlist(admin.ACTION_CHECKBOX_NAME)
        redirectURL = reverse("projects:mlp:mlp_change_xy")
        return HttpResponseRedirect(redirectURL + "?ids=%s" % (",".join(selected)))
    change_xy.short_description = "Manually change coordinates for a point"

    def change_occurrence2biology(selfself, request, queryset):
        selected = request.POST.getlist(admin.ACTION_CHECKBOX_NAME)
        redirectURL = reverse("projects:mlp:mlp_occurrence2biology")
        return HttpResponseRedirect(redirectURL + "?ids=%s" % (",".join(selected)))
    change_occurrence2biology.short_description = "Change Occurrence to Biology"



    # admin action to download data in csv format
    def create_data_csv(self, request, queryset):
        response = HttpResponse(content_type='text/csv')  # declare the response type
        response['Content-Disposition'] = 'attachment; filename="MLP_data.csv"'  # declare the file name
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
        # Replace the geom field with two new fields
        occurrence_field_list.append("point_x")  # add new fields for coordinates of the geom object
        occurrence_field_list.append("point_y")

        biology_field_list = b.__dict__.keys()  # get biology fields
        try:  # try removing the state field
            biology_field_list.remove('_state')
        except ValueError:  # raised if _state field is not in the dictionary list
            pass

        #################################################################
        # For now this method handles all occurrences and corresponding #
        # data from the biology table for faunal occurrences.           #
        #################################################################
        writer.writerow(occurrence_field_list+biology_field_list)  # write column headers

        for occurrence in queryset:  # iterate through the occurrence instances selected in the admin
            # The next line uses string comprehension to build a list of values for each field
            occurrence_dict = occurrence.__dict__
            # Check that instance has geom
            try:
                occurrence_dict['point_x'] = occurrence.geom.get_x()  # translate the occurrence geom object
                occurrence_dict['point_y'] = occurrence.geom.get_y()
            except AttributeError:  # If no geom data exists write None to the dictionary
                occurrence_dict['point_x'] = None
                occurrence_dict['point_y'] = None

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

############################
#  Register Admin Classes  #
############################
admin.site.register(Occurrence, OccurrenceAdmin)
admin.site.register(Biology, BiologyAdmin)