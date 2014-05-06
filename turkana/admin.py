from django.contrib.gis import admin

from turkana.models import Turkana


class TurkanaAdmin(admin.ModelAdmin):
    list_display = list((Turkana.fields_to_display()))
    search_fields = list((Turkana.fields_to_display()))
    list_filter = ["study_area","formation", "member",]



admin.site.register(Turkana, TurkanaAdmin)
