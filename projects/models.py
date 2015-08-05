from django.contrib.gis.db import models
from mysite.settings import INSTALLED_APPS
from django.db.models.loading import get_model
from django.contrib.contenttypes.models import ContentType
from django.core.exceptions import ValidationError
from base.models import PaleocoreUser
from ast import literal_eval

# exclude any installed apps that have 'django' in the name
app_CHOICES = [(name, name) for name in INSTALLED_APPS if name.find("django") == -1]

abstract_help_text = "A  description of the project, its importance, etc."
attribution_help_text = "A description of the people / institutions responsible for collecting the data."
occurrence_table_name_help_text = "The name of the main occurrence table in the models.py file of the associated app"
display_summary_info_help_text = "Should project summary data be published? Only uncheck this in extreme circumstances"
display_fields_help_text = "A list of fields to display in the public view of the data, first entry should be 'id'"
display_filter_fields_help_text = "A list of fields to filter on in the public view of the data, can be empty list []"


class Project(models.Model):
    short_name = models.CharField(max_length=50, unique=True)
    full_name = models.CharField(max_length=300, unique=True, db_index=True)
    paleocore_appname = models.CharField(max_length=200, choices=app_CHOICES, null=True)
    abstract = models.TextField(max_length=4000, null=True, blank=True,
                                help_text=abstract_help_text)
    is_standard = models.BooleanField(default=False)
    attribution = models.TextField(max_length=1000, null=True, blank=True,
                                   help_text=attribution_help_text)
    website = models.URLField(null=True, blank=True)
    geographic = models.CharField(max_length=255, null=True, blank=True)
    temporal = models.CharField(max_length=255, null=True, blank=True)
    graphic = models.FileField(max_length=255, null=True, blank=True, upload_to="uploads/images/projects")
    occurrence_table_name = models.CharField(max_length=255, null=True, blank=True,
                                             help_text=occurrence_table_name_help_text)
    is_public = models.BooleanField(default=False, help_text="Is the raw data to be made publicly viewable?")
    display_summary_info = models.BooleanField(default=True,
                                               help_text=display_summary_info_help_text)
    display_fields = models.TextField(max_length=2000, default="['id',]", null=True, blank=True,
                                      help_text=display_fields_help_text)
    display_filter_fields = models.TextField(max_length=2000, default="[]", null=True, blank=True,
                                             help_text=display_filter_fields_help_text)
    users = models.ManyToManyField(PaleocoreUser, blank=True, null=True)
    terms = models.ManyToManyField('standard.Term', through='ProjectTerm', blank=True, null=True)
    default_app_model = models.ForeignKey(ContentType, blank=True, null=True)
    geom = models.PointField(srid=4326, blank=True, null=True)
    objects = models.GeoManager()

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

    # def record_count(self):
    #     if self.is_standard:
    #         return 0
    #     else:
    #         model = get_model(self.paleocore_appname, self.occurrence_table_name)
    #         return model.objects.count()

    def __unicode__(self):
        return self.full_name


# FYI: this is a case of this:
# https://docs.djangoproject.com/en/dev/topics/db/models/#extra-fields-on-many-to-many-relationships
class ProjectTerm(models.Model):
    term = models.ForeignKey('standard.Term')
    project = models.ForeignKey('projects.Project')
    native = models.BooleanField(default=False,
                                 help_text="If true, this term is native to the project or standard, otherwise the "
                                           "term is being reused by the project or standard.")
    mapping = models.CharField(max_length=255, null=True, blank=True,
                               help_text="If this term is being reused from another standard or project, "
                                         "the mapping field is used to provide the name of the field in this project "
                                         "or standard as opposed to the name in the project or standard "
                                         "from which it is being reused.")

    def native_project(self):
        return str(self.term.native_project())

    def term_project(self):
        return self.project.full_name

    def __unicode__(self):
        # return "[" + str(self.term.native_project()) + "] " + self.term.name
        return self.term.name

    class Meta:
        verbose_name = "Project Term"
        verbose_name_plural = "Project Terms"
        db_table = 'projects_project_term'
        unique_together = ('project', 'term',)
