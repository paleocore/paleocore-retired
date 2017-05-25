from django.contrib import admin
from .models import PaleoSite, Occurrence
from olwidget.admin import GeoModelAdmin

# Register your models here.
class OccurrenceAdmin(GeoModelAdmin):
    list_display = ('id', 'catalog_number', 'item_scientific_name', 'item_description')
    options = {
        'layers': ['google.terrain']
    }
class PaleoSiteAdmin(GeoModelAdmin):
    list_display = ('id', 'name', 'setting')
    options = {
        'layers': ['google.terrain']
    }

admin.site.register(PaleoSite, PaleoSiteAdmin)
admin.site.register(Occurrence, OccurrenceAdmin)