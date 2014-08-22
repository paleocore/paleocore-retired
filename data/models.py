from django.db import models

# Create your models here.


class Project(models.Model):

    title = models.CharField(max_length=200, null=False, blank=False)
    short_title = models.CharField(max_length=200, null=False, blank=False)
    principle_investigator = models.CharField(max_length=200, null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    location = models.CharField(max_length=200, null=True, blank=True)
    abstract = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    logo = models.FileField(upload_to="uploads/images", null=True, blank=True)
    min_geochronological_age = models.IntegerField(null=True, blank=True)
    max_geochronological_age = models.IntegerField(null=True, blank=True)

    def __unicode__(self):
        return self.title