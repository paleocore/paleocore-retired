from django.contrib import admin
from models import PaleoSite, Occurrence

# Register your models here.
class OccurrenceAdmin(admin.ModelAdmin):
    list_display = ('id', 'catalog_number', 'item_scientific_name', 'item_description')
class PaleoSiteAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'setting')

admin.site.register(PaleoSite, PaleoSiteAdmin)
admin.site.register(Occurrence, OccurrenceAdmin)