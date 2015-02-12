from django_countries.fields import CountryField
from django.contrib.gis.db import models


class Site(models.Model):
    id = models.AutoField(primary_key=True)
    site = models.CharField('Site name', max_length=255, blank=False, null=True)
    country = CountryField('Country', null=True, max_length=255)
    data_source = models.CharField('Data Source', max_length=50, blank=True, null=True)
    #latitude = models.FloatField('Latitude', blank=True, null=True)
    #longitude = models.FloatField('Longitude', blank=True, null=True)
    altitude = models.FloatField('Altitude', blank=True, null=True)
    site_types = (('Shelter', 'Shelter'), ('Cave', 'Cave'), ('Open-air', 'Open-air'), ('Unknown', 'Unknown'))
    site_type = models.CharField('Site type', max_length=20, blank=True, null=True, choices=site_types)
    display = models.NullBooleanField('Flagged', blank=True, null=True)
    map_location = models.PointField(dim=2, blank=True, null=True)
    objects = models.GeoManager()
    notes = models.TextField(blank=True, null=True)

    def longitude(self):
        if self.map_location:
            return self.map_location.x
        else:
            return None

    def latitude(self):
        if self.map_location:
            return self.map_location.y
        else:
            return None

    class Meta:
        managed = True
        #db_table = 'sites'

    def __unicode__(self):
        return u'%s, %s' % (self.site, self.country)


class Date(models.Model):
    site = models.ForeignKey(Site)
    layer = models.CharField('Layer', max_length=300, blank=True, null=True)
    industry = models.CharField('Industry', max_length=100, blank=True, null=True)
    industry_2 = models.CharField('Industry', max_length=100, blank=True, null=True)
    industry_3 = models.CharField('Industry', max_length=100, blank=True, null=True)
    cat_no = models.CharField('Catalog Number', max_length=100, blank=True, null=True)
    date = models.FloatField('Age', blank=True, null=True)
    sd_plus = models.FloatField('SD Plus', blank=True, null=True)
    sd_minus = models.FloatField('SD Minus', blank=True, null=True)
    sample = models.CharField('Sample', max_length=100, blank=True, null=True)
    technique = models.CharField('Method', max_length=100, blank=True, null=True)
    corrected_date_BP = models.FloatField('Cal. Age BP', blank=True, null=True)
    plus = models.FloatField('Cal. Plus', blank=True, null=True)
    minus = models.FloatField('Cal. Minus', blank=True, null=True)
    hominid_remains = models.TextField('Hominins', blank=True, null=True)
    bibliography = models.TextField('Bibliography', blank=True, null=True)
    period = models.CharField('Period', max_length=100, blank=True, null=True)
    notes = models.TextField('Notes', blank=True, null=True)
    intcal09_max = models.FloatField('IntCal09 Max. Age', blank=True, null=True)
    intcal09_min = models.FloatField('IntCal09 Min. Age', blank=True, null=True)

    class Meta:
        managed = True
        #db_table = 'dates'

    def __unicode__(self):
        return u'%s %s %s' % (self.site,self.layer,self.industry)


class Site_plus_dates(Site):
    class Meta:
        proxy = True
        managed = True
        verbose_name = "Sites and dates"
        verbose_name_plural = "Sites and dates"
