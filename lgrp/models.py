from django.contrib.gis.db import models
from taxonomy.models import Taxon, IdentificationQualifier
from lgrp.ontologies import LGRP_COLLECTOR_CHOICES, LGRP_COLLECTING_METHOD_VOCABULARY, LGRP_BASIS_OF_RECORD_VOCABULARY,\
    LGRP_FINDER_CHOICES, LGRP_ELEMENT_CHOICES, LGRP_ELEMENT_PORTION_CHOICES, LGRP_ELEMENT_NUMBER_CHOICES, \
    LGRP_ELEMENT_MODIFIER_CHOICES, LGRP_SIDE_CHOICES, LGRP_IDENTIFIER_CHOICES, LGRP_WEATHERING_CHOICES
from mysite.ontologies import ITEM_TYPE_VOCABULARY
import os
import utm
from django.contrib.gis.geos import Point


# Occurrence Class and Subclasses
class Occurrence(models.Model):
    geom = models.PointField(srid=4326, blank=True, null=True)  # NOT NULL
    # TODO basis is Null for import Not Null afterwards
    basis_of_record = models.CharField("Basis of Record", max_length=50, blank=True, null=False,
                                       choices=LGRP_BASIS_OF_RECORD_VOCABULARY)  # NOT NULL
    item_type = models.CharField("Item Type", max_length=255, blank=True, null=False,
                                 choices=ITEM_TYPE_VOCABULARY)  # NOT NULL
    # During initial import remove collection code choices. Add later for validation.
    collection_code = models.CharField("Coll Code", max_length=20, blank=True, null=True)
    locality_number = models.IntegerField("Locality", null=True, blank=True)
    # Splitting item number and part allows more fine grained searches
    item_number = models.CharField("Item #",  max_length=10, null=True, blank=True)
    item_part = models.CharField("Item Part", max_length=10, null=True, blank=True)

    # Keep catalog number temporarily, but going forward create method to build from other fields
    # catalog_number = models.CharField("Catalog #", max_length=255, blank=True, null=True)

    #  max length influences size of input widget for TextField but not amount of text stored in DB
    remarks = models.TextField(max_length=500, null=True, blank=True)
    item_scientific_name = models.CharField("Sci Name", max_length=255, null=True, blank=True)
    item_description = models.CharField("Description", max_length=255, blank=True, null=True)
    georeference_remarks = models.TextField(max_length=500, null=True, blank=True)
    collecting_method = models.CharField(max_length=50,
                                         choices=LGRP_COLLECTING_METHOD_VOCABULARY, null=True, blank=True)
    related_catalog_items = models.CharField("Related Catalog Items", max_length=50, null=True, blank=True)
    field_number = models.CharField(max_length=50, null=True, blank=True)
    collector = models.CharField(max_length=50, blank=True, null=True, choices=LGRP_COLLECTOR_CHOICES)
    finder = models.CharField(null=True, blank=True, max_length=50, choices=LGRP_FINDER_CHOICES)
    disposition = models.CharField(max_length=255, blank=True, null=True)
    collection_remarks = models.TextField(max_length=500, null=True, blank=True)
    date_recorded = models.DateTimeField(blank=True, null=True, editable=True)
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
    analytical_unit_1 = models.CharField(max_length=255, blank=True, null=True)
    analytical_unit_2 = models.CharField(max_length=255, blank=True, null=True)
    analytical_unit_3 = models.CharField(max_length=255, blank=True, null=True)
    analytical_unit_found = models.CharField(max_length=255, blank=True, null=True)
    analytical_unit_likely = models.CharField(max_length=255, blank=True, null=True)
    analytical_unit_simplified = models.CharField(max_length=255, blank=True, null=True)
    in_situ = models.BooleanField(default=False)
    ranked = models.BooleanField(default=False)
    geology_remarks = models.TextField(max_length=500, null=True, blank=True)
    image = models.FileField(max_length=255, blank=True, upload_to="uploads/images/lgrp", null=True)
    weathering = models.SmallIntegerField(blank=True, null=True, choices=LGRP_WEATHERING_CHOICES)
    surface_modification = models.CharField(max_length=255, blank=True, null=True)
    problem = models.BooleanField(default=False)
    problem_comment = models.TextField(max_length=255, blank=True, null=True)
    barcode = models.IntegerField("Barcode", null=True, blank=True)
    date_last_modified = models.DateTimeField("Modified", auto_now=True)
    objects = models.GeoManager()
    old_cat_number = models.CharField(max_length=255, blank=True, null=True)

    # LGRP Specific Fields
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
            catalog_number_string = str(self.collection_code) + " " + str(self.barcode)
            return catalog_number_string.replace('None', '').replace('- ', '')  # replace None with empty string
        else:
            return None

    def old_catalog_number(self):
        """
        Generate a pretty string formated catalog number from constituent fields
        :return: old version of catalog number as string
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

            catalog_number_string = str(self.collection_code) + " " + str(self.locality_number) + item_text
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
        """
        Field names from model
        :return: list with all field names
        """
        field_list = self._meta.get_fields()  # produce a list of field objects
        return [f.name for f in field_list]  # return a list of names from each field

    def get_foreign_key_field_names(self):
        """
        Get foreign key fields
        :return: returns a list of for key field names
        """
        field_list = self._meta.get_fields()  # produce a list of field objects
        return [f.name for f in field_list if f.is_relation]  # return a list of names for fk fields

    def get_concrete_field_names(self):
        """
        Get field names that correspond to columns in the DB
        :return: returns a lift
        """
        field_list = self._meta.get_fields()
        return [f.name for f in field_list if f.concrete]

    class Meta:
        verbose_name = "LGRP Occurrence"
        verbose_name_plural = "LGRP Occurrences"
        ordering = ["collection_code", "item_number", "item_part"]


class Biology(Occurrence):
    taxon = models.ForeignKey(Taxon,
                              default=0, on_delete=models.SET_DEFAULT,  # prevent deletion when taxa deleted
                              related_name='lgrp_taxon_bio_occurrences')
    identification_qualifier = models.ForeignKey(IdentificationQualifier,
                                                 on_delete=models.SET_NULL,
                                                 related_name='lgrp_id_qualifier_bio_occurrences',
                                                 null=True, blank=True)
    qualifier_taxon = models.ForeignKey(Taxon, null=True, blank=True,
                                        on_delete=models.SET_NULL,
                                        related_name='lgrp_qualifier_taxon_bio_occurrences')
    verbatim_taxon = models.CharField(null=True, blank=True, max_length=1024)
    taxonomy_remarks = models.TextField(max_length=500, null=True, blank=True)
    verbatim_identification_qualifier = models.CharField(null=True, blank=True, max_length=255)

    identified_by = models.CharField(null=True, blank=True, max_length=100, choices=LGRP_IDENTIFIER_CHOICES)
    year_identified = models.IntegerField(null=True, blank=True)
    type_status = models.CharField(null=True, blank=True, max_length=50)
    sex = models.CharField(null=True, blank=True, max_length=50)
    life_stage = models.CharField(null=True, blank=True, max_length=50)
    biology_remarks = models.TextField(max_length=500, null=True, blank=True)
    preparations = models.CharField(null=True, blank=True, max_length=50)
    morphobank_number = models.IntegerField(null=True, blank=True)
    side = models.CharField(null=True, blank=True, max_length=50, choices=LGRP_SIDE_CHOICES)
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
    element = models.CharField(null=True, blank=True, max_length=50, choices=LGRP_ELEMENT_CHOICES)
    element_modifier = models.CharField(null=True, blank=True, max_length=50, choices=LGRP_ELEMENT_MODIFIER_CHOICES)
    element_portion = models.CharField(null=True, blank=True, max_length=50, choices=LGRP_ELEMENT_PORTION_CHOICES)
    element_number = models.CharField(null=True, blank=True, max_length=50, choices=LGRP_ELEMENT_NUMBER_CHOICES)
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
    element_remarks = models.TextField(max_length=500, null=True, blank=True)

    class Meta:
        verbose_name = "LGRP Biology"
        verbose_name_plural = "LGRP Biology"

    def __unicode__(self):
        return str(self.id)
        #return str(self.taxon.__unicode__())


class Archaeology(Occurrence):
    find_type = models.CharField(null=True, blank=True, max_length=255)
    length_mm = models.DecimalField(max_digits=38, decimal_places=8, null=True, blank=True)
    width_mm = models.DecimalField(max_digits=38, decimal_places=8, null=True, blank=True)

    class Meta:
        verbose_name = "LGRP Archaeology"
        verbose_name_plural = "LGRP Archaeology"


class Geology(Occurrence):
    find_type = models.CharField(null=True, blank=True, max_length=255)
    dip = models.DecimalField(max_digits=38, decimal_places=8, null=True, blank=True)
    strike = models.DecimalField(max_digits=38, decimal_places=8, null=True, blank=True)
    color = models.CharField(null=True, blank=True, max_length=255)
    texture = models.CharField(null=True, blank=True, max_length=255)

    class Meta:
        verbose_name = "LGRP Geology"
        verbose_name_plural = "LGRP Geology"


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
        verbose_name = "LGRP Hydrology"
        verbose_name_plural = "LGRP Hydrology"


# Media Classes
class Image(models.Model):
    # occurrence = models.ForeignKey("Occurrence")
    occurrence = models.ForeignKey("Occurrence", related_name='images')
    image = models.ImageField(upload_to="uploads/images", null=True, blank=True)
    description = models.TextField(null=True, blank=True)


class File(models.Model):
    occurrence = models.ForeignKey("Occurrence")
    file = models.FileField(upload_to="uploads/files", null=True, blank=True)
    description = models.TextField(null=True, blank=True)
