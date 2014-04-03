from django.contrib import admin
from schema.models import Project, Term, TermCategory, TermStatus, TermDataType, TermRelationship, \
        TermRelationshipType, Comment

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'user_names', 'geographic', 'temporal')
    filter_horizontal = ('users',)
    ordering = ("name",)

class TermAdmin(admin.ModelAdmin):
    list_display = ('name','project','data_type','status','category')
    list_filter = ['project','data_type','status','category']
    ordering = ('project','name')

class TermCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_occurrence', 'description','parent','tree_visibility')
    list_filter = ['is_occurrence']
    ordering = ('name',)

class TermRelationshipAdmin(admin.ModelAdmin):
    def term(self):
        project_name = str(self.term.project)
        term_name  =str(self.term.name)
        return project_name+' : '+term_name

    def related_term(self):
        project_name = str(self.related_term.project)
        term_name  =str(self.related_term.name)
        return project_name+' : '+term_name

    list_display = (term, related_term, 'relationship_type','term_project')
    ordering = ('term',)

admin.site.register(Project, ProjectAdmin)
admin.site.register(Comment)
admin.site.register(Term, TermAdmin)
admin.site.register(TermCategory, TermCategoryAdmin)
admin.site.register(TermStatus)
admin.site.register(TermDataType)
admin.site.register(TermRelationship, TermRelationshipAdmin)
admin.site.register(TermRelationshipType)