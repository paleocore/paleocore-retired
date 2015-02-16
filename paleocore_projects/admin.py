from django.contrib.gis import admin
from paleocore_projects.models import Project


class projectsAdmin(admin.GeoModelAdmin):
    list_display = ["full_name", "paleocore_appname","latitude", "longitude", "is_public"]

admin.site.register(Project, projectsAdmin)