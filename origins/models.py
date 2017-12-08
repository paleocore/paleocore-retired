from django.contrib.gis.db import models
import base.models
import uuid, datetime, os
from django_countries.fields import CountryField

# Create your models here.

class TaxonRank(base.models.TaxonRank):
    class Meta:
        verbose_name = "LGRP Taxon Rank"


class Taxon(base.models.Taxon):
    parent = models.ForeignKey('self', null=True, blank=True)
    rank = models.ForeignKey(TaxonRank, null=True, blank=True)

    class Meta:
        verbose_name = "Taxon"
        verbose_name_plural = "Taxa"
        ordering = ['rank__ordinal', 'name']


class IdentificationQualifier(base.models.IdentificationQualifier):
    class Meta:
        verbose_name = "Identification Qualifer"


class Reference(models.Model):
    # Original fields from Paleobiology DB
    reference_no = models.IntegerField(blank=True, null=True)
    record_type = models.CharField(max_length=5, null=True, blank=True)
    ref_type = models.CharField(max_length=201, null=True, blank=True)
    author1init = models.CharField(max_length=202, null=True, blank=True)
    author1last = models.CharField(max_length=203, null=True, blank=True)
    author2init = models.CharField(max_length=204, null=True, blank=True)
    author2last = models.CharField(max_length=205, null=True, blank=True)
    otherauthors = models.TextField(null=True, blank=True)
    pubyr = models.CharField(max_length=207, null=True, blank=True)
    reftitle = models.TextField(null=True, blank=True)
    pubtitle = models.TextField(null=True, blank=True)
    editors = models.TextField(null=True, blank=True)
    pubvol = models.CharField(max_length=210, null=True, blank=True)
    pubno = models.CharField(max_length=211, null=True, blank=True)
    firstpage = models.CharField(max_length=212, null=True, blank=True)
    lastpage = models.CharField(max_length=213, null=True, blank=True)
    publication_type = models.CharField(max_length=200, null=True, blank=True)
    language = models.CharField(max_length=214, null=True, blank=True)
    doi = models.CharField(max_length=215, null=True, blank=True)
    # Added fields
    source = models.CharField(max_length=216, null=True, blank=True)
    fossil = models.ManyToManyField(to='Fossil')
    # Media
    reference_pdf = models.FileField(max_length=255, blank=True, upload_to="uploads/files/origins", null=True)

    def __unicode__(self):
        unicode_string = '['+unicode(self.id)+']'
        if self.author1last:
            unicode_string = unicode_string+' '+self.author1last
        elif self.pubyr:
            unicode_string = unicode_string+' '+unicode(self.pubyr)
        return unicode_string

    def get_concrete_field_names(self):
        """
        Get field names that correspond to columns in the DB
        :return: returns a lift
        """
        field_list = self._meta.get_fields()
        return [f.name for f in field_list if f.concrete]


class Site(models.Model):
    # Original fields from Paleobiology DB
    collection_no = models.IntegerField(blank=True, null=True)
    record_type = models.CharField(max_length=20, null=True, blank=True)
    formation = models.CharField(max_length=50, null=True, blank=True)
    lng = models.DecimalField(max_digits=20, decimal_places=10, null=True, blank=True)
    lat = models.DecimalField(max_digits=20, decimal_places=10, null=True, blank=True)
    collection_name = models.CharField(max_length=200, null=True, blank=True)
    collection_subset = models.CharField(max_length=20, null=True, blank=True)
    collection_aka = models.CharField(max_length=200, null=True, blank=True)
    n_occs = models.IntegerField(null=True, blank=True)
    early_interval = models.CharField(max_length=50, null=True, blank=True)
    late_interval = models.CharField(max_length=50, null=True, blank=True)
    max_ma = models.DecimalField(max_digits=20, decimal_places=10, null=True, blank=True)
    min_ma = models.DecimalField(max_digits=20, decimal_places=10, null=True, blank=True)
    reference_no = models.IntegerField(null=True, blank=True)

    # Added fields
    name = models.CharField(max_length=40, null=True, blank=True)
    source = models.CharField(max_length=20, null=True, blank=True)
    mio_plio = models.BooleanField(default=False)

    # spatial
    geom = models.PointField(srid=4326, null=True, blank=True)

    def __unicode__(self):
        unicode_string = '['+unicode(self.id)+']'
        if self.name:
            unicode_string = unicode_string+' '+self.name
        elif self.collection_name:
            unicode_string = unicode_string+' '+self.collection_name
        return unicode_string

    def has_ref(self):
        has_ref = False
        if self.reference:
            has_ref = True
        return has_ref


class Context(models.Model):
    # Original Fields from Paleobiology DB
    collection_no = models.IntegerField(blank=True, null=True)
    record_type = models.CharField(max_length=20, null=True, blank=True)
    formation = models.CharField(max_length=50, null=True, blank=True)
    member = models.CharField(max_length=50, null=True, blank=True)
    lng = models.DecimalField(max_digits=20, decimal_places=10, null=True, blank=True)
    lat = models.DecimalField(max_digits=20, decimal_places=10, null=True, blank=True)
    collection_name = models.CharField(max_length=200, null=True, blank=True)
    collection_subset = models.CharField(max_length=20, null=True, blank=True)
    collection_aka = models.CharField(max_length=200, null=True, blank=True)
    n_occs = models.IntegerField(null=True, blank=True)
    early_interval = models.CharField(max_length=50, null=True, blank=True)
    late_interval = models.CharField(max_length=50, null=True, blank=True)
    max_ma = models.DecimalField(max_digits=20, decimal_places=10, null=True, blank=True)
    min_ma = models.DecimalField(max_digits=20, decimal_places=10, null=True, blank=True)
    reference_no = models.IntegerField(null=True, blank=True)
    # Added fields

    source = models.CharField(max_length=20, null=True, blank=True)

    geological_formation = models.CharField(max_length=50, null=True, blank=True)
    geological_member = models.CharField(max_length=50, null=True, blank=True)
    geological_bed = models.CharField(max_length=50, null=True, blank=True)
    older_interval = models.CharField(max_length=50, null=True, blank=True)
    younger_interval = models.CharField(max_length=50, null=True, blank=True)
    max_age = models.DecimalField(max_digits=20, decimal_places=10, null=True, blank=True)
    min_age = models.DecimalField(max_digits=20, decimal_places=10, null=True, blank=True)
    best_age = models.DecimalField(max_digits=20, decimal_places=10, null=True, blank=True)
    mio_plio = models.BooleanField(default=False)

    # spatial
    geom = models.PointField(srid=4326, null=True, blank=True)
    # foreign keys
    reference = models.ForeignKey(to=Reference, null=True, blank=True)
    site = models.ForeignKey(to=Site, on_delete=models.CASCADE, null=True, blank=True)

    def __unicode__(self):
        unicode_string = '['+unicode(self.id)+']'
        if self.collection_name:
            unicode_string = unicode_string+' '+self.collection_name
        return unicode_string

    def has_ref(self):
        has_ref = False
        if self.reference:
            has_ref = True
        return has_ref

    def get_concrete_field_names(self):
        """
        Get field names that correspond to columns in the DB
        :return: returns a lift
        """
        field_list = self._meta.get_fields()
        return [f.name for f in field_list if f.concrete]


class Fossil(models.Model):
    # Original Fields from Paleobiology DB
    PlaceName = models.CharField(max_length=100, null=True, blank=True)
    HomininElement = models.CharField(max_length=40, null=True, blank=True)
    HomininElementNotes = models.TextField(null=True, blank=True)
    SkeletalElement = models.CharField(max_length=40, null=True, blank=True)
    SkeletalElementSubUnit = models.CharField(max_length=40, null=True, blank=True)
    SkeletalElementSubUnitDescriptor = models.CharField(max_length=100, null=True, blank=True)
    SkeletalElementSide = models.CharField(max_length=40, null=True, blank=True)
    SkeletalElementPosition = models.CharField(max_length=40, null=True, blank=True)
    SkeletalElementComplete = models.CharField(max_length=40, null=True, blank=True)
    SkeletalElementClass = models.CharField(max_length=40, null=True, blank=True)
    Locality = models.CharField(max_length=40, null=True, blank=True)
    Country = models.CharField(max_length=20, null=True, blank=True)

    # Added fields

    # Fossil(Find)
    guid = models.URLField(null=True, blank=True)
    uuid = models.UUIDField(default=uuid.uuid4)
    catalog_number = models.CharField(max_length=40, null=True, blank=True)
    organism_id = models.CharField(max_length=40, null=True, blank=True)
    nickname = models.CharField(max_length=40, null=True, blank=True)
    holotype = models.BooleanField(default=False)
    lifestage = models.CharField(max_length=20, null=True, blank=True)
    sex = models.CharField(max_length=10, null=True, blank=True)

    project_name = models.CharField(max_length=100, null=True, blank=True)
    project_abbreviation = models.CharField(max_length=10, null=True, blank=True)
    collection_code = models.CharField(max_length=10, null=True, blank=True)

    # Record
    created_by = models.CharField(max_length=100, null=True, blank=True)
    created = models.DateTimeField('Modified', auto_now_add=True)
    modified = models.DateTimeField('Modified', auto_now=True,
                                    help_text='The date and time this resource was last altered.')

    # Location
    locality = models.CharField(max_length=40, null=True, blank=True)
    # country = models.CharField(max_length=10, null=True, blank=True)
    country = CountryField('Country', blank=True, null=True)
    continent = models.CharField(max_length=20, null=True, blank=True)
    verbatim_provenience = models.TextField(null=True, blank=True)


    image = models.ImageField(max_length=255, blank=True, upload_to="uploads/images/origins", null=True)

    # Added foreign keys
    context = models.ForeignKey(to=Context, on_delete=models.CASCADE, null=True, blank=True)

    def __unicode__(self):
        return unicode(self.id)+' '+unicode(self.HomininElement)

    def element_count(self):
        return FossilElement.objects.filter(fossil=self.id).count()

    def elements(self):
        return self.fossilelement_set.all()

    def aapa(self):
        young_sites = [None, 'Olduvai', 'Border Cave', 'Lincoln Cave', 'Olorgesailie', 'Klasies River',
                       'Thomas Quarries', u'Sal\xe9', u'Haua Fteah', u'Melka-Kuntur\xe9 (cf. Locality)',
                       u'Olduvai Gorge', u'Cave of Hearths', u'Kanjera (Locality)']
        return self.continent == 'Africa' and self.Locality not in young_sites


class FossilElement(models.Model):
    # hop db fields
    PlaceName = models.CharField(max_length=100, null=True, blank=True)
    HomininElement = models.CharField(max_length=40, null=True, blank=True)
    HomininElementNotes = models.TextField(null=True, blank=True)
    SkeletalElement = models.CharField(max_length=40, null=True, blank=True)
    SkeletalElementSubUnit = models.CharField(max_length=40, null=True, blank=True)
    SkeletalElementSubUnitDescriptor = models.CharField(max_length=100, null=True, blank=True)
    SkeletalElementSide = models.CharField(max_length=40, null=True, blank=True)
    SkeletalElementPosition = models.CharField(max_length=40, null=True, blank=True)
    SkeletalElementComplete = models.CharField(max_length=40, null=True, blank=True)
    SkeletalElementClass = models.CharField(max_length=40, null=True, blank=True)
    Locality = models.CharField(max_length=40, null=True, blank=True)
    Country = models.CharField(max_length=20, null=True, blank=True)
    # added fields
    continent = models.CharField(max_length=20, null=True, blank=True)
    # foreign keys
    fossil = models.ForeignKey(Fossil, on_delete=models.CASCADE, null=True, blank=False)

    def __unicode__(self):
        unicode_string = '['+unicode(self.id)+']'
        if self.SkeletalElementSide:
            unicode_string = unicode_string+' '+self.SkeletalElementSide
        if self.SkeletalElement:
            unicode_string = unicode_string + ' ' + self.SkeletalElement
        return unicode_string


class Photo(models.Model):
    image = models.ImageField('Image', upload_to='uploads/images/origins', null=True, blank=True)
    fossil = models.ForeignKey(Fossil, on_delete=models.CASCADE, null=True, blank=False)

    def thumbnail(self):
        image_url = os.path.join(self.image.url)
        return u'<a href="{}"><img src="{}" style="width:300px" /></a>'.format(image_url, image_url)

    thumbnail.short_description = 'Image'
    thumbnail.allow_tags = True
    thumbnail.mark_safe = True

    class Meta:
        managed = True
        verbose_name = "Image"
        verbose_name_plural = "Images"