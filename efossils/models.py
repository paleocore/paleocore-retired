from django.contrib.gis.db import models
from mysite import ontologies

settingCHOICES = ontologies.SETTING_CHOICES
countryCHOICES = ontologies.COUNTRY_CHOICES
regionCHOICES = ontologies.REGION_CHOICES
continentCHOICES = ontologies.CONTINENT_CHOICES
materialCHOICES = ontologies.MATERIAL_CHOICES
epochCHOICES = ontologies.EPOCH_CHOICES


class PaleoSite(models.Model):
    """
    Namespaces
    dwc: Darwin Core
    dc: Dublin Core
    tdr: the Digital Archaeological Record tDAR
    """
    name = models.CharField(max_length=255, blank=False, null=False)  # REQUIRED
    setting = models.CharField(max_length=255, blank=True, null=True, choices=settingCHOICES)
    continent = models.CharField(max_length=255, blank=True, null=True, choices=continentCHOICES)  # dwc:continent
    country = models.CharField(max_length=255, blank=True, null=True, choices=countryCHOICES)  # dwc:country
    region = models.CharField(max_length=255, blank=True, null=True, choices=regionCHOICES)  # dwc:locality
    research_project = models.CharField(max_length=255, blank=True, null=True)  # e.g.
    collection_code = models.CharField(null=True, blank=True,max_length=20)  # dwc:collection_code
    geological_member = models.CharField(max_length=255, blank=True, null=True)  # dwd:member
    cultural_term = models.CharField(max_length=255, blank=True, null=True)  # tdr:cultural_term, Stillbay
    technology_period = models.CharField(max_length=255, blank=True, null=True)  # e.g. MSA, ESA, UP, MP
    start_date = models.CharField(max_length=255, blank=True, null=True)  # tdr: start_date
    end_date = models.CharField(max_length=255, blank=True, null=True)  # tdr:end_date
    geological_epoch = models.CharField(max_length=255, blank=True, null=True, choices=epochCHOICES)  # dwc:epoch
    date_description = models.CharField(max_length=255, blank=True, null=True)  # tdr:date_description, e.g. ESR, OSL
    material = geom = models.CharField(max_length=255, blank=True, null=True, choices=materialCHOICES)  # tdr:material_types
    references = models.TextField(null=True, blank=True,max_length=2500)  # dwc:references
    remarks = models.TextField(null=True, blank=True, max_length=2500)
    geom = models.PointField(srid=4326)


