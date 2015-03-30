from django.contrib.gis.db import models
from mysite.settings import INSTALLED_APPS
from django.db.models.loading import get_model
from django.core.exceptions import ValidationError
from ast import literal_eval

#exclude any installed apps that have 'django' in the name
app_CHOICES = [(name, name) for name in INSTALLED_APPS if name.find("django") == -1]

#This model is only for projects that are currently hosted on PaleoCore

class Project(models.Model):
    full_name = models.CharField(max_length=300)
    abstract = models.TextField(max_length=2000, null=True, blank=True, help_text="A  description of the project, its importance, etc.")
    attribution = models.TextField(max_length = 1000, null=True, blank=True, help_text="A description of the people / institutions responsible for collecting the data.")
    paleocore_appname = models.CharField(max_length = 200, choices = app_CHOICES)
    graphic = models.FileField(max_length=255, null=True, blank=True, upload_to="uploads/images/paleocore_projects")
    occurrence_table_name = models.CharField(max_length=255, help_text="the name of the main occurrence table in the models.py file of the associated app")
    is_public = models.BooleanField(default=False, help_text="Is the raw data to be made publicly viewable?")
    display_summary_info = models.BooleanField(default=True, help_text="Should project summary data be published? Only uncheck this in extreme circumstances")
    display_fields = models.TextField(max_length=2000, default="['id',]",null=True, blank=True, help_text="a list of fields to display in the public view of the data, first entry should be 'id'")
    display_filter_fields = models.TextField(max_length=2000, default="[]", null=True, blank=True, help_text="a list of fields to filter on in the public view of the data, can be empty list []")
    geom = models.PointField(srid=4326,db_column="shape")
    objects = models.GeoManager()

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
        model = get_model(self.paleocore_appname, self.occurrence_table_name)
        return(model.objects.all().count())

    def __unicode__(self):
        return self.full_name

    def clean(self, *args, **kwargs):

        #try to get the paleocore model implied by the entries
        model = get_model(self.paleocore_appname, self.occurrence_table_name)
        if not model:
            raise ValidationError("there is no field '" + self.occurrence_table_name + "'" + " in the " + self.paleocore_appname + " app.")

        #make sure the display fields are valid list or tuple
        try:
            literal_eval(self.display_fields)
            literal_eval(self.display_filter_fields)
        except:
            raise ValidationError("Display fields and filter fields must be a valid list or tuple")

        fieldnames = model._meta.get_all_field_names()

        #test that all the display fields are actual valid fieldnames
        for field in literal_eval(self.display_fields):
            if not field in fieldnames:
                raise ValidationError("'" + field + "' is not a valid field in " + self.paleocore_appname + "." + self.occurrence_table_name)

        #test that all the display fields are actual valid fieldnames
        for field in literal_eval(self.display_filter_fields):
            if not field in fieldnames:
                raise ValidationError("'" + field + "' is not a valid field in " + self.paleocore_appname + "." + self.occurrence_table_name)

        #call the normal clean
        super(Project, self).clean(*args, **kwargs)

    #have to call full clean before saving so that the above clean method gets run
    def save(self, *args, **kwargs):
        self.full_clean()
        super(Project, self).save(*args, **kwargs)

