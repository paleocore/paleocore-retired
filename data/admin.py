from django.contrib import admin
from models import *

# Register your models here.


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'location', 'abstract', 'min_geochronological_age', "max_geochronological_age")
    list_display_links = ['title']
    list_filter = ['location', 'abstract']
    search_fields = ['title', 'short_title', 'abstract', 'description', 'principle_investigator', 'location']


admin.site.register(Project, ProjectAdmin)