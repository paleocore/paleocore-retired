from django.contrib.gis.db import models
from taxonomy.models import Taxon, IdentificationQualifier
from lgrp.ontologies import LGRP_COLLECTOR_CHOICES, LGRP_COLLECTING_METHOD_VOCABULARY, LGRP_BASIS_OF_RECORD_VOCABULARY,\
    LGRP_FINDER_CHOICES, LGRP_ELEMENT_CHOICES, LGRP_ELEMENT_PORTION_CHOICES, LGRP_ELEMENT_NUMBER_CHOICES, \
    LGRP_ELEMENT_MODIFIER_CHOICES, LGRP_SIDE_CHOICES, LGRP_IDENTIFIER_CHOICES, LGRP_WEATHERING_CHOICES, \
    LGRP_COLLECTION_CODES
from mysite.ontologies import ITEM_TYPE_VOCABULARY
import os
import utm
from django.contrib.gis.geos import Point


# Occurrence Class and Subclasses
class Occurrence(models.Model):
    """
    Occurrence == Find, a general class for things discovered in the field.
    Find's have three subtypes: Archaeology, Biology, Geology
    Fields are grouped by comments into logical sets (i.e. ontological classes)
    """
    # Record
    date_last_modified = models.DateTimeField("Modified", auto_now=True,
                                              help_text='The date and time this resource was last altered.')  # dwc:modified
    basis_of_record = models.CharField("Basis of Record", max_length=50, blank=True, null=False,
                                       help_text='e.g. Observed item or Collected item',
                                       choices=LGRP_BASIS_OF_RECORD_VOCABULARY)  # NOT NULL, dwc:basisOfRecord
    problem = models.BooleanField(default=False,
                                  help_text='Is there a problem with this record that needs attention?')
    problem_comment = models.TextField(max_length=255, blank=True, null=True,
                                       help_text='Description of the problem.')
    remarks = models.TextField("Record Remarks", max_length=500, null=True, blank=True,
                               help_text='General remarks about this database record.')

    # Event
    date_recorded = models.DateTimeField("Date Rec", blank=True, null=True, editable=True,
                                         help_text='Date and time the item was observed or collected.')
    year_collected = models.IntegerField("Year", blank=True, null=True,
                                         help_text='The year, event or field campaign during which the item was found.')

    # Find
    barcode = models.IntegerField("Barcode", null=True, blank=True,
                                  help_text='For collected items only.')  # dwc:recordNumber
    field_number = models.CharField(max_length=50, null=True, blank=True)  # dwc:fieldNumber
    item_type = models.CharField("Item Type", max_length=255, blank=True, null=False, choices=ITEM_TYPE_VOCABULARY)
    # TODO merge with taxon
    item_scientific_name = models.CharField("Sci Name", max_length=255, null=True, blank=True)  # dwc:scientificName
    # TODO merge with element
    item_description = models.CharField("Description", max_length=255, blank=True, null=True)  # merge with element
    item_count = models.IntegerField(blank=True, null=True, default=1)

    collector = models.CharField(max_length=50, blank=True, null=True, choices=LGRP_COLLECTOR_CHOICES)  # dwc:recordedBy
    finder = models.CharField(null=True, blank=True, max_length=50, choices=LGRP_FINDER_CHOICES)
    collecting_method = models.CharField(max_length=50,
                                         choices=LGRP_COLLECTING_METHOD_VOCABULARY,
                                         null=True, blank=True)  # dwc:sampling_protocol
    locality_number = models.IntegerField("Locality", null=True, blank=True)
    item_number = models.CharField("Item #", max_length=10, null=True, blank=True)
    item_part = models.CharField("Item Part", max_length=10, null=True, blank=True)
    old_cat_number = models.CharField("Old Cat Number", max_length=255, blank=True, null=True)
    disposition = models.CharField(max_length=255, blank=True, null=True)  # dwc:disposition
    preparation_status = models.CharField(max_length=50, blank=True, null=True)  # Drop? - 2 specimens with entries
    # TODO rename collection_remarks to find_remarks
    collection_remarks = models.TextField(max_length=500, null=True, blank=True)  # dwc:occurrence_remarks

    # Geological Context
    stratigraphic_formation = models.CharField("Formation", max_length=255, blank=True, null=True)  # dwc:formation
    stratigraphic_member = models.CharField("Member", max_length=255, blank=True, null=True)  # dwc:member
    analytical_unit_1 = models.CharField(max_length=255, blank=True, null=True)
    analytical_unit_2 = models.CharField(max_length=255, blank=True, null=True)
    analytical_unit_3 = models.CharField(max_length=255, blank=True, null=True)
    analytical_unit_found = models.CharField(max_length=255, blank=True, null=True)
    analytical_unit_likely = models.CharField(max_length=255, blank=True, null=True)
    analytical_unit_simplified = models.CharField(max_length=255, blank=True, null=True)  # dwc:bed
    in_situ = models.BooleanField(default=False)
    ranked = models.BooleanField(default=False)  # Drop? One record is True
    weathering = models.SmallIntegerField(blank=True, null=True, choices=LGRP_WEATHERING_CHOICES)
    surface_modification = models.CharField(max_length=255, blank=True, null=True)
    geology_remarks = models.TextField(max_length=500, null=True, blank=True)

    # Location
    # TODO merge collection_code and drainage region
    collection_code = models.CharField("Coll Code", max_length=20, blank=True, null=True,
                                       choices=LGRP_COLLECTION_CODES)  # dwc:collectionCode, change to locality?
    drainage_region = models.CharField(null=True, blank=True, max_length=255)  # merge with collection_code?
    georeference_remarks = models.TextField(max_length=500, null=True, blank=True)
    geom = models.PointField(srid=4326, blank=True, null=True)  # NOT NULL  dwc:footprintWKT
    objects = models.GeoManager()

    # Media
    image = models.FileField(max_length=255, blank=True, upload_to="uploads/images/lgrp", null=True)

    @staticmethod
    def fields_to_display():
        fields = ("id", "barcode")
        return fields

    @staticmethod
    def method_fields_to_export():
        """
        Method to store a list of fields that should be added to data exports.
        Called by export admin actions.
        These fields are defined in methods and are not concrete fields in the DB so have to be declared.
        :return:
        """
        return ['longitude', 'latitude', 'easting', 'northing', 'catalog_number', 'photo']

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
        try:
            if self.geom.srid == 4326:
                return self.geom.x
            else:
                gcs_point = self.geom.transform(4326, clone=True)  # transform a clone of original point
                return gcs_point.x
        except AttributeError:
            return None

    def latitude(self):
        """
        Return the latitude for the point in the WGS84 datum
        :return:
        """
        try:
            if self.geom.srid == 4326:
                return self.geom.y
            else:
                gcs_point = self.geom.transform(4326, clone=True)  # transform a clone of original point
                return gcs_point.y
        except AttributeError:
            return None

    def easting(self):
        """
        Return the easting for the point in UTM meters using the WGS84 datum
        :return:
        """
        try:
            if self.geom.srid == 32637:
                return self.geom.x
            else:
                utm_point = self.geom.transform(32637, clone=True)  # get a copy of the point in utm
                return utm_point.x
        except AttributeError:
            return None

    def northing(self):
        """
        Return the easting for the point in UTM meters using the WGS84 datum
        :return:
        """
        try:
            if self.geom.srid == 32637:
                return self.geom.y
            else:
                utm_point = self.geom.transform(32637, clone=True)
                return utm_point.y
        except AttributeError:
            return None

    def catalog_number(self):
        """
        Generate a pretty string formatted catalog number from constituent fields
        dwc: catalogNumber
        :return: catalog number as string
        """

        if self.basis_of_record == 'Collection':
            catalog_number_string = str(self.collection_code) + " " + str(self.barcode)
            return catalog_number_string.replace('None', '').replace('- ', '')  # replace None with empty string
        else:
            return None

    def photo(self):
        try:
            html_string = u'<a href="{}"><img src="{}" style="width:600px" /></a>'
            return html_string.format(os.path.join(self.image.url), os.path.join(self.image.url))
        except:
            return None
    photo.short_description = 'Photo'
    photo.allow_tags = True
    photo.mark_safe = True

    def thumbnail(self):
        try:
            html_string = u'<a href="%s"><img src="%s" style="width:100px" /></a>'
            return html_string.format(os.path.join(self.image.url), os.path.join(self.image.url))
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

    def __unicode__(self):
        nice_name = str(self.catalog_number()) + ' ' + '[' + str(self.item_scientific_name) + ' ' \
                    + str(self.item_description) + "]"
        return nice_name.replace("None", "").replace("--", "")

    class Meta:
        verbose_name = "LGRP Occurrence"
        verbose_name_plural = "LGRP Occurrences"
        ordering = ["collection_code", "item_number", "item_part"]


class Biology(Occurrence):
    # Biology
    sex = models.CharField(null=True, blank=True, max_length=50)
    life_stage = models.CharField(null=True, blank=True, max_length=50)
    biology_remarks = models.TextField(max_length=500, null=True, blank=True)

    # Taxon
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

    # Identification
    identified_by = models.CharField(null=True, blank=True, max_length=100, choices=LGRP_IDENTIFIER_CHOICES)
    year_identified = models.IntegerField(null=True, blank=True)
    type_status = models.CharField(null=True, blank=True, max_length=50)
    verbatim_identification_qualifier = models.CharField(null=True, blank=True, max_length=255)
    fauna_notes = models.TextField(null=True, blank=True, max_length=64000)

    # Element
    side = models.CharField(null=True, blank=True, max_length=50, choices=LGRP_SIDE_CHOICES)

    element = models.CharField(null=True, blank=True, max_length=50, choices=LGRP_ELEMENT_CHOICES)
    element_modifier = models.CharField(null=True, blank=True, max_length=50, choices=LGRP_ELEMENT_MODIFIER_CHOICES)
    element_portion = models.CharField(null=True, blank=True, max_length=50, choices=LGRP_ELEMENT_PORTION_CHOICES)
    element_number = models.CharField(null=True, blank=True, max_length=50, choices=LGRP_ELEMENT_NUMBER_CHOICES)

    tooth_upper_or_lower = models.CharField(null=True, blank=True, max_length=50)
    tooth_number = models.CharField(null=True, blank=True, max_length=50)
    tooth_type = models.CharField(null=True, blank=True, max_length=50)

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

    # Measurements
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

    @staticmethod
    def find_unmatched_values(field_name):
        lgrp_bio = Biology.objects.all()
        values = list(set([getattr(bio, field_name) for bio in lgrp_bio]))
        field = Biology._meta.get_field_by_name(field_name)[0]
        choices = [i[0] for i in field.choices]
        result = [v for v in values if v not in choices]
        if (not result) or result == [None]:
            return (False, None, None)
        else:
            return (True, len(result), result)

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
    image = models.ImageField(upload_to="uploads/images/lgrp", null=True, blank=True)
    description = models.TextField(null=True, blank=True)


class File(models.Model):
    occurrence = models.ForeignKey("Occurrence", related_name='files')
    file = models.FileField(upload_to="uploads/files/lgrp", null=True, blank=True)
    description = models.TextField(null=True, blank=True)
