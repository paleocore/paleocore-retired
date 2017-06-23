from django.contrib import admin
from models import Occurrence, Biology, Locality
import base.admin


# Register your models here.
class LocalityAdmin(base.admin.DGGeoAdmin):
    list_display = ('locality_number', 'locality_field_number', 'name', 'date_discovered',
                    'point_x', 'point_y')
    readonly_fields = ('locality_number', 'point_x', 'point_y', 'easting', 'northing', 'date_last_modified')
    list_filter = ['date_discovered', 'formation', 'NALMA', 'region', 'county']
    search_fields = ('locality_number', 'locality_field_number', 'name')


class BiologyAdmin(admin.ModelAdmin):
    list_display = ('specimen_number', 'item_scientific_name', 'item_description', 'locality',
                    'date_collected', 'time_collected', 'date_time_collected', 'on_loan', 'date_last_modified')
    list_filter = ['date_collected', 'on_loan', 'NALMA', 'date_last_modified']

    list_per_page = 1000

admin.site.register(Occurrence)
admin.site.register(Biology, BiologyAdmin)
admin.site.register(Locality, LocalityAdmin)