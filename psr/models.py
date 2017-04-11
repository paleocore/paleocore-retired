from django.contrib.gis.db import models

from .ontologies import *

import utm
from django.contrib.gis.geos import Point


class TaxonRank(models.Model):
    name = models.CharField(null=False, blank=False, max_length=50, unique=True)
    plural = models.CharField(null=False, blank=False, max_length=50, unique=True)
    ordinal = models.IntegerField(null=False, blank=False, unique=True)

    def __unicode__(self):
        return str(self.name)

    class Meta:
        verbose_name = "Taxon Rank"



class Taxon(models.Model):
    name = models.CharField(null=False, blank=False, max_length=255, unique=False)
    parent = models.ForeignKey('self', null=True, blank=True)
    rank = models.ForeignKey(TaxonRank)

    def parent_rank(self):
        return self.parent.rank.name

    def rank_ordinal(self):
        return self.rank.ordinal

    def parent_name(self):
        if self.parent is None:
            return "NA"
        else:
            return self.parent.name

    def full_name(self):
        if self.parent is None:
            return self.name
        elif self.parent.parent is None:
            return self.name
        else:
            return self.parent.full_name() + ", " + self.name

    def full_lineage(self):
        """
        Get a list of taxon object representing the full lineage hierarchy
        :return: list of taxon objects ordered highest rank to lowest
        """
        if self.parent is None:
            return [self]
        if self.parent.parent is None:
            return [self]
        else:
            return self.parent.full_lineage()+[self]

    def __unicode__(self):
        if self.rank.name == 'Species' and self.parent:
            return "[" + self.rank.name + "] " + self.parent.name + " " + self.name
        else:
            return "[" + self.rank.name + "] " + str(self.name)

    class Meta:
        verbose_name = "Taxon"
        verbose_name_plural = "taxa"
        ordering = ['rank__ordinal', 'name']




# Locality Class
class Locality(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    geom = models.PointField(srid=4326, blank=True, null=True)
    collection_code = models.CharField(null=True, blank=True, max_length=10, choices=PSR_COLLECTION_CODES)
    locality_type = models.CharField(null=True, blank=True, max_length=255, choices=PSR_LOCALITY_TYPE)
    slope = models.IntegerField(null=True, blank=True)
    aspect = models.CharField(null=True, blank=True, max_length=10, choices=PSR_ASPECT_CHOICES)
    remarks = models.TextField(null=True, blank=True, max_length=255)
    group = models.CharField(null=True, blank=True, max_length=255)
    formation = models.CharField(null=True, blank=True, max_length=255)
    member = models.CharField(null=True, blank=True, max_length=255)
    bed = models.CharField(null=True, blank=True, max_length=255)
    modified = models.DateTimeField("Date Last Modified", auto_now=True)
    objects = models.GeoManager()

    def __unicode__(self):
        nice_name = str(self.collection_code) + " " + str(self.id)
        return nice_name.replace("None", "").replace("--", "")

    def point_x(self):
        """
        Return the x coordinate for the point in its native coordinate system
        :return:
        """
        if self.geom and type(self.geom) == Point:
            return self.geom.x
        else:
            return None

    def point_y(self):
        """
        Return the y coordinate for the point in its native coordinate system
        :return:
        """
        if self.geom and type(self.geom) == Point:
            return self.geom.y
        else:
            return None

    def longitude(self):
        """
        Return the longitude for the point in the WGS84 datum
        :return:
        """
        if self.geom and type(self.geom) == Point:
            pt = self.geom
            pt.transform(4326)  # transform to GCS WGS84
            return pt.x
        else:
            return None

    def latitude(self):
        """
        Return the latitude for the point in the WGS84 datum
        :return:
        """
        if self.geom and type(self.geom) == Point:
            pt = self.geom
            pt.transform(4326)
            return pt.y
        else:
            return None

    def easting(self):
        """
        Return the easting for the point in UTM meters using the WGS84 datum
        :return:
        """
        try:
            utmPoint = utm.from_latlon(self.geom.coords[1], self.geom.coords[0])
            return utmPoint[0]
        except:
            return 0

    def northing(self):
        """
        Return the easting for the point in UTM meters using the WGS84 datum
        :return:
        """
        if self.geom and type(self.geom) == Point:
            pt = self.geom
            utm_point = utm.from_latlon(pt.y, pt.x)
            return utm_point[0]
        else:
            return None

    class Meta:
        verbose_name = "PSR Locality"
        verbose_name_plural = "PSR Localities"


# Occurrence Class and Subclasses
class Occurrence(models.Model):
    geom = models.PointField(srid=4326, blank=True, null=True)  # NOT NULL
    # TODO basis is Null for import Not Null afterwards
    basis_of_record = models.CharField("Basis of Record", max_length=50, blank=True, null=False,
                                       choices=PSR_BASIS_OF_RECORD_VOCABULARY)  # NOT NULL
    item_type = models.CharField("Item Type", max_length=255, blank=True, null=False,
                                 choices=PSR_ITEM_TYPE_VOCABULARY)  # NOT NULL
    # During initial import remove collection code choices. Add later for validation.
    collection_code = models.CharField(null=True, blank=True, max_length=10, choices=PSR_COLLECTION_CODES)
    catalog_number = models.CharField("Catalog #", max_length=255, blank=True, null=True)
    remarks = models.TextField("Remarks", null=True, blank=True, max_length=2500)

    collecting_method = models.CharField(max_length=50,
                                         choices=PSR_COLLECTING_METHOD_VOCABULARY, null=True)
    recorded_by = models.CharField(max_length=50, blank=True, null=True, choices=PSR_COLLECTOR_CHOICES)
    date_recorded = models.DateTimeField(blank=True, null=True, editable=True)  # NOT NULL
    item_count = models.IntegerField(blank=True, null=True, default=1)
    disposition = models.CharField(max_length=255, blank=True, null=True)
    year_recorded = models.IntegerField(blank=True, null=True)
    in_situ = models.BooleanField(default=False)
    problem = models.BooleanField(default=False)
    problem_comment = models.TextField(max_length=255, blank=True, null=True)
    modified = models.DateTimeField("Date Last Modified", auto_now=True)


    # Foreign key to locality table
    locality = models.ForeignKey(Locality, null=True, blank=True)

    # Define geoManager
    objects = models.GeoManager()

    def __unicode__(self):
        nice_name = self.collection_code + '' + self.catalog_number + ' ' + '[' + str(self.id) + ']'
        return nice_name.replace("None", "").replace("--", "")

    @staticmethod
    def fields_to_display():
        fields = ("id",)
        return fields

    def point_x(self):
        """
        Return the x coordinate for the point in its native coordinate system
        :return:
        """
        if self.geom and type(self.geom) == Point:
            return self.geom.x
        else:
            return None

    def point_y(self):
        """
        Return the y coordinate for the point in its native coordinate system
        :return:
        """
        if self.geom and type(self.geom) == Point:
            return self.geom.y
        else:
            return None

    def longitude(self):
        """
        Return the longitude for the point in the WGS84 datum
        :return:
        """
        if self.geom and type(self.geom) == Point:
            pt = self.geom
            pt.transform(4326)  # transform to GCS WGS84
            return pt.x
        else:
            return None

    def latitude(self):
        """
        Return the latitude for the point in the WGS84 datum
        :return:
        """
        if self.geom and type(self.geom) == Point:
            pt = self.geom
            pt.transform(4326)
            return pt.y
        else:
            return None

    def easting(self):
        """
        Return the easting for the point in UTM meters using the WGS84 datum
        :return:
        """
        try:
            utmPoint = utm.from_latlon(self.geom.coords[1], self.geom.coords[0])
            return utmPoint[0]
        except:
            return None

    def northing(self):
        """
        Return the easting for the point in UTM meters using the WGS84 datum
        :return:
        """
        try:
            utmPoint = utm.from_latlon(self.geom.coords[1], self.geom.coords[0])
            return utmPoint[1]
        except:
            return None

    def get_all_field_names(self):
        return self._meta.get_all_field_names()

    class Meta:
        verbose_name = "PSR Occurrence"
        verbose_name_plural = "PSR Occurrences"


class Biology(Occurrence):
    identified_by = models.CharField(null=True, blank=True, max_length=100)
    year_identified = models.IntegerField(null=True, blank=True)
    type_status = models.CharField(null=True, blank=True, max_length=50)
    sex = models.CharField(null=True, blank=True, max_length=50)
    life_stage = models.CharField(null=True, blank=True, max_length=50)
    biological_preparations = models.CharField(null=True, blank=True, max_length=50)
    element = models.CharField(null=True, blank=True, max_length=50)
    element_modifier = models.CharField(null=True, blank=True, max_length=50)
    side = models.CharField(null=True, blank=True, max_length=50, choices=PSR_SIDE_VOCABULARY)
    bone_weathering = models.SmallIntegerField(blank=True, null=True)
    bone_surface_modification = models.CharField(max_length=255, blank=True, null=True)

    taxon = models.ForeignKey(Taxon, related_name='psr_taxon_bio_occurrences')
    identification_qualifier = models.CharField(max_length=50, null=True, blank=True, choices=PSR_ID_QUALIFIER_VOCABULARY)


    class Meta:
        verbose_name = "PSR Biology"
        verbose_name_plural = "PSR Biology"

    def __unicode__(self):
        return str(self.taxon.__unicode__())


class Archaeology(Occurrence):
    archaeology_type = models.CharField(null=True, blank=True, max_length=255)
    period = models.CharField(null=True, blank=True, max_length=255)
    archaeology_preparations = models.CharField(null=True, blank=True, max_length=255)

    class Meta:
        verbose_name = "PSR Archaeology"
        verbose_name_plural = "PSR Archaeology"


class Geology(Occurrence):
    geology_type = models.CharField(null=True, blank=True, max_length=255)
    dip = models.DecimalField(max_digits=38, decimal_places=8, null=True, blank=True)
    strike = models.DecimalField(max_digits=38, decimal_places=8, null=True, blank=True)
    color = models.CharField(null=True, blank=True, max_length=255)
    texture = models.CharField(null=True, blank=True, max_length=255)

    class Meta:
        verbose_name = "PSR Geology"
        verbose_name_plural = "PSR Geology"


class BulkFind (Occurrence):
    screen_size = models.CharField(max_length=20, blank=True, null=True)
    platform_count = models.IntegerField(blank=True, null=True)
    platform_weight = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        verbose_name_plural = "PSR Small Finds (Summary Counts by bucket)"
        verbose_name = "PSR Small find (bucket)"


# Media Classes
class Image(models.Model):
    occurrence = models.ForeignKey("Occurrence", related_name='psr_occurrences')
    image = models.ImageField(upload_to="uploads/images", null=True, blank=True)
    description = models.TextField(null=True, blank=True)


class File(models.Model):
    occurrence = models.ForeignKey("Occurrence")
    file = models.FileField(upload_to="uploads/files", null=True, blank=True)
    description = models.TextField(null=True, blank=True)


# Event Class
class Event(models.Model):
    start_time = models.DateTimeField(null=True, blank=True)
    end_time = models.DateTimeField(null=True, blank=True)
    description = models.TextField()
    geom = models.GeometryField(null=True, blank=True, srid=4326)
    #objects = models.LineStringField()








