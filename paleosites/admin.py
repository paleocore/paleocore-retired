from models import Site, Date, Site_plus_dates
from django.contrib.gis import admin
import django.contrib.gis.geos
import csv
from django_countries import countries
from django.contrib.gis.db import models


class DateInLine(admin.StackedInline):
    model = Date
    extra = 1
    fieldsets = [('Sample Information', {
                 'fields': [('layer', 'industry', 'industry_2', 'industry_3'),
                            ('cat_no', 'sample', 'technique', 'date', 'sd_plus', 'sd_minus', 'corrected_date_BP',
                             'plus', 'minus', 'intcal09_max', 'intcal09_min'),
                            ('hominid_remains', 'bibliography', 'notes', 'period')],
                 'classes': [('collapse')]})]


class SiteDateAdmin(admin.ModelAdmin):
    inlines = [
        DateInLine,
    ]
    fieldsets = [(None, {
                 'fields': [('site', 'site_type'), ('latitude', 'longitude', 'altitude', 'country'),
                            ('data_source')]})]
    readonly_fields = ('latitude', 'longitude',)
    list_display = ('site', 'site_type', 'latitude', 'longitude', 'altitude', 'country', 'data_source')
    list_filter = ['country', 'data_source']
    search_fields = ['site', 'country']


class SiteAdmin(admin.OSMGeoAdmin):
    fieldsets = [(None, {
                 'fields': [('site', 'site_type', 'data_source', 'display'), ('latitude', 'longitude', 'altitude',
                                                                              'country'), ('map_location', 'notes')]})]
    readonly_fields = ('latitude', 'longitude',)
    list_display = ('site', 'site_type', 'latitude', 'longitude', 'altitude', 'country', 'data_source')
    list_filter = ['data_source', 'display', 'country']
    ordering = ['site',]
    search_fields = ['site', 'country']

    def update_map_location(modeladmin, request, queryset):
        for a_site in Site.objects.all():
            if a_site.latitude and a_site.longitude:
                pnt = django.contrib.gis.geos.GEOSGeometry('POINT(%s %s)' % (a_site.longitude,a_site.latitude))
                a_site.map_location = pnt
                a_site.save()
        return None         # Return None to display the change list page again.
    update_map_location.short_description = "Update map location from Lat/Long"

    def do_stuff(modeladmin, request, queryset):
        for a_site in Site.objects.all():
            if a_site.site_type=="Abri":
                a_site.site_type = "Shelter"
                a_site.save()
            if a_site.site_type=="open":
                a_site.site_type = "Open-air"
                a_site.save()
        return None
    do_stuff.short_description = "Do Stuff"

    def clear_flagged(modeladmin, request, queryset):
        for a_site in Site.objects.all():
            if a_site.display:
                a_site.display = False
                a_site.save()
        return None         # Return None to display the change list page again.
    clear_flagged.short_description = "Clear flag on all records"

    # TODO generalize this function
    def import_sites(modeladmin, request, queryset):
        with open('D:/Users/mcpherro/PycharmProjects/Sites/sites.csv', 'rb') as f:
            reader = csv.reader(f)
            for row in reader:
                country_name = row[2]
                for c in countries:
                    if row[2]==c[1]:
                        country_name = c[0]
                s = Site(id=row[0], site=row[1], country=country_name, data_source=row[3], site_type=row[7],
                         display=row[8])
                if row[4] != 'NA':
                    s.latitude = row[4]
                if row[5] != 'NA':
                    s.longitude = row[5]
                if row[6] != 'NA':
                    s.altitude = row[6]
                if row[4] != 'NA' and row[5] != 'NA':
                    pnt = django.contrib.gis.geos.GEOSGeometry('POINT(%s %s)' % (row[5], row[4]))
                    s.map_location = pnt
                s.save()
        return None         # Return None to display the change list page again.
    import_sites.short_description = "Import sites.csv"
    actions = [import_sites, update_map_location, clear_flagged, do_stuff]


class DateAdmin(admin.ModelAdmin):
    fieldsets = [('Sample Information', {
                 'fields': [('site'), ('layer', 'industry', 'industry_2', 'industry_3'),
                            ('cat_no', 'sample', 'technique', 'date', 'sd_plus', 'sd_minus', 'corrected_date_BP',
                             'plus', 'minus', 'intcal09_max', 'intcal09_min'),
                            ('hominid_remains', 'bibliography', 'notes', 'period')]})]
    list_display = ('site', 'cat_no', 'layer', 'industry')
    list_filter = ['industry']
    search_fields = ['site', 'layer', 'industry', 'industry_2', 'industry_3']

    def import_dates(modeladmin, request, queryset):
        with open('D:/Users/mcpherro/PycharmProjects/Sites/dates.csv', 'rb') as f:
            reader = csv.reader(f)
            for row in reader:
                d = Date(id=row[0], site_id=row[1], layer=row[2], industry=row[3], industry_2=row[4],
                         industry_3=row[5], cat_no=row[6], sample=row[10], technique=row[11], hominid_remains=row[15],
                         bibliography=row[16], period=row[17], notes=row[18])
                if row[7] != 'NA':
                    d.date = row[7]
                if row[8] != 'NA':
                    d.sd_plus = row[8]
                if row[9] != 'NA':
                    d.sd_minus = row[9]
                if row[19] != 'NA':
                    d.intcal09_max = row[19]
                if row[20] != 'NA':
                    d.intcal09_min = row[20]
                if row[12] != 'NA':
                    d.corrected_date_BP = row[12]
                if row[13] != 'NA':
                    d.plus = row[13]
                if row[14] != 'NA':
                    d.minus = row[14]
                d.save()
        return None         # Return None to display the change list page again.
    import_dates.short_description = "Import dates.csv"
    actions = [import_dates]

admin.site.register(Site, SiteAdmin)
admin.site.register(Site_plus_dates, SiteDateAdmin)
admin.site.register(Date, DateAdmin)
#admin.site.register(Place, admin.OSMGeoAdmin)

