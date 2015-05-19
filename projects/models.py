from django.contrib.gis.db import models
from mysite.settings import INSTALLED_APPS
from django.db.models.loading import get_model
from django.core.exceptions import ValidationError
from base.models import PaleocoreUser
from ast import literal_eval

#exclude any installed apps that have 'django' in the name
app_CHOICES = [(name, name) for name in INSTALLED_APPS if name.find("django") == -1]


#This model is only for projects that are currently hosted on PaleoCore

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

class Project(models.Model):
    short_name = models.CharField(max_length=50, unique=True)
    full_name = models.CharField(max_length=300)
    abstract = models.TextField(max_length=4000, null=True, blank=True, help_text="A  description of the project, its importance, etc.")
    is_standard = models.BooleanField(default=False)
    attribution = models.TextField(max_length = 1000, null=True, blank=True, help_text="A description of the people / institutions responsible for collecting the data.")
    website = models.URLField(null=True, blank=True)
    geographic = models.CharField(max_length=255, null=True, blank=True)
    temporal = models.CharField(max_length=255, null=True, blank=True)
    paleocore_appname = models.CharField(max_length=200, null=True, blank=True, choices=app_CHOICES)
    graphic = models.FileField(max_length=255, null=True, blank=True, upload_to="uploads/images/projects")
    occurrence_table_name = models.CharField(max_length=255, null=True, blank=True, help_text="the name of the main occurrence table in the models.py file of the associated app")
    is_public = models.BooleanField(default=False, help_text="Is the raw data to be made publicly viewable?")
    display_summary_info = models.BooleanField(default=True, help_text="Should project summary data be published? Only uncheck this in extreme circumstances")
    #display_fields = models.TextField(max_length=2000, default="['id',]",null=True, blank=True, help_text="a list of fields to display in the public view of the data, first entry should be 'id'")
    #display_filter_fields = models.TextField(max_length=2000, default="[]", null=True, blank=True, help_text="a list of fields to filter on in the public view of the data, can be empty list []")
    users = models.ManyToManyField(PaleocoreUser, blank=True, null=True)
    terms = models.ManyToManyField('standard.Term', through='ProjectTerm', blank=True, null=True)
    geom = models.PointField(srid=4326)
    objects = models.GeoManager()

    # def terms(self):
    #     return sorted(self.term_set.all(), key=lambda term: term.relatedTermCount(), reverse=True)

    # def user_names(self):
    #     return ', '.join((str(u) for u in self.users.all()))
    # user_names.short_description = 'Project Users'

    class Meta:
        ordering = ["short_name"]
        verbose_name_plural = "Projects"
        verbose_name = "Project"

    def longitude(self):
        try:
            return self.geom.coords[1]
        except:
            return 0

    def latitude(self):
        try:
            return self.geom.coords[0]
        except:
            return 0

    def record_count(self):
        if self.is_standard:
            return 0
        else:
            model = get_model(self.paleocore_appname, self.occurrence_table_name)
            return(model.objects.all().count())

    def __unicode__(self):
        return self.full_name

    # def clean(self, *args, **kwargs):
    #
    #     #try to get the paleocore model implied by the entries
    #     model = get_model(self.paleocore_appname, self.occurrence_table_name)
    #     if model:
    #     #    raise ValidationError("there is no field '" + self.occurrence_table_name + "'" + " in the " + self.paleocore_appname + " app.")
    #     #else:
    #         #make sure the display fields are valid list or tuple
    #         try:
    #             literal_eval(self.display_fields)
    #             literal_eval(self.display_filter_fields)
    #         except:
    #             raise ValidationError("Display fields and filter fields must be a valid list or tuple")
    #
    #         fieldnames = model._meta.get_all_field_names()
    #
    #         #test that all the display fields are actual valid fieldnames
    #         for field in literal_eval(self.display_fields):
    #             if not field in fieldnames:
    #                 raise ValidationError("'" + field + "' is not a valid field in " + self.paleocore_appname + "." + self.occurrence_table_name)
    #
    #         #test that all the display fields are actual valid fieldnames
    #         for field in literal_eval(self.display_filter_fields):
    #             if not field in fieldnames:
    #                 raise ValidationError("'" + field + "' is not a valid field in " + self.paleocore_appname + "." + self.occurrence_table_name)
    #
    #     #call the normal clean
    #     super(Project, self).clean(*args, **kwargs)
    #
    # #have to call full clean before saving so that the above clean method gets run
    # def save(self, *args, **kwargs):
    #     self.full_clean()
    #     super(Project, self).save(*args, **kwargs)

# FYI: this is a case of this: https://docs.djangoproject.com/en/dev/topics/db/models/#extra-fields-on-many-to-many-relationships
class ProjectTerm(models.Model):
    term = models.ForeignKey('standard.Term')
    project = models.ForeignKey('projects.Project')
    belongs_to = models.BooleanField(default=False, help_text="If true, this term is native to the project or standard, otherwise the term is being reused by the project or standard.")
    display = models.BooleanField(default=False, help_text="If true, term will be included in the list of fields displayed in the public view of the data.")
    filter = models.BooleanField(default=False, help_text="If true, term will be included in the list of fields to filter on in the public view of the data.")
    mapping = models.CharField(max_length=255, null=True, blank=True, help_text="If this term is being reused from another standard or project, the mapping field is used to provide the name of the field in this project or standard as opposed to the name in the project or standard from which it is being reused.")

    def term_project(self):
        return self.project.full_name

    def __unicode__(self):
        return "[" + str(self.project) + "] " + self.term.name

    class Meta:
        verbose_name = "Project Term"
        verbose_name_plural = "Project Terms"
        db_table = 'projects_project_term'
