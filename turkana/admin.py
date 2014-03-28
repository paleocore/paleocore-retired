from django.contrib.gis import admin

from turkana.models import Turkana


class TurkanaAdmin(admin.ModelAdmin):
    list_display = list((Turkana.fields_to_display()))




admin.site.register(Turkana, TurkanaAdmin)
