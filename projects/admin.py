from django.contrib.gis import admin
from projects.models import Project, ProjectTerm
from olwidget.admin import GeoModelAdmin

class ProjectTermInline(admin.TabularInline):
    model = ProjectTerm
    extra = 1
    ordering = 'term',
    readonly_fields = 'native_project',
    fields = 'term', 'native', 'mapping',

class ProjectsAdmin(GeoModelAdmin):
    list_display = ["full_name", "short_name", "is_standard", "geographic", "website", "is_public"]
    options = {
        'layers': ['google.terrain']
    }
    filter_horizontal = ('users', 'terms',)
    inlines = (ProjectTermInline,)

admin.site.register(Project, ProjectsAdmin)