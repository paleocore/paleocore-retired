from django.contrib import admin
from standard.models import Project, Term, TermCategory, TermStatus, TermDataType, Comment


# class ProjectAdmin(admin.ModelAdmin):
#     list_display = ('name', 'is_standard', 'user_names', 'geographic', 'temporal')
#     filter_horizontal = ('users', 'reused_terms')
#     ordering = ("name",)

class TermAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'data_type', 'status', 'category')
    list_filter = ['data_type', 'status', 'category']
    ordering = ('name',)
    filter_horizontal = ('projects',)

class TermCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_occurrence', 'description', 'parent', 'tree_visibility')
    list_filter = ['is_occurrence']
    ordering = ('name',)


#custom admin list filter. this comes straight from the django admin site docs
#I could add related_term__project to list filters, but this would result in two filters called "project"
#I get around this by creating a custom SimpleListFilter so I can specify the name
# class RelatedProjectsListFilter(admin.SimpleListFilter):
#     # Human-readable title which will be displayed in the
#     # right admin sidebar just above the filter options.
#     title = 'related project'
#
#     # Parameter for the filter that will be used in the URL query.
#     parameter_name = 'related-project'
#
#     def lookups(self, request, model_admin):
#         """
#         Returns a list of tuples. The first element in each
#         tuple is the coded value for the option that will
#         appear in the URL query. The second element is the
#         human-readable name for the option that will appear
#         in the right sidebar.
#         """
#         projectsTuple = tuple(Project.objects.all().values_list("name","name"))
#         return projectsTuple
#
#     def queryset(self, request, queryset):
#         """
#         Returns the filtered queryset based on the value
#         provided in the query string and retrievable via
#         `self.value()`.
#         """
#         if self.value():
#             return queryset.filter(related_term__project__name=self.value())

# class TermRelationshipAdmin(admin.ModelAdmin):
#     def term(self):
#         project_name = str(self.term.project)
#         term_name  =str(self.term.name)
#         return project_name+' : '+term_name
#
#     def related_term(self):
#         project_name = str(self.related_term.project)
#         term_name  =str(self.related_term.name)
#         return project_name+' : '+term_name
#
#     list_display = (term, related_term, 'relationship_type', 'term_project')
#     list_filter = ["term__project", RelatedProjectsListFilter]
#     search_fields = ["related_term__name", "term__name"]
#     ordering = ('term',)

#admin.site.register(Project, ProjectAdmin)
admin.site.register(Comment)
admin.site.register(Term, TermAdmin)
admin.site.register(TermCategory, TermCategoryAdmin)
admin.site.register(TermStatus)
admin.site.register(TermDataType)
# admin.site.register(TermRelationship, TermRelationshipAdmin)
# admin.site.register(TermRelationshipType)