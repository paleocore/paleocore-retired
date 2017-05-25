from django.contrib.gis.db import models
from mysite.ontologies import BASIS_OF_RECORD_VOCABULARY, ITEM_TYPE_VOCABULARY, COLLECTING_METHOD_VOCABULARY, \
    COLLECTOR_CHOICES, SIDE_VOCABULARY
from taxonomy.models import Taxon, IdentificationQualifier
from uuid import uuid4
import os
import utm


# Model for occurrence table generated by inspect.db
class Occurrence(models.Model):
    #id = models.IntegerField(primary_key=True)  # NOT NULL
    barcode = models.IntegerField(blank=True, null=True)
    date_last_modified = models.DateTimeField("Date Last Modified", auto_now=True)
    basis_of_record = models.CharField("Basis of Record", max_length=50, blank=True, null=False,
                                       choices=BASIS_OF_RECORD_VOCABULARY)  # NOT NULL
    item_type = models.CharField("Item Type", max_length=255, blank=True, null=False,
                                 choices=ITEM_TYPE_VOCABULARY)  # NOT NULL
    collection_code = models.CharField("Collection Code", max_length=20, blank=True, null=True, default='SF')
    # Note we're not using localities!
    item_number = models.IntegerField("Item #", null=True, blank=True)
    item_part = models.CharField("Item Part", max_length=10, null=True, blank=True)
    catalog_number = models.CharField("Catalog #", max_length=255, blank=True, null=True)
    # TODO add rich text field for remarks
    remarks = models.TextField(max_length=255, null=True, blank=True)
    item_scientific_name = models.CharField("Sci Name", max_length=255, null=True, blank=True)
    item_description = models.CharField("Item Description", max_length=255, blank=True, null=True)
    georeference_remarks = models.CharField(max_length=50, null=True, blank=True)
    collecting_method = models.CharField("Collecting Method", max_length=50, blank=True,
                                         choices=COLLECTING_METHOD_VOCABULARY, null=False)  # NOT NULL
    related_catalog_items = models.CharField("Related Catalog Items", max_length=50, null=True, blank=True)
    collector = models.CharField(max_length=50, blank=True, null=True, choices=COLLECTOR_CHOICES)
    finder = models.CharField(max_length=50, blank=True, null=True)
    disposition = models.CharField(max_length=255, blank=True, null=True)
    field_number = models.DateTimeField(blank=False, null=False, editable=True)  # NOT NULL
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
    stratigraphic_member = models.CharField(max_length=255, blank=True, null=True)
    analytical_unit = models.CharField(max_length=255, blank=True, null=True)
    analyticalunit2 = models.CharField(max_length=255, blank=True, null=True)
    analyticalunit3 = models.CharField(max_length=255, blank=True, null=True)
    in_situ = models.BooleanField(default=False)
    ranked = models.BooleanField(default=False)
    image = models.FileField(max_length=255, blank=True, upload_to="uploads/images/san_francisco", null=True)
    weathering = models.SmallIntegerField(blank=True, null=True)
    surface_modification = models.CharField(max_length=255, blank=True, null=True)
    #TODO Change presentation to show only 2 decimal places
    #point_x = models.DecimalField(max_digits=38, decimal_places=8, blank=True, null=True)  # now taken from geom
    #point_y = models.DecimalField(max_digits=38, decimal_places=8, blank=True, null=True)  # now taken from geom
    problem = models.BooleanField(default=False)
    problem_comment = models.TextField(max_length=255, blank=True, null=True)
    geom = models.PointField(srid=4326, blank=True, null=True)  # NOT NULL
    objects = models.GeoManager()

    class Meta:
        managed = True
        #db_table = 'san_francisco_occurrence'
        verbose_name = 'San Francisco Occurrence'
        verbose_name_plural = 'San Francisco Occurrences'

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

    def point_x(self):
        try:
            return self.geom.x
        except:
            return None

    def point_y(self):
        try:
            return self.geom.y
        except:
            return None

    def easting(self):
        try:
            return utm.from_latlon(self.geom.y, self.geom.x)[0]
        except:
            return 0

    def northing(self):
        try:
            return utm.from_latlon(self.geom.y, self.geom.x)[1]
        except:
            return 0

    def photo(self):
        try:
            return '<a href="%s"><img src="%s" style="width:600px" /></a>' \
                   % (os.path.join(self.image.url), os.path.join(self.image.url))
        except:
            return None
    photo.short_description = 'Photo'
    photo.allow_tags = True
    photo.mark_safe = True

    def thumbnail(self):
        try:
            return '<a href="%s"><img src="%s" style="width:100px" /></a>' \
                   % (os.path.join(self.image.url), os.path.join(self.image.url))
        except:
            return None
    thumbnail.short_description = 'Thumb'
    thumbnail.allow_tags = True
    thumbnail.mark_safe = True

    @staticmethod
    def fields_to_display():
        fields = ("id", "barcode")
        return fields


class Biology(Occurrence):
    #occurrence = models.OneToOneField("san_francisco_occurrence")
    #kingdom = models.CharField(null=True, blank=True, max_length=50)
    #phylum = models.CharField(null=True, blank=True, max_length=50)
    #tax_class = models.CharField("Class",null=True, blank=True, max_length=50,db_column="class")
    #tax_order = models.CharField("Order",null=True, blank=True, max_length=50,db_column="order_")
    #family = models.CharField(null=True, blank=True, max_length=50)
    #subfamily = models.CharField(null=True, blank=True, max_length=50)
    #tribe = models.CharField(null=True, blank=True, max_length=50)
    #genus = models.CharField(null=True, blank=True, max_length=50)
    #specificepithet = models.CharField("Species Name",null=True, blank=True, max_length=50)
    infraspecificepithet = models.CharField(null=True, blank=True, max_length=50)
    infraspecificrank = models.CharField(null=True, blank=True, max_length=50)
    authoryearofscientificname = models.CharField(null=True, blank=True, max_length=50)
    nomenclaturalcode = models.CharField(null=True, blank=True, max_length=50)
    identificationqualifier = models.CharField(null=True, blank=True, max_length=50)
    identifiedby = models.CharField(null=True, blank=True, max_length=100)
    dateidentified = models.DateTimeField(null=True, blank=True)
    typestatus = models.CharField(null=True, blank=True, max_length=50)
    sex = models.CharField(null=True, blank=True, max_length=50)
    lifestage = models.CharField(null=True, blank=True, max_length=50)
    preparations = models.CharField(null=True, blank=True, max_length=50)
    morphobanknum = models.IntegerField(null=True, blank=True)
    side = models.CharField(null=True, blank=True, max_length=50, choices=SIDE_VOCABULARY)
    attributes = models.CharField(null=True, blank=True, max_length=50)
    faunanotes = models.TextField(null=True, blank=True, max_length=64000)
    toothupperorlower = models.CharField(null=True, blank=True, max_length=50)
    toothnumber = models.CharField(null=True, blank=True, max_length=50)
    toothtype = models.CharField(null=True, blank=True, max_length=50)
    umtoothrowlengthmm = models.FloatField(null=True, blank=True)
    um1lengthmm = models.FloatField(null=True, blank=True)
    um1widthmm = models.FloatField(null=True, blank=True)
    um2lengthmm = models.FloatField(null=True, blank=True)
    um2widthmm = models.FloatField(null=True, blank=True)
    um3lengthmm = models.FloatField(null=True, blank=True)
    um3widthmm = models.FloatField(null=True, blank=True)
    lmtoothrowlengthmm = models.FloatField(null=True, blank=True)
    lm1length = models.FloatField(null=True, blank=True)
    lm1width = models.FloatField(null=True, blank=True)
    lm2length = models.FloatField(null=True, blank=True)
    lm2width = models.FloatField(null=True, blank=True)
    lm3length = models.FloatField(null=True, blank=True)
    lm3width = models.FloatField(null=True, blank=True)
    element = models.CharField(null=True, blank=True, max_length=50)
    elementmodifier = models.CharField(null=True, blank=True, max_length=50)
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
    taxon = models.ForeignKey(Taxon,
                              default=0, on_delete=models.SET_DEFAULT,  # prevent deletion when taxa deleted
                              related_name='san_francisco_biology_occurrences')
    identification_qualifier = models.ForeignKey(IdentificationQualifier, related_name='san_francisco_biology_occurrences')

    # def lowest_level_identification(self):
    #     if self.taxon.rank.name == "Genus":
    #         return str(self.genus) + " " + str(self.specificepithet).replace("None", "")
    #     elif self.tribe:
    #         return str(self.tribe).replace("None", "")
    #     elif self.subfamily:
    #         return str(self.subfamily).replace("None", "")
    #     elif self.family:
    #         return str(self.family).replace("None", "")
    #     elif self.tax_order:
    #         return str(self.tax_order).replace("None", "")
    #     else:
    #         return str(self.tax_class).replace("None", "")

    class Meta:
        verbose_name = "San Francisco Biology"
        verbose_name_plural = "San Francisco Biology"
        #db_table='san_francisco_biology'

    def __unicode__(self):
        return str(self.taxon.__unicode__())