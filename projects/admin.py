from django.contrib.gis import admin
from models import Project, ProjectTerm
from olwidget.admin import GeoModelAdmin


class ProjectTermInline(admin.TabularInline):
    model = ProjectTerm
    extra = 1
    ordering = 'term',
    readonly_fields = 'native_project',
    fields = 'term', 'native', 'mapping',


class ProjectsAdmin(GeoModelAdmin):
    list_display = ['full_name', 'short_name', 'is_standard', 'geographic', 'website', 'is_public']
    list_filter = ['is_standard', 'is_public']
    search_fields = ['full_name', 'short_name']
    options = {}
    # options = {
    #     'layers': ['google.terrain']
    # }
    inlines = (ProjectTermInline,)

admin.site.register(Project, ProjectsAdmin)
