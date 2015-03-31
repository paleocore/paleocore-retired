from django.contrib.gis import admin
from paleocore_projects.models import Project
from olwidget.admin import GeoModelAdmin

class projectsAdmin(GeoModelAdmin):
    list_display = ["full_name", "paleocore_appname","latitude", "longitude", "is_public"]
    options = {
        'layers': ['google.terrain']
    }

admin.site.register(Project, projectsAdmin)