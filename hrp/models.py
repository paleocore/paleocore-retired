from django.contrib.gis.db import models
from taxonomy.models import Taxon, IdentificationQualifier
from .ontologies import *
import os
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

    class Meta:
        verbose_name = "HRP Locality"
        verbose_name_plural = "HRP Localities"
        ordering = ("locality_number", "sublocality")


# Occurrence Class and Subclasses
class Occurrence(models.Model):
    """
        Occurrence == Find, a general class for things discovered in the field.
        Find's have three subtypes: Archaeology, Biology, Geology
        Fields are grouped by comments into logical sets (i.e. ontological classes)
        """
    # Record
    # dwc:modified
    date_last_modified = models.DateTimeField("Modified", auto_now=True,
                                              help_text='The date and time this resource was last altered.')
    basis_of_record = models.CharField("Basis of Record", max_length=50, blank=True, null=False,
                                       help_text='e.g. Observed item or Collected item',
                                       choices=HRP_BASIS_OF_RECORD_VOCABULARY)  # NOT NULL  dwc:basisOfRecord
    problem = models.BooleanField(default=False)
    problem_comment = models.TextField(max_length=255, blank=True, null=True)
    remarks = models.TextField("Remarks", null=True, blank=True, max_length=2500)

    # Event
    date_recorded = models.DateTimeField(blank=True, null=True, editable=True)  # NOT NULL
    year_collected = models.IntegerField(blank=True, null=True)

    # Find
    barcode = models.IntegerField("Barcode", null=True, blank=True)
    field_number = models.CharField(max_length=50, null=True, blank=True)
    item_type = models.CharField("Item Type", max_length=255, blank=True, null=False,
                                 choices=ITEM_TYPE_VOCABULARY)  # NOT NULL
    # TODO merge with taxon
    item_scientific_name = models.CharField("Sci Name", max_length=255, null=True, blank=True)
    # TODO merge with element
    item_description = models.CharField("Description", max_length=255, blank=True, null=True)
    item_count = models.IntegerField(blank=True, null=True, default=1)
    collector = models.CharField(max_length=50, blank=True, null=True, choices=HRP_COLLECTOR_CHOICES)
    finder = models.CharField(null=True, blank=True, max_length=50)
    collecting_method = models.CharField(max_length=50,
                                         choices=HRP_COLLECTING_METHOD_VOCABULARY,
                                         null=True, blank=True)
    locality = models.ForeignKey(Locality, null=True, blank=True)  # dwc:sampling_protocol
    item_number = models.IntegerField("Item #", null=True, blank=True)
    item_part = models.CharField("Item Part", max_length=10, null=True, blank=True)
    cat_number = models.CharField("Cat Number", max_length=255, blank=True, null=True)
    disposition = models.CharField(max_length=255, blank=True, null=True)
    preparation_status = models.CharField(max_length=50, blank=True, null=True)
    # TODO rename collection remarks to find remarks
    collection_remarks = models.TextField("Remarks", null=True, blank=True, max_length=255)

    # Geological Context
    stratigraphic_formation = models.CharField("Formation", max_length=255, blank=True, null=True)
    stratigraphic_member = models.CharField("Member", max_length=255, blank=True, null=True)
    analytical_unit = models.CharField(max_length=255, blank=True, null=True)
    analytical_unit_2 = models.CharField(max_length=255, blank=True, null=True)
    analytical_unit_3 = models.CharField(max_length=255, blank=True, null=True)
    analytical_unit_found = models.CharField(max_length=255, blank=True, null=True)
    analytical_unit_likely = models.CharField(max_length=255, blank=True, null=True)
    analytical_unit_simplified = models.CharField(max_length=255, blank=True, null=True)
    in_situ = models.BooleanField(default=False)
    ranked = models.BooleanField(default=False)
    weathering = models.SmallIntegerField(blank=True, null=True)
    surface_modification = models.CharField(max_length=255, blank=True, null=True)
    geology_remarks = models.TextField(max_length=500, null=True, blank=True)

    # Location
    collection_code = models.CharField("Collection Code", max_length=20, blank=True, null=True)
    drainage_region = models.CharField(null=True, blank=True, max_length=255)
    georeference_remarks = models.TextField(max_length=50, null=True, blank=True)
    geom = models.PointField(srid=4326, blank=True, null=True)  # NOT NULL
    objects = models.GeoManager()

    # Media
    image = models.FileField(max_length=255, blank=True, upload_to="uploads/images/hrp", null=True)

    class Meta:
        verbose_name = "HRP Occurrence"
        verbose_name_plural = "HRP Occurrences"
        ordering = ["collection_code", "locality", "item_number", "item_part"]

    def __unicode__(self):
        nice_name = str(self.catalog_number()) + ' ' + '[' + str(self.item_scientific_name) + ' ' \
                    + str(self.item_description) + "]"
        return nice_name.replace("None", "").replace("--", "")

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


class Biology(Occurrence):
    # Biology
    sex = models.CharField(null=True, blank=True, max_length=50)
    life_stage = models.CharField(null=True, blank=True, max_length=50)
    biology_remarks = models.TextField(max_length=500, null=True, blank=True)

    # Taxon
    taxon = models.ForeignKey(Taxon,
                              default=0, on_delete=models.SET_DEFAULT,  # prevent deletion when taxa deleted
                              related_name='hrp_taxon_bio_occurrences')
    identification_qualifier = models.ForeignKey(IdentificationQualifier, null=True, blank=True,
                                                 on_delete=models.SET_NULL,
                                                 related_name='hrp_id_qualifier_bio_occurrences')
    qualifier_taxon = models.ForeignKey(Taxon, null=True, blank=True,
                                        on_delete=models.SET_NULL,
                                        related_name='hrp_qualifier_taxon_bio_occurrences')
    verbatim_taxon = models.CharField(null=True, blank=True, max_length=1024)
    verbatim_identification_qualifier = models.CharField(null=True, blank=True, max_length=255)
    taxonomy_remarks = models.TextField(max_length=500, null=True, blank=True)

    # Identification
    identified_by = models.CharField(null=True, blank=True, max_length=100)
    year_identified = models.IntegerField(null=True, blank=True)
    type_status = models.CharField(null=True, blank=True, max_length=50)

    fauna_notes = models.TextField(null=True, blank=True, max_length=64000)

    # Element
    side = models.CharField(null=True, blank=True, max_length=50, choices=HRP_SIDE_CHOICES)
    # TODO add element_choices once field is cleaned
    element = models.CharField(null=True, blank=True, max_length=50)
    # TODO add element_modifier choices once field is cleaned
    element_modifier = models.CharField(null=True, blank=True, max_length=50)
    # TODO populate portion after migrate
    element_portion = models.CharField(null=True, blank=True, max_length=50, choices=HRP_ELEMENT_PORTION_CHOICES)
    # TODO populate number choices after migrate
    element_number = models.CharField(null=True, blank=True, max_length=50, choices=HRP_ELEMENT_NUMBER_CHOICES)

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
    # TODO delete attributes, preparations and morphobank number
    attributes = models.CharField(null=True, blank=True, max_length=50)
    preparations = models.CharField(null=True, blank=True, max_length=50)
    morphobank_number = models.IntegerField(null=True, blank=True)  # empty, ok to delete

    class Meta:
        verbose_name = "HRP Biology"
        verbose_name_plural = "HRP Biology"

    def __unicode__(self):
        return str(self.taxon.__unicode__())

    @staticmethod
    def find_unmatched_values(field_name):
        """
        For every field in the data model this function compares the values in the DB against the values
        in the choice lists and reports any unmatched values, i.e. DB values not in choices lists.
        :param field_name:
        :return: returns a three-element tuple:
        1. The first element is True/False and indicates if any non-matching values were found
        2. The second element list how many unique non-matching values were found
        3. The third is a list of all the uniuqe non-matching values
        """
        bio_objs = Biology.objects.all()  # get all biology objects
        # get a list of unique values not in choice sets
        values = list(set([getattr(bio, field_name) for bio in bio_objs]))
        # get the field object based on the field_name argument
        field = Biology._meta.get_field_by_name(field_name)[0]
        # get the choices for that field, assumes field has a choice list
        choices = [i[0] for i in field.choices]
        # create a list of all unique values in the db that are not in the choice list
        result = [v for v in values if v not in choices]
        if (not result) or result == [None]:
            result_tuple = (False, None, None)
            return result_tuple
        else:
            result_tuple = (True, len(result), result)
            return result_tuple


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
