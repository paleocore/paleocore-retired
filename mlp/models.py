from django.contrib.gis.db import models
from taxonomy.models import Taxon, IdentificationQualifier
from mysite.ontologies import BASIS_OF_RECORD_VOCABULARY, ITEM_TYPE_VOCABULARY, COLLECTING_METHOD_VOCABULARY, \
    COLLECTOR_CHOICES, SIDE_VOCABULARY

import os
from django.contrib.gis.geos import Point


FIELD_SEASON_CHOICES = (('Jan 2014', 'Jan 2014'), ('Nov 2014', 'Nov 2014'), ('Nov 2015', 'Nov 2015'))


# Model for occurrence table generated by inspect.db
class Occurrence(models.Model):
    """
    Occurrence == Find, a general class for things discovered in the field.
    Find's have three subtypes: Archaeology, Biology, Geology
    Fields are grouped by comments into logical sets (i.e. ontological classes)
    """
    # Record
    # dwc:modified
    date_last_modified = models.DateTimeField('Modified', auto_now=True,
                                              help_text='The date and time this resource was last altered.')
    basis_of_record = models.CharField("Basis of Record", max_length=50, blank=True, null=False,
                                       help_text='e.g. HumanObservation or FossilSpecimen',
                                       choices=BASIS_OF_RECORD_VOCABULARY)  # NOT NULL  dwc:basisOfRecord
    problem = models.BooleanField(default=False,
                                  help_text='Is there a problem with this record that needs attention?')
    problem_comment = models.TextField(max_length=255, blank=True, null=True,
                                       help_text='Description of the problem.')
    # TODO add rich text field for remarks
    remarks = models.TextField(max_length=255, null=True, blank=True,
                               help_text='General remarks about this database record.')

    # Event
    year_collected = models.IntegerField(blank=True, null=True)
    field_season = models.CharField(max_length=50, null=True, blank=True, choices=FIELD_SEASON_CHOICES)
    # TODO add a date_recorded field and repurpose field number to its appropriate meaning

    # Find
    barcode = models.IntegerField(blank=True, null=True,
                                  help_text='For collected items only.')  # dwc:recordNumber
    field_number = models.DateTimeField(blank=False, null=False, editable=True)  # NOT NULL

    item_type = models.CharField(max_length=255, blank=True, null=False, choices=ITEM_TYPE_VOCABULARY)  # NOT NULL
    item_scientific_name = models.CharField("Sci Name", max_length=255, null=True, blank=True)
    item_description = models.CharField("Description", max_length=255, blank=True, null=True)
    # TODO rename to item_count
    # Note: individual count here <> dwc:individual count
    individual_count = models.IntegerField(blank=True, null=True, default=1)
    collector = models.CharField(max_length=50, blank=True, null=True, choices=COLLECTOR_CHOICES)
    finder = models.CharField(max_length=50, blank=True, null=True)
    collecting_method = models.CharField("Collecting Method", max_length=50,
                                         choices=COLLECTING_METHOD_VOCABULARY, null=False)  # NOT NULL
    item_number = models.IntegerField("Item #", null=True, blank=True)
    item_part = models.CharField("Item Part", max_length=10, null=True, blank=True)
    catalog_number = models.CharField("Catalog #", max_length=255, blank=True, null=True)
    related_catalog_items = models.CharField("Related Catalog Items", max_length=50, null=True, blank=True)
    disposition = models.CharField(max_length=255, blank=True, null=True)
    preparation_status = models.CharField(max_length=50, blank=True, null=True)

    # Geological Context
    stratigraphic_member = models.CharField(max_length=255, blank=True, null=True)
    analytical_unit = models.CharField("Submember", max_length=255, blank=True, null=True)
    analytical_unit_2 = models.CharField(max_length=255, blank=True, null=True)
    analytical_unit_3 = models.CharField(max_length=255, blank=True, null=True)
    in_situ = models.BooleanField(default=False)
    ranked = models.BooleanField(default=False)
    weathering = models.SmallIntegerField(blank=True, null=True)
    surface_modification = models.CharField(max_length=255, blank=True, null=True)

    stratigraphic_marker_upper = models.CharField(max_length=255, blank=True, null=True)
    distance_from_upper = models.DecimalField(max_digits=38, decimal_places=8, blank=True, null=True)
    stratigraphic_marker_lower = models.CharField(max_length=255, blank=True, null=True)
    distance_from_lower = models.DecimalField(max_digits=38, decimal_places=8, blank=True, null=True)
    stratigraphic_marker_found = models.CharField(max_length=255, blank=True, null=True)
    distance_from_found = models.DecimalField(max_digits=38, decimal_places=8, blank=True, null=True)
    stratigraphic_marker_likely = models.CharField(max_length=255, blank=True, null=True)
    distance_from_likely = models.DecimalField(max_digits=38, decimal_places=8, blank=True, null=True)

    # Location
    collection_code = models.CharField("Collection Code", max_length=20, blank=True, null=True, default='MLP')
    georeference_remarks = models.CharField(max_length=50, null=True, blank=True)
    geom = models.PointField(srid=4326, blank=True, null=True)  # NOT NULL
    objects = models.GeoManager()

    # Media
    image = models.FileField(max_length=255, blank=True, upload_to="uploads/images/mlp", null=True)

    class Meta:
        managed = True
        verbose_name = 'MLP Occurrence'
        verbose_name_plural = 'MLP Occurrences'

    def __unicode__(self):
        """
        What is the best string representation for an occurrence instance?
        All collected items have catalogue numbers, but observations do not
        This method returns the catalog number if it exists, or a string with the id value
        if there is no catalog number.
        """
        if self.catalog_number:
            return self.catalog_number
        else:
            return "item "+str(self.id)

    @staticmethod
    def method_fields_to_export():
        """
        Method to store a list of fields that should be added to data exports.
        Called by export admin actions.
        These fields are defined in methods and are not concrete fields in the DB so have to be declared.
        :return:
        """
        return ['longitude', 'latitude', 'easting', 'northing', 'photo']

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

    # TODO if point is outside utm zone raises GDAL Exception: OGR Failure.
    # Happened when I uploaded a test point in austin, can't convert those coordinates to 32637
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
    preparations = models.CharField(null=True, blank=True, max_length=50)
    morphobank_number = models.IntegerField(null=True, blank=True)

    # Taxon
    taxon = models.ForeignKey(Taxon,
                              default=0, on_delete=models.SET_DEFAULT,  # prevent deletion when taxa deleted
                              related_name='mlp_biology_occurrences')
    identification_qualifier = models.ForeignKey(IdentificationQualifier, null=True, blank=True,
                                                 on_delete=models.SET_NULL,
                                                 related_name='mlp_biology_occurrences')


    # Identification
    identified_by = models.CharField(null=True, blank=True, max_length=100, choices=COLLECTOR_CHOICES)
    date_identified = models.DateTimeField(null=True, blank=True)
    type_status = models.CharField(null=True, blank=True, max_length=50)


    infraspecific_epithet = models.CharField(null=True, blank=True, max_length=50)
    infraspecific_rank = models.CharField(null=True, blank=True, max_length=50)
    author_year_of_scientific_name = models.CharField(null=True, blank=True, max_length=50)
    nomenclatural_code = models.CharField(null=True, blank=True, max_length=50)
    fauna_notes = models.TextField(null=True, blank=True, max_length=64000)

    # Element
    side = models.CharField(null=True, blank=True, max_length=50, choices=SIDE_VOCABULARY)

    element = models.CharField(null=True, blank=True, max_length=50)
    element_modifier = models.CharField(null=True, blank=True, max_length=50)
    # TODO add element_portion
    # TODO add element_number

    tooth_upper_or_lower = models.CharField(null=True, blank=True, max_length=10)
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
    attributes = models.CharField(null=True, blank=True, max_length=50)

    class Meta:
        verbose_name = "MLP Biology"
        verbose_name_plural = "MLP Biology"

    def __unicode__(self):
        return str(self.taxon.__unicode__())
