from django.contrib import admin
from django.http import HttpResponse
from models import Occurrence, Biology, Locality
import base.admin
import unicodecsv
import os


# Register your models here.
class OccurrenceAdmin(admin.ModelAdmin):
    list_display = ('specimen_number', 'item_scientific_name', 'item_description', 'locality',
                    'date_collected', 'time_collected', 'date_time_collected', 'on_loan', 'date_last_modified')
    list_filter = ['date_collected', 'on_loan', 'date_last_modified']

    list_per_page = 1000


class LocalityAdmin(base.admin.DGGeoAdmin):
    list_display = ('locality_number', 'locality_field_number', 'name', 'date_discovered',
                    'point_x', 'point_y')
    readonly_fields = ('locality_number', 'point_x', 'point_y', 'easting', 'northing', 'date_last_modified')
    list_filter = ['date_discovered', 'formation', 'NALMA', 'region', 'county']
    search_fields = ('locality_number', 'locality_field_number', 'name')


class BiologyAdmin(admin.ModelAdmin):
    list_display = ('specimen_number', 'item_scientific_name', 'item_description', 'locality',
                    'date_collected', 'time_collected', 'date_time_collected', 'on_loan', 'date_last_modified')
    list_filter = ['tax_order', 'family', 'genus', 'date_collected', 'on_loan', 'NALMA', 'date_last_modified', 'locality']
    list_per_page = 1000
    search_fields = ['tax_class', 'tax_order', 'family', 'tribe', 'genus', 'specific_epithet', 'item_scientific_name']
    actions = ['create_data_csv']

    def create_data_csv(self, request, queryset):
        """
        Export biology data to csv format. Still some issues with unicode characters.
        :param request:
        :param queryset:
        :return:
        """
        response = HttpResponse(content_type='text/csv')  # declare the response type
        # TODO generalize project file name
        # Use ContentType.objects.get_for_model(myobject)
        response['Content-Disposition'] = 'attachment; filename="GDB_Biology.csv"'  # declare the file name
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

    class Media:
        js = ['admin/js/list_filter_collapse.js']

    create_data_csv.short_description = 'Download Selected to .csv'


admin.site.register(Occurrence, OccurrenceAdmin)
admin.site.register(Biology, BiologyAdmin)
admin.site.register(Locality, LocalityAdmin)
