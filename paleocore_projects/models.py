from django.contrib.gis.db import models
from mysite.settings import INSTALLED_APPS

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
    display_fields = models.TextField(max_length=2000, null=True, blank=True, help_text="a list of fields to display in the public view of the data, in the same format as the list_display setting in admin.py")
    display_filter_fields = models.TextField(max_length=2000, null=True, blank=True, help_text="a list of fields to filter on in the public view of the data, in the same format as the list_filter setting in admin.py")
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

    def __unicode__(self):
        return self.full_name

