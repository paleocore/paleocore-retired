from django.contrib.gis.db import models
from psr.ontologies import *
from django.contrib.gis.geos import Point
import utm


class TaxonRank(models.Model):
    """
    The hierarchical rank of a biological taxon, e.g. 'Genus'
    """
    name = models.CharField(null=False, blank=False, max_length=50, unique=True,
                            help_text='The name of the taxonomic rank, such as Order, Family, Genus etc.')
    """
    The name of the taxonomic rank, such as the standards from the Linnaen hierarchy of
    Kingdom, Phylum, Class, Order, Family, Genus, Species as well as more esoteric ranks including
    Division, Subfamily, Tribe etc.
    """

    plural = models.CharField(null=False, blank=False, max_length=50, unique=True,
                              help_text='The plural form of the taxonomic rank name, such as Orders, Families, Genera')
    """
    The plural form of the taxonomic rank name, such as Genera as the plural for Genus.
    """

    ordinal = models.IntegerField(null=False, blank=False, unique=True,
                                  help_text='The Numeric rank of taxon category. Lower numbers indicate broader '
                                            'categories.')
    """
    The numeric rank of the taxonomic category. The root rank has value 0 and more restrictive ranks have
    higher values. As a rule of thumb the major levels in the hierarchy are ten units apart, e.g. Kingdom
    has a value of 10 and Phylum a value of 20.
    """

    def __unicode__(self):
        return str(self.name)


class Taxon(models.Model):
    """
    Named groupings of organisms, i.e. taxa.
    """
    name = models.CharField(null=False, blank=False, max_length=255, unique=False,
                            help_text='The name of the taxon, e.g. sapiens')
    """
    Names for species store only the trivial portion (or smaller) or the species name rather than the full binomen.
    For example the species name for 'Homo sapiens' is just 'sapiens'.
    The unicode method shows the name for ranks for Genus and higher, and shows the binomen for species.
    """

    parent = models.ForeignKey('self', null=True, blank=True,
                               help_text='The parent taxon.')
    """
    A pointer to the parent taxon object.
    """

    rank = models.ForeignKey(TaxonRank, help_text='The Linnaen rank of the taxon, e.g. Order, Genus etc.')
    """
    The taxonomic rank of the taxon, e.g. Order, Genus.
    Many-to-one foreign key to the TaxonRank table.
    """

    def parent_rank(self):
        """
        The rank of the parent taxon
        :return: The parent taxon name as a string.
        """
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
        verbose_name_plural = "taxa"
        ordering = ['rank__ordinal', 'name']


# Locality Class
class Locality(models.Model):
    """
    dwc: locality
    Locality class for recording information about general locations and places
    """
    id = models.CharField(primary_key=True, max_length=255)
    """
    Unique database identifier and primary key for localities.
    """

    collection_code = models.CharField(null=True, blank=True, max_length=10, choices=PSR_COLLECTION_CODES)
    """
    dwc:collectionCode
    A short string indicating the collection area.
    """

    locality_type = models.CharField(null=True, blank=True, max_length=255, choices=PSR_LOCALITY_TYPE)
    """
    The physical type of the locality, e.g. rockshelter, cave etc.
    """

    slope = models.IntegerField(null=True, blank=True)
    """
    The steepness of the terrain, measured in degrees from 0-90
    """

    aspect = models.CharField(null=True, blank=True, max_length=10, choices=PSR_ASPECT_CHOICES)
    """
    The direction or orientation of the slope in cardinal directions (N, NW etc).
    """

    remarks = models.TextField(null=True, blank=True, max_length=255)
    """
    General comments about the locality.
    """

    group = models.CharField(null=True, blank=True, max_length=255)
    """
    dwc: group
    The stratigraphic group the locality is in.
    """

    formation = models.CharField(null=True, blank=True, max_length=255)
    """
    dwc: formation
    The stratigraphic formation of the locality.
    """

    member = models.CharField(null=True, blank=True, max_length=255)
    """
    dwc: member
    The stratigraphic member of the locality.
    """

    bed = models.CharField(null=True, blank=True, max_length=255)
    """
    dwc:bed
    The stratigraphic bed of the locality.
    """

    modified = models.DateTimeField("Date Last Modified", auto_now=True)
    """
    dwc: modified
    The date and time the locality record was last modified.
    """

    geom = models.PointField(srid=4326, blank=True, null=True)
    """
    The geographic spatial location in geographic coordinates using the WGS84 datum.
    """

    objects = models.GeoManager()
    """
    The spatial ojbects manageer. Internal attribute for managing geospatial objects.
    """

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
    """
    Class Find (temporarily named Occurrence for backward compatibility)
    """

    # TODO basis is Null for import Not Null afterwards
    basis_of_record = models.CharField("Basis of Record", max_length=50, blank=True, null=False,
                                       choices=PSR_BASIS_OF_RECORD_VOCABULARY,
                                       help_text= 'The type of collection, e.g. Observation or Collection')
    """
    dwc:basisOfRecord
    The evidentiary basis for the record. This field records whether the record is based on a visual observation
    or a collected specimen.
    Controlled vocabulary: Observation, Collection
    """

    item_type = models.CharField("Item Type", max_length=255, blank=True, null=False,
                                 choices=PSR_ITEM_TYPE_VOCABULARY)  # NOT NULL
    """
    The type of collection, e.g. faunal, floral, archaeological, geological.
    This field duplicates the subclassing and is perhaps redundant.
    """



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

    locality = models.ForeignKey(Locality, null=True, blank=True)  # Foreign key to locality table
    geom = models.PointField(srid=4326, blank=True, null=True)  # NOT NULL
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








