from django.contrib.gis.db import models
from taxonomy.models import Taxon, IdentificationQualifier
from mysite.ontologies import ITEM_TYPE_VOCABULARY, HRP_COLLECTOR_CHOICES, \
    HRP_COLLECTING_METHOD_VOCABULARY, HRP_BASIS_OF_RECORD_VOCABULARY, HRP_COLLECTION_CODES
import os
import utm
from django.contrib.gis.geos import Point


# Locality Class
class Locality(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    collection_code = models.CharField(null=True, blank=True, choices=HRP_COLLECTION_CODES, max_length=10)
    locality_number = models.IntegerField(null=True, blank=True)
    sublocality = models.CharField(null=True, blank=True, max_length=50)
    description = models.TextField(null=True, blank=True, max_length=255)
    stratigraphic_section = models.CharField(null=True, blank=True, max_length=50)
    upper_limit_in_section = models.IntegerField(null=True, blank=True)
    lower_limit_in_section = models.DecimalField(max_digits=38, decimal_places=8, null=True, blank=True)
    error_notes = models.CharField(max_length=255, null=True, blank=True)
    notes = models.CharField(max_length=254, null=True, blank=True)
    geom = models.PointField(srid=4326, blank=True, null=True)
    date_last_modified = models.DateTimeField("Date Last Modified", auto_now=True)
    objects = models.GeoManager()

    def __unicode__(self):
        nice_name = str(self.collection_code) + " " + str(self.locality_number) + str(self.sublocality)
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
        verbose_name = "HRP Locality"
        verbose_name_plural = "HRP Localities"
        ordering = ("locality_number", "sublocality")


# Occurrence Class and Subclasses
class Occurrence(models.Model):
    geom = models.PointField(srid=4326, blank=True, null=True)  # NOT NULL
    # TODO basis is Null for import Not Null afterwards
    basis_of_record = models.CharField("Basis of Record", max_length=50, blank=True, null=False,
                                       choices=HRP_BASIS_OF_RECORD_VOCABULARY)  # NOT NULL
    item_type = models.CharField("Item Type", max_length=255, blank=True, null=False,
                                 choices=ITEM_TYPE_VOCABULARY)  # NOT NULL
    # During initial import remove collection code choices. Add later for validation.
    collection_code = models.CharField("Collection Code", max_length=20, blank=True, null=True)
    # Foreign key to locality table
    locality = models.ForeignKey(Locality, null=True, blank=True)
    # Splitting item number and part allows more fine grained searches
    item_number = models.IntegerField("Item #", null=True, blank=True)
    item_part = models.CharField("Item Part", max_length=10, null=True, blank=True)
    # Keep catalog number temporarily, but going forward create method to build from other fields
    # catalog_number = models.CharField("Catalog #", max_length=255, blank=True, null=True)
    remarks = models.TextField("Remarks", null=True, blank=True, max_length=2500)
    item_scientific_name = models.CharField("Sci Name", max_length=255, null=True, blank=True)
    item_description = models.CharField("Description", max_length=255, blank=True, null=True)
    georeference_remarks = models.TextField(max_length=50, null=True, blank=True)
    collecting_method = models.CharField(max_length=50,
                                         choices=HRP_COLLECTING_METHOD_VOCABULARY, null=True)
    related_catalog_items = models.CharField("Related Catalog Items", max_length=50, null=True, blank=True)
    field_number = models.CharField(max_length=50, null=True, blank=True)
    collector = models.CharField(max_length=50, blank=True, null=True, choices=HRP_COLLECTOR_CHOICES)
    finder = models.CharField(null=True, blank=True, max_length=50)
    disposition = models.CharField(max_length=255, blank=True, null=True)
    collection_remarks = models.TextField("Remarks", null=True, blank=True, max_length=255)
    date_recorded = models.DateTimeField(blank=True, null=True, editable=True)  # NOT NULL
    year_collected = models.IntegerField(blank=True, null=True)
    individual_count = models.IntegerField(blank=True, null=True, default=1)
    preparation_status = models.CharField(max_length=50, blank=True, null=True)
    stratigraphic_marker_upper = models.CharField(max_length=255, blank=True, null=True)
    distance_from_upper = models.DecimalField(max_digits=38, decimal_places=8, blank=True, null=True)
    stratigraphic_marker_lower = models.CharField(max_length=255, blank=True, null=True)
    distance_from_lower = models.DecimalField(max_digits=38, decimal_places=8, blank=True, null=True)
    stratigraphic_marker_found = models.CharField(max_length=255, blank=True, null=True)
    distance_from_found = models.DecimalField(max_digits=38, decimal_places=8, blank=True, null=True)
    stratigraphic_marker_likely = models.CharField(max_length=255, blank=True, null=True)
    distance_from_likely = models.DecimalField(max_digits=38, decimal_places=8, blank=True, null=True)
    stratigraphic_formation = models.CharField(max_length=255, blank=True, null=True)
    stratigraphic_member = models.CharField(max_length=255, blank=True, null=True)
    analytical_unit = models.CharField(max_length=255, blank=True, null=True)
    analytical_unit_2 = models.CharField(max_length=255, blank=True, null=True)
    analytical_unit_3 = models.CharField(max_length=255, blank=True, null=True)
    analytical_unit_found = models.CharField(max_length=255, blank=True, null=True)
    analytical_unit_likely = models.CharField(max_length=255, blank=True, null=True)
    analytical_unit_simplified = models.CharField(max_length=255, blank=True, null=True)
    in_situ = models.BooleanField(default=False)
    ranked = models.BooleanField(default=False)
    image = models.FileField(max_length=255, blank=True, upload_to="uploads/images/hrp", null=True)
    weathering = models.SmallIntegerField(blank=True, null=True)
    surface_modification = models.CharField(max_length=255, blank=True, null=True)
    problem = models.BooleanField(default=False)
    problem_comment = models.TextField(max_length=255, blank=True, null=True)
    barcode = models.IntegerField("Barcode", null=True, blank=True)
    date_last_modified = models.DateTimeField("Date Last Modified", auto_now=True)
    objects = models.GeoManager()

    # HRP Specific Fields
    drainage_region = models.CharField(null=True, blank=True, max_length=255)

    @staticmethod
    def fields_to_display():
        fields = ("id", "barcode")
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

    def catalog_number(self):
        """
        Generate a pretty string formatted catalog number from constituent fields
        :return: catalog number as string
        """

        if self.basis_of_record == 'Collection':
            #  Crate catalog number string. Null values become None when converted to string
            if self.item_number:
                if self.item_part:
                    item_text = '-' + str(self.item_number) + str(self.item_part)
                else:
                    item_text = '-' + str(self.item_number)
            else:
                item_text = ''

            catalog_number_string = str(self.collection_code) + " " + str(self.locality_id) + item_text
            return catalog_number_string.replace('None', '').replace('- ', '')  # replace None with empty string
        else:
            return None

    def __unicode__(self):
        nice_name = str(self.catalog_number()) + ' ' + '[' + str(self.item_scientific_name) + ' ' \
                    + str(self.item_description) + "]"
        return nice_name.replace("None", "").replace("--", "")

    def save(self, *args, **kwargs):
        """
        Custom save method for Occurrence objects. Automatically updates catalog_number field
        :param args:
        :param kwargs:
        :return:
        """
        # The following code automatically updates the catalog number field. It is commented out for
        # now to experiment with a model that does not have a dedicated catalog number field in the database,
        # but uses a method to dynamically construct a catalog number as necessary.
        # the_catalog_number = str(self.collection_code) + " " + str(self.paleolocality_number) + \
        #                      str(self.paleo_sublocality) + "-" + str(self.item_number) + str(self.item_part)
        # self.catalog_number = the_catalog_number.replace("None", "")

        # call the normal hrp_occurrence save method using alternate database
        super(Occurrence, self).save(*args, **kwargs)

    def photo(self):
        try:
            return u'<a href="%s"><img src="%s" style="width:600px" /></a>' \
                   % (os.path.join(self.image.url), os.path.join(self.image.url))
        except:
            return None
    photo.short_description = 'Photo'
    photo.allow_tags = True
    photo.mark_safe = True

    def thumbnail(self):
        try:
            return u'<a href="%s"><img src="%s" style="width:100px" /></a>' \
                   % (os.path.join(self.image.url), os.path.join(self.image.url))
        except:
            return None
    thumbnail.short_description = 'Thumb'
    thumbnail.allow_tags = True
    thumbnail.mark_safe = True

    def get_all_field_names(self):
        return self._meta.get_all_field_names()

    class Meta:
        verbose_name = "HRP Occurrence"
        verbose_name_plural = "HRP Occurrences"
        ordering = ["collection_code", "locality", "item_number", "item_part"]


class Biology(Occurrence):
    verbatim_taxon = models.CharField(null=True, blank=True, max_length=1024)
    taxon = models.ForeignKey(Taxon, related_name='hrp_biology_occurrences')
    verbatim_identification_qualifier = models.CharField(null=True, blank=True, max_length=255)
    identification_qualifier = models.ForeignKey(IdentificationQualifier, related_name='hrp_biology_occurrences',
                                                 null=True, blank=True)
    qualifier_taxon = models.ForeignKey(Taxon, null=True, blank=True)
    identified_by = models.CharField(null=True, blank=True, max_length=100)
    year_identified = models.IntegerField(null=True, blank=True)
    type_status = models.CharField(null=True, blank=True, max_length=50)
    sex = models.CharField(null=True, blank=True, max_length=50)
    life_stage = models.CharField(null=True, blank=True, max_length=50)
    preparations = models.CharField(null=True, blank=True, max_length=50)
    morphobank_number = models.IntegerField(null=True, blank=True)
    side = models.CharField(null=True, blank=True, max_length=50)
    attributes = models.CharField(null=True, blank=True, max_length=50)
    fauna_notes = models.TextField(null=True, blank=True, max_length=64000)
    tooth_upper_or_lower = models.CharField(null=True, blank=True, max_length=50)
    tooth_number = models.CharField(null=True, blank=True, max_length=50)
    tooth_type = models.CharField(null=True, blank=True, max_length=50)
    um_tooth_row_length_mm = models.DecimalField(max_digits=38, decimal_places=8, null=True, blank=True)
    um_1_length_mm = models.DecimalField(max_digits=38, decimal_places=8, null=True, blank=True)
    um_1_width_mm = models.DecimalField(max_digits=38, decimal_places=8, null=True, blank=True)
    um_2_length_mm = models.DecimalField(max_digits=38, decimal_places=8, null=True, blank=True)
    um_2_width_mm = models.DecimalField(max_digits=38, decimal_places=8, null=True, blank=True)
    um_3_length_mm = models.DecimalField(max_digits=38, decimal_places=8, null=True, blank=True)
    um_3_width_mm = models.DecimalField(max_digits=38, decimal_places=8, null=True, blank=True)
    lm_tooth_row_length_mm = models.DecimalField(max_digits=38, decimal_places=8, null=True, blank=True)
    lm_1_length = models.DecimalField(max_digits=38, decimal_places=8, null=True, blank=True)
    lm_1_width = models.DecimalField(max_digits=38, decimal_places=8, null=True, blank=True)
    lm_2_length = models.DecimalField(max_digits=38, decimal_places=8, null=True, blank=True)
    lm_2_width = models.DecimalField(max_digits=38, decimal_places=8, null=True, blank=True)
    lm_3_length = models.DecimalField(max_digits=38, decimal_places=8, null=True, blank=True)
    lm_3_width = models.DecimalField(max_digits=38, decimal_places=8, null=True, blank=True)
    element = models.CharField(null=True, blank=True, max_length=50)
    element_modifier = models.CharField(null=True, blank=True, max_length=50)
    # upper dentition fields
    uli1 = models.BooleanField(default=False)
    uli2 = models.BooleanField(default=False)
    uli3 = models.BooleanField(default=False)
    uli4 = models.BooleanField(default=False)
    uli5 = models.BooleanField(default=False)
    uri1 = models.BooleanField(default=False)
    uri2 = models.BooleanField(default=False)
    uri3 = models.BooleanField(default=False)
    uri4 = models.BooleanField(default=False)
    uri5 = models.BooleanField(default=False)
    ulc = models.BooleanField(default=False)
    urc = models.BooleanField(default=False)
    ulp1 = models.BooleanField(default=False)
    ulp2 = models.BooleanField(default=False)
    ulp3 = models.BooleanField(default=False)
    ulp4 = models.BooleanField(default=False)
    urp1 = models.BooleanField(default=False)
    urp2 = models.BooleanField(default=False)
    urp3 = models.BooleanField(default=False)
    urp4 = models.BooleanField(default=False)
    ulm1 = models.BooleanField(default=False)
    ulm2 = models.BooleanField(default=False)
    ulm3 = models.BooleanField(default=False)
    urm1 = models.BooleanField(default=False)
    urm2 = models.BooleanField(default=False)
    urm3 = models.BooleanField(default=False)
    # lower dentition fields
    lli1 = models.BooleanField(default=False)
    lli2 = models.BooleanField(default=False)
    lli3 = models.BooleanField(default=False)
    lli4 = models.BooleanField(default=False)
    lli5 = models.BooleanField(default=False)
    lri1 = models.BooleanField(default=False)
    lri2 = models.BooleanField(default=False)
    lri3 = models.BooleanField(default=False)
    lri4 = models.BooleanField(default=False)
    lri5 = models.BooleanField(default=False)
    llc = models.BooleanField(default=False)
    lrc = models.BooleanField(default=False)
    llp1 = models.BooleanField(default=False)
    llp2 = models.BooleanField(default=False)
    llp3 = models.BooleanField(default=False)
    llp4 = models.BooleanField(default=False)
    lrp1 = models.BooleanField(default=False)
    lrp2 = models.BooleanField(default=False)
    lrp3 = models.BooleanField(default=False)
    lrp4 = models.BooleanField(default=False)
    llm1 = models.BooleanField(default=False)
    llm2 = models.BooleanField(default=False)
    llm3 = models.BooleanField(default=False)
    lrm1 = models.BooleanField(default=False)
    lrm2 = models.BooleanField(default=False)
    lrm3 = models.BooleanField(default=False)
    # indeterminate dental fields
    indet_incisor = models.BooleanField(default=False)
    indet_canine = models.BooleanField(default=False)
    indet_premolar = models.BooleanField(default=False)
    indet_molar = models.BooleanField(default=False)
    indet_tooth = models.BooleanField(default=False)
    deciduous = models.BooleanField(default=False)

    class Meta:
        verbose_name = "HRP Biology"
        verbose_name_plural = "HRP Biology"

    def __unicode__(self):
        return str(self.taxon.__unicode__())


class Archaeology(Occurrence):
    find_type = models.CharField(null=True, blank=True, max_length=255)
    length_mm = models.DecimalField(max_digits=38, decimal_places=8, null=True, blank=True)
    width_mm = models.DecimalField(max_digits=38, decimal_places=8, null=True, blank=True)

    class Meta:
        verbose_name = "HRP Archaeology"
        verbose_name_plural = "HRP Archaeology"


class Geology(Occurrence):
    find_type = models.CharField(null=True, blank=True, max_length=255)
    dip = models.DecimalField(max_digits=38, decimal_places=8, null=True, blank=True)
    strike = models.DecimalField(max_digits=38, decimal_places=8, null=True, blank=True)
    color = models.CharField(null=True, blank=True, max_length=255)
    texture = models.CharField(null=True, blank=True, max_length=255)

    class Meta:
        verbose_name = "HRP Geology"
        verbose_name_plural = "HRP Geology"


# Hydrology Class
class Hydrology(models.Model):
    length = models.DecimalField(max_digits=38, decimal_places=8, null=True, blank=True)
    name = models.CharField(null=True, blank=True, max_length=50)
    size = models.IntegerField(null=True, blank=True)
    map_sheet = models.CharField(null=True, blank=True, max_length=50)
    geom = models.LineStringField(srid=4326)
    objects = models.GeoManager()

    def __unicode__(self):
        return str(self.name)

    class Meta:
        verbose_name = "HRP Hydrology"
        verbose_name_plural = "HRP Hydrology"


# Media Classes
class Image(models.Model):
    occurrence = models.ForeignKey("Occurrence", related_name='hrp_occurrences')
    image = models.ImageField(upload_to="uploads/images", null=True, blank=True)
    description = models.TextField(null=True, blank=True)


class File(models.Model):
    occurrence = models.ForeignKey("Occurrence")
    file = models.FileField(upload_to="uploads/files", null=True, blank=True)
    description = models.TextField(null=True, blank=True)
