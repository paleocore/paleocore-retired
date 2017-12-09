from django.contrib import admin
from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
import unicodecsv

import base.admin  # import default PaleoCore admin classes
from models import Occurrence, Biology
import os
import barcode


class BiologyInline(admin.TabularInline):
    model = Biology
    extra = 0
    readonly_fields = ("id",)
    fieldsets = base.admin.default_biology_inline_fieldsets


class OccurrenceAdmin(base.admin.PaleoCoreOccurrenceAdmin):
    actions = ["change_xy", "change_occurrence2biology"]
    readonly_fields = base.admin.default_read_only_fields+('photo',)  # defaults plus photo
    list_display = base.admin.default_list_display+('thumbnail',)  # defaults plus thumbnail
    list_filter = ['basis_of_record', 'item_type', 'field_season',
                   'field_number', 'collector', 'problem', 'disposition']

    fieldsets = [
        ('Curatorial', {
            'fields': [('barcode', 'catalog_number', 'id'),
                       ('field_number', 'year_collected', 'field_season', 'date_last_modified'),
                       ('collection_code', 'item_number', 'item_part')]
        }),
        ('Occurrence Details', {
            'fields': [('basis_of_record', 'item_type', 'disposition', 'preparation_status'),
                       ('collector', 'finder', 'collecting_method', 'individual_count'),
                       ('item_description', 'item_scientific_name',),
                       ('problem', 'problem_comment'),
                       ('remarks',)],
            'classes': ['collapse']
        }),
        ('Photos', {
            'fields': [('photo', 'image')],
            'classes': ['collapse'],
        }),
        ('Taphonomic Details', {
            'fields': [('weathering', 'surface_modification')],
            'classes': ['collapse'],
        }),
        ('Provenience', {
            'fields': [('analytical_unit',),
                       ('in_situ',),
                       # The following fields are based on methods and must be included in the read only field list
                       ('point_x', 'point_y'),
                       ('easting', 'northing'),
                       ('geom',)],
            'classes': ['collapse'],
        })
    ]

    # Admin Actions
    # admin action to manually enter coordinates
    def change_xy(self, request, queryset):
        selected = request.POST.getlist(admin.ACTION_CHECKBOX_NAME)
        redirect_url = reverse("projects:mlp:mlp_change_xy")
        return HttpResponseRedirect(redirect_url + "?ids=%s" % (",".join(selected)))
    change_xy.short_description = "Manually change coordinates for a point"

    def change_occurrence2biology(self, request, queryset):
        selected = request.POST.getlist(admin.ACTION_CHECKBOX_NAME)
        redirect_url = reverse("projects:mlp:mlp_occurrence2biology")
        return HttpResponseRedirect(redirect_url + "?ids=%s" % (",".join(selected)))
    change_occurrence2biology.short_description = "Change Occurrence to Biology"

    # admin action to download data in csv format
    def create_data_csv_old(self, request, queryset):
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
    create_data_csv_old.short_description = "Download Selected to .csv"


class BiologyAdmin(OccurrenceAdmin):
    actions = ["change_xy", "change_occurrence2biology", "create_data_csv", "generate_specimen_labels",
               "generate_barcode"]
    biology_fieldsets = list(OccurrenceAdmin.fieldsets)  # creates a separate copy of the fielset list
    taxonomy_fieldsets = ('Identification', {'fields': [('taxon', 'identification_qualifier', 'identified_by')]})
    element_fieldsets = ('Detailed Description', {'fields': [('element', 'element_modifier')]})
    biology_fieldsets.insert(2, taxonomy_fieldsets)
    biology_fieldsets.insert(3, element_fieldsets)
    fieldsets = biology_fieldsets

    def create_data_csv(self, request, queryset):
        """
        Export data to csv format. Still some issues with unicode characters.
        :param request:
        :param queryset:
        :return:
        """
        response = HttpResponse(content_type='text/csv')  # declare the response type
        response['Content-Disposition'] = 'attachment; filename="MLP_Biology.csv"'  # declare the file name
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

    def generate_specimen_labels(self, request, queryset):
        """
        Export a text report with biology specimen data formatted for labels
        :param queryset:
        :param request:
        :return:
        """
        content = ""
        for b in queryset:
            specimen_data = "Mille-Logya Project\n{catalog_number}\n{date_collected}\n{sci_name}\n" \
                            "{description}\n\n".format(catalog_number=b.catalog_number, sci_name=b.item_scientific_name,
                                                       description=b.item_description, date_collected=b.field_number)
            content = content + specimen_data
        response = HttpResponse(content, content_type='text/plain')  # declare the response type
        response['Content-Disposition'] = 'attachment; filename="Specimens.txt"'  # declare the file name
        return response
    generate_specimen_labels.short_description = 'Specimen Labels'

    def generate_barcode(self, request, queryset):
        b=Biology.objects.get(barcode=1040)
        d = barcode.MyBarcodeDrawing(b.barcode)
        binaryStuff = d.asString('gif')
        return HttpResponse(binaryStuff, 'image/gif')


############################
#  Register Admin Classes  #
############################
admin.site.register(Occurrence, OccurrenceAdmin)
admin.site.register(Biology, BiologyAdmin)
