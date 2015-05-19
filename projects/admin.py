from django.contrib.gis import admin
from projects.models import Project, ProjectTerm
from olwidget.admin import GeoModelAdmin

class projectsAdmin(GeoModelAdmin):
    list_display = ["full_name", "paleocore_appname", "latitude", "longitude", "is_public"]
    options = {
        'layers': ['google.terrain']
    }
    filter_horizontal = ('users', 'terms',)

admin.site.register(Project, projectsAdmin)