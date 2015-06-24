from django.db import models
from base.models import PaleocoreUser
from projects.models import Project
from django.db import connection

# Create your models here.

############################################
# TermCategory
############################################
class TermCategory(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=4000)
    is_occurrence = models.BooleanField()
    parent = models.ForeignKey('self', null=True, blank=True)
    tree_visibility = models.BooleanField(default=True)

    def __unicode__(self):
        return self.name
    
    class Meta:
        ordering = ["name"]
        verbose_name = "Term Category"
        verbose_name_plural = "Term Categories"
        db_table = "standard_term_category"

############################################
# TermStatus
############################################
class TermStatus(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=4000)

    def __unicode__(self):
        return self.name
    
    class Meta:
        ordering = ["name"]
        verbose_name = "Term Status"
        verbose_name_plural = "Term Statuses"
        db_table = "standard_term_status"
      
############################################
# TermDataType
############################################  
class TermDataType(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=4000)
    
    def __unicode__(self):
        return self.name    
    
    class Meta:
        ordering = ["name"]
        verbose_name_plural = "Term Types"
        verbose_name = "Term Type"
        db_table = "standard_term_data_type"

############################################
# TermRelationshipType
############################################
# class TermRelationshipType(models.Model):
#     name = models.CharField(max_length=50, unique=True)
#     description = models.CharField(max_length=4000)
#     preposition = models.CharField(max_length=15)
#
#     def __unicode__(self):
#         return self.name
#
#     class Meta:
#         ordering = ["name"]
#         verbose_name_plural = "Term Relationship Types"
#         verbose_name = "Term Relationship Type"
#         db_table = "standard_term_relationship_type"

############################################
# Project
############################################       
# class Project(models.Model):
#     name = models.CharField(max_length=50, unique=True)
#     description = models.CharField(max_length=4000, null=True, blank=True)
#     is_standard = models.BooleanField(default=False)
#     website = models.URLField(null=True, blank=True)
#     geographic = models.CharField(max_length=255, null=True, blank=True)
#     temporal = models.CharField(max_length=255, null=True, blank=True)
#     users = models.ManyToManyField(PaleocoreUser, blank=True, null=True)
#     reused_terms = models.ManyToManyField('Term', blank=True, null=True, related_name='reused_by_projects')
#
#     def terms(self):
#         return sorted(self.term_set.all(), key=lambda term: term.relatedTermCount(), reverse=True)
#
#     def occurrenceTerms(self):
#         return sorted(self.term_set.filter(category__is_occurrence = True))
#
#     def relatedTermCount(self):
#         r = 0
#         for term in self.term_set.all():
#             r = r + term.relatedTermCount()
#         return r
#
#     def user_names(self):
#         return ', '.join((str(u) for u in self.users.all()))
#
#     user_names.short_description = 'Project Users'
#
#     def __unicode__(self):
#         return self.name
#
#     class Meta:
#         ordering = ["name"]
#         verbose_name_plural = "Projects"
#         verbose_name = "Project"

############################################
# Term
############################################        
class Term(models.Model):
    name = models.CharField(max_length=50)
    definition = models.TextField()
    data_type = models.ForeignKey(TermDataType)
    status = models.ForeignKey(TermStatus)
    category = models.ForeignKey(TermCategory, null=True)
    example = models.TextField(null=True, blank=True)
    data_range = models.CharField(max_length=255, null=True, blank=True)
    uses_controlled_vocabulary = models.BooleanField(default=False)
    controlled_vocabulary = models.CharField(null=True, blank=True, max_length=75)
    controlled_vocabulary_url = models.CharField(null=True, blank=True, max_length=155)
    uri = models.CharField(null=True, blank=True, max_length=255)
    projects = models.ManyToManyField('projects.Project', through='projects.ProjectTerm', blank=True, null=True)

    def get_projects(self):
        return ', '.join(['project.short_name' for projects in self.projects.all()])

    def native_project(self):
        try:
            native_project_term = self.projectterm_set.get(native=True)
            return native_project_term.project.full_name
        except:
            return None

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ["name"]
        verbose_name_plural = "Terms"
        verbose_name = "Term"

############################################
# Comment
############################################
class Comment(models.Model):
    term = models.ForeignKey(Term)
    subject = models.CharField(max_length=100)
    body = models.TextField()
    author = models.ForeignKey(PaleocoreUser)
    timestamp = models.DateTimeField()
    
    def __unicode__(self):
        return self.subject + "(" + self.author + ", " + self.timestamp.__str__() + ")"
    
    class Meta:
        ordering = ["-timestamp"]
        verbose_name_plural = "Comments"
        verbose_name = "Comment"

############################################
# TermRelationship
############################################       
# class TermRelationship(models.Model):
#     term = models.ForeignKey(Term, related_name='term_relationships')
#     related_term = models.ForeignKey(Term, related_name='related_term_relationships')
#     relationship_type = models.ForeignKey(TermRelationshipType)
#
#     def term_project(self):
#         return self.term.project.name
#
#     def __unicode__(self):
#         return "[" + str(self.term.project) + "] " + self.term.name + " (" + self.relationship_type.name + ") " + "[" + str(self.related_term.project) + "] " + self.related_term.name
#
#     class Meta:
#         verbose_name = "Term Relationship"
#         verbose_name_plural = "Term Relationships"
#         unique_together = ("term", "related_term", "relationship_type")
#         db_table = "standard_term_relationship"

## ModelForms
class CompareView():

    baseProject = Project
    projects = []
    termViews = []
    showColumns = []
    showProjects = []

    def showColumnsCount(self):
        return self.showColumns.count()

    def projectNames(self):
        projectNames = []
        for project in self.projects:
            projectNames.append(project.name)
        return projectNames

    def __init__( self ):
        self.termViews = []
        self.baseProject = Project
        self.projects = []

# class RelatedTermView():
#     term_id = 0
#     name = ""
#     project_name = ""
#     related_projects = 0


class TermView():
    id = ""
    name = ""
    definition = ""
    data_type = ""
    projectsWithRelatedTerms = []
    relatedProjectCount = None

    def percentageOfRelatedProjects(self):
        if self.relatedProjectCount == None:
            self.numberOfRelatedProjects()

        totalProjects = Project.objects.count()

        return (self.relatedProjectCount*100)/totalProjects

    def numberOfRelatedProjects(self):
        cursor = connection.cursor()

        # Data retrieval operation - no commit required
        cursor.execute("SELECT related_projects FROM term_project_relationship_count WHERE term_id = %s", [self.id])
        row = cursor.fetchone()

        self.relatedProjectCount = row[0]

        return self.relatedProjectCount

    def projectsWithRelatedTermsNames(self):
        projectNames = []
        for projectView in self.projectsWithRelatedTerms:
            projectNames.append(projectView.name)
        return projectNames

    def __init__( self ):
        self.projectsWithRelatedTerms = []

class ProjectView():
    name = ""
    # relatedTermRelationship = TermRelationship

class RelateProjectTerms():
    firstProject = Project
    secondProject = Project

#class TermRelationshipView():
#    type = ""
#    termProject = ProjectView
#    relatedTermProject = ProjectView
