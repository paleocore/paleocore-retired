from django.contrib import admin
from models import PaleoSite


# Register your models here.


class PaleoSiteAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'setting')

admin.site.register(PaleoSite, PaleoSiteAdmin)