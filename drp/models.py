# This is an auto-generated Django model module created by ogrinspect.
from django.contrib.gis.db import models
from datetime import datetime
from taxonomy.models import Taxon, IdentificationQualifier
from mysite.ontologies import *

item_typeCHOICES = (("Artifactual", "Artifactual"), ("Faunal", "Faunal"), ("Floral", "Floral"), ("Geological", "Geological"))


class Locality(models.Model):
    paleolocality_number = models.IntegerField(null=True,blank=True)
    collection_code = models.CharField(null=True, blank=True, choices = (("DIK", "DIK"), ("ASB", "ASB")), max_length=10)
    paleo_sublocality = models.CharField(null=True, blank=True, max_length=50)
    description_1 = models.TextField(null=True, blank=True, max_length=255)
    description_2 = models.TextField(null=True, blank=True, max_length=255)
    description_3 = models.TextField(null=True, blank=True, max_length=255)
    stratigraphic_section = models.CharField(null=True, blank=True, max_length=50)
    upper_limit_in_section = models.IntegerField(null=True, blank=True)
    lower_limit_in_section = models.DecimalField(max_digits=38, decimal_places=8, null=True, blank=True)
    error_notes = models.CharField(max_length=255, null=True, blank=True)
    notes = models.CharField(max_length=254, null=True, blank=True)
    geom = models.PolygonField(srid=4326)
    objects = models.GeoManager()

    def __unicode__(self):
        return str(self.collection_code) + " " + str(self.paleolocality_number)

    class Meta:
        verbose_name = "DRP Locality"
        verbose_name_plural = "DRP Localities"
        #db_table='drp_locality'
        ordering = ("collection_code", "paleolocality_number", "paleo_sublocality")


# This is the DRP data model. It is only partly PaleoCore compliant.
class Occurrence(models.Model):
    barcode = models.IntegerField("Barcode",null=True, blank=True)
    date_last_modified = models.DateTimeField("Date Last Modified", auto_now_add=True, auto_now=True)
    #date_last_modified   = models.DateTimeField("Date Last Modified",null=True, blank=True)
    basis_of_record = models.CharField("Basis of Record", max_length=50, blank=True, null=False,
                                       choices=BASIS_OF_RECORD_VOCABULARY)  # NOT NULL
    #basis_of_record   = models.CharField("Basis of Record",null=True, blank=True,max_length=50,choices=basisCHOICES)
    item_type = models.CharField("Item Type", max_length=255, blank=True, null=False,
                                 choices=ITEM_TYPE_VOCABULARY)  # NOT NULL
    #item_type = models.CharField("Item Type",null=True, blank=True,max_length=255,choices=item_typeCHOICES)
    #institutionalcode = models.CharField("Institution",null=True, blank=True,max_length=20)
    collection_code = models.CharField("Collection Code", max_length=20, blank=True, null=True, choices=(("DIK","DIK"),("ASB","ASB")))
    #collection_code =  models.CharField("Coll Code",null=True, blank=True,max_length=20,choices=(("DIK","DIK"),("ASB","ASB")))
    item_number = models.IntegerField("Item #", max_length=50, null=True, blank=True)
    #item_number =  models.IntegerField("Item #",null=True, blank=True,max_length=50)
    item_part = models.CharField("Item Part", max_length=10, null=True, blank=True)
    #item_part = models.CharField("Item Part",null=True, blank=True,max_length=10)
    catalog_number = models.CharField("Catalog #", max_length=255, blank=True, null=True)
    #catalog_number = models.CharField("Catalog Number", null=True, blank=True,max_length=255)
    #remarks = models.TextField(max_length=255, null=True, blank=True)
    remarks = models.TextField("Remarks", null=True, blank=True,max_length=2500)
    item_scientific_name = models.CharField("Sci Name", max_length=255, null=True, blank=True)
    #item_scientific_name = models.CharField("Scientific Name",null=True, blank=True,max_length=255)
    item_description = models.CharField("Description", max_length=255, blank=True, null=True)
    #itemdescription = models.CharField("Description",null=True, blank=True,max_length=255)
    #continent = models.CharField(null=True, blank=True,max_length=50)
    #country = models.CharField(null=True, blank=True,max_length=50)
    #stateprovince = models.CharField(null=True, blank=True,max_length=50)
    georeference_remarks = models.CharField(max_length=50, null=True, blank=True)
    #georeferenceremarks = models.CharField(null=True, blank=True,max_length=50)
    #utmzone = models.IntegerField(null=True, blank=True)
    #utmeast = models.DecimalField(max_digits=38, decimal_places=8, null=True, blank=True)
    #utmnorth = models.DecimalField(max_digits=38, decimal_places=8, null=True, blank=True)
    collecting_method = models.CharField("Collecting Method", max_length=50,
                                         choices=COLLECTING_METHOD_VOCABULARY, null=False)
    #collectingmethod = models.CharField("Collection Method",null=True, blank=True,max_length=50)
    related_catalog_items = models.CharField("Related Catalog Items", max_length=50, null=True, blank=True)
    #relatedcatalogitems = models.CharField(null=True, blank=True,max_length=50)

    #earliestdatecollected = models.DateTimeField(null=True, blank=True)
    #dayofyear = models.IntegerField(null=True, blank=True)
    collector = models.CharField(max_length=50, blank=True, null=True, choices=COLLECTOR_CHOICES)
    #collector = models.CharField(null=True, blank=True,max_length=50)
    #finder = models.CharField(max_length=50, blank=True, null=True)
    finder = models.CharField(null=True, blank=True,max_length=50)
    disposition = models.CharField(max_length=255, blank=True, null=True)
    #disposition = models.CharField(null=True, blank=True,max_length=255)
    field_number = models.DateTimeField(blank=False, null=False, editable=False)  # NOT NULL
    #fieldnumber = models.DateTimeField("Field Number",null=True, blank=True)
    #monthcollected = models.CharField(null=True, blank=True,max_length=20)
    year_collected = models.IntegerField(blank=True, null=True)
    #year_collected = models.IntegerField("Year",null=True, blank=True)
    individual_count = models.IntegerField(blank=True, null=True, default=1)
    #individualcount = models.IntegerField(null=True, blank=True)
    preparation_status = models.CharField(max_length=50, blank=True, null=True)
    #preparationstatus = models.CharField(null=True, blank=True,max_length=50)
    stratigraphic_marker_upper = models.CharField(max_length=255, blank=True, null=True)
    #stratigraphic_marker_upper = models.CharField(null=True, blank=True,max_length=255,db_column="stratigraphicmarkerupper")
    distance_from_upper = models.DecimalField(max_digits=38, decimal_places=8, blank=True, null=True)
    #distancefromupper = models.DecimalField(max_digits=38, decimal_places=8, "Distance Upper",null=True, blank=True)
    stratigraphic_marker_lower = models.CharField(max_length=255, blank=True, null=True)
    #stratigraphic_marker_lower = models.CharField(null=True, blank=True,max_length=255,db_column="stratigraphicmarkerlower")
    distance_from_lower = models.DecimalField(max_digits=38, decimal_places=8, blank=True, null=True)
    #distancefromlower = models.DecimalField(max_digits=38, decimal_places=8, "Distance Lower",null=True, blank=True)
    stratigraphic_marker_found = models.CharField(max_length=255, blank=True, null=True)
    #stratigraphic_marker_found = models.CharField(null=True, blank=True,max_length=255,db_column="stratigraphicmarkerfound")
    distance_from_found = models.DecimalField(max_digits=38, decimal_places=8, blank=True, null=True)
    #distancefromfound = models.DecimalField(max_digits=38, decimal_places=8, "Distance Found",null=True, blank=True)
    stratigraphic_marker_likely = models.CharField(max_length=255, blank=True, null=True)
    #stratigraphic_marker_likely = models.CharField(null=True, blank=True,max_length=255,db_column="stratigraphicmarkerlikely")
    distance_from_likely = models.DecimalField(max_digits=38, decimal_places=8, blank=True, null=True)
    #distancefromlikely = models.DecimalField(max_digits=38, decimal_places=8, "Distance Likely",null=True, blank=True)
    stratigraphic_member = models.CharField(max_length=255, blank=True, null=True)
    #stratigraphicmember = models.CharField("Member",null=True, blank=True,max_length=255)
    analytical_unit = models.CharField(max_length=255, blank=True, null=True)
    #analyticalunit = models.CharField("Submember",null=True, blank=True,max_length=255)
    analytical_unit_2 = models.CharField(max_length=255, blank=True, null=True)
    #analyticalunit2 = models.CharField("Submember2",null=True, blank=True,max_length=255)
    analytical_unit_3 = models.CharField(max_length=255, blank=True, null=True)
    #analyticalunit3 = models.CharField("Submember3",null=True, blank=True,max_length=255)
    in_situ = models.BooleanField(default=False)
    #insitu = models.IntegerField("In Situ?",null=True,blank=True)
    ranked = models.BooleanField(default=False)
    #ranked = models.IntegerField("Ranked?",null=True,blank=True)
    image = models.FileField(max_length=255, blank=True, upload_to="uploads/images/drp", null=True)
    #imageurl = models.CharField(null=True, blank=True,max_length=255)
    #relatedinformation = models.CharField(null=True, blank=True,max_length=50)
    #localityid = models.IntegerField(null=True, blank=True)
    weathering = models.SmallIntegerField(blank=True, null=True)
    #weathering = models.IntegerField(null=True, blank=True)
    surface_modification = models.CharField(max_length=255, blank=True, null=True)
    #surfacemodification = models.CharField(null=True, blank=True,max_length=255)
    #point_x = models.DecimalField(max_digits=38, decimal_places=8, null=True, blank=True)
    #point_y = models.DecimalField(max_digits=38, decimal_places=8, null=True, blank=True)
    problem = models.BooleanField(default=False)
    #problem = models.IntegerField(null=True,blank=True,max_length=5)
    problem_comment = models.TextField(max_length=255, blank=True, null=True)
    #problemcomment = models.CharField(null=True, blank=True,max_length=255)
    #dgupdate2013 = models.IntegerField(null=True, blank=True)
    #dgupdatex = models.DecimalField(max_digits=38, decimal_places=8, null=True, blank=True)
    #dgupdatey = models.DecimalField(max_digits=38, decimal_places=8, null=True, blank=True)
    geom = models.GeometryField(srid=4326, blank=True, null=True)  # NOT NULL
    #geom = models.PointField(srid=4326)
    objects = models.GeoManager()

    #DRP Specific Fields
    paleolocality_number = models.IntegerField("Locality #",null=True, blank=True)
    paleo_sublocality = models.CharField("Sublocality",null=True, blank=True,max_length=50)
    locality_text = models.CharField(null=True, blank=True,max_length=255,db_column="locality")
    verbatim_coordinates = models.CharField(null=True, blank=True,max_length=50)
    verbatim_coordinate_system = models.CharField(null=True, blank=True,max_length=50)
    geodetic_datum = models.CharField(null=True, blank=True,max_length=20)
    collection_remarks = models.CharField("Remarks",null=True, blank=True,max_length=255)
    stratigraphic_section = models.CharField(null=True, blank=True,max_length=50)
    stratigraphic_height_in_meters = models.DecimalField(max_digits=38, decimal_places=8, null=True, blank=True)
    locality = models.ForeignKey(Locality)

    @staticmethod
    def fields_to_display():
        fields = ("id", "barcode")
        return fields

    def point_X(self):
        return self.geom.x

    def point_Y(self):
        return self.geom.y

    def __unicode__(self):
        niceName = str(self.collection_code) + "-" + str(self.paleolocality_number) + "-" + str(self.item_number) + str(self.item_part) + " [" + str(self.item_scientific_name) + " " + str(self.item_description) + "]"
        return niceName.replace("None","").replace("--","")

    def save(self, *args, **kwargs):#custom save method for occurrence
        thecatalog_number = str(self.collection_code) + "-" + str(self.paleolocality_number) + str(self.paleosublocality) + "-" + str(self.item_number) + str(self.item_part)
        self.catalog_number = thecatalog_number.replace("None","")
        self.date_last_modified = datetime.now()  # TODO change date_last_modified autonow option to accomplish this

        #call the normal drp_occurrence save method using alternate database
        super(Occurrence, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "DRP Occurrence"
        verbose_name_plural = "DRP Occurrences"
        # The DRP database is in the SDE standard in order to make it compatible with
        # ArcGIS 10.1. Django does not handle PostGIS DB schemas natively. This is a
        # work-around to point Django to the right location for the data tables.
        #db_table='drp_occurrence'
        ordering = ["collection_code", "paleolocality_number", "item_number", "item_part"]


class Image(models.Model):
    occurrence = models.ForeignKey("Occurrence", related_name='drp_occurrences')
    image = models.ImageField(upload_to="uploads/images", null=True, blank=True)
    description = models.TextField(null=True, blank=True)


class File(models.Model):
    occurrence = models.ForeignKey("Occurrence")
    file = models.FileField(upload_to="uploads/files", null=True, blank=True)
    description = models.TextField(null=True, blank=True)


class Biology(Occurrence):
    infraspecific_epithet = models.CharField(null=True, blank=True, max_length=50)
    #infraspecificepithet = models.CharField(null=True,blank=True,max_length=50)
    infraspecific_rank = models.CharField(null=True, blank=True, max_length=50)
    #infraspecificrank = models.CharField(null=True,blank=True,max_length=50)
    author_year_of_scientific_name = models.CharField(null=True, blank=True, max_length=50)
    #authoryearofscientificname = models.CharField(null=True,blank=True,max_length=50)
    nomenclatural_code = models.CharField(null=True, blank=True, max_length=50)
    #nomenclaturalcode = models.CharField(null=True,blank=True,max_length=50)
    identification_qualifier = models.CharField(null=True, blank=True, max_length=50)
    #identificationqualifier = models.CharField(null=True,blank=True,max_length=50)
    identified_by = models.CharField(null=True, blank=True, max_length=100)
    #identifiedby = models.CharField(null=True,blank=True,max_length=100)
    date_identified = models.DateTimeField(null=True, blank=True)
    #dateidentified = models.DateTimeField(null=True,blank=True)
    type_status = models.CharField(null=True, blank=True, max_length=50)
    #typestatus = models.CharField(null=True,blank=True,max_length=50)
    sex = models.CharField(null=True, blank=True, max_length=50)
    #sex = models.CharField(null=True,blank=True,max_length=50)
    life_stage = models.CharField(null=True, blank=True, max_length=50)
    #lifestage = models.CharField(null=True,blank=True,max_length=50)
    preparations = models.CharField(null=True, blank=True, max_length=50)
    #preparations = models.CharField(null=True,blank=True,max_length=50)
    morphobank_number = models.IntegerField(null=True, blank=True)
    #morphobanknum = models.IntegerField(null=True,blank=True)
    side = models.CharField(null=True, blank=True, max_length=50)
    attributes = models.CharField(null=True, blank=True, max_length=50)
    #attributes = models.CharField(null=True,blank=True,max_length=50)
    fauna_notes = models.TextField(null=True, blank=True, max_length=64000)
    #faunanotes = models.TextField(null=True,blank=True,max_length=64000)
    tooth_upper_or_lower = models.CharField(null=True, blank=True, max_length=50)
    #toothupperorlower = models.CharField(null=True,blank=True,max_length=10)
    tooth_number = models.CharField(null=True, blank=True, max_length=50)
    #toothnumber = models.CharField(null=True,blank=True,max_length=50)
    tooth_type = models.CharField(null=True, blank=True, max_length=50)
    #toothtype = models.CharField(null=True,blank=True,max_length=50)
    um_tooth_row_length_mm = models.DecimalField(max_digits=38, decimal_places=8, null=True, blank=True)
    #umtoothrowlengthmm = models.DecimalField(max_digits=38, decimal_places=8, null=True,blank=True)
    um_1_length_mm = models.DecimalField(max_digits=38, decimal_places=8, null=True, blank=True)
    #um1lengthmm = models.DecimalField(max_digits=38, decimal_places=8, null=True,blank=True)
    um_1_width_mm = models.DecimalField(max_digits=38, decimal_places=8, null=True, blank=True)
    #um1widthmm = models.DecimalField(max_digits=38, decimal_places=8, null=True,blank=True)
    um_2_length_mm = models.DecimalField(max_digits=38, decimal_places=8, null=True,blank=True)
    um_2_width_mm = models.DecimalField(max_digits=38, decimal_places=8, null=True,blank=True)
    um_3_length_mm = models.DecimalField(max_digits=38, decimal_places=8, null=True,blank=True)
    um_3_width_mm = models.DecimalField(max_digits=38, decimal_places=8, null=True,blank=True)
    lm_tooth_row_length_mm = models.DecimalField(max_digits=38, decimal_places=8, null=True, blank=True)
    lm_1_length = models.DecimalField(max_digits=38, decimal_places=8, null=True, blank=True)
    lm_1_width = models.DecimalField(max_digits=38, decimal_places=8, null=True, blank=True)
    lm_2_length = models.DecimalField(max_digits=38, decimal_places=8, null=True, blank=True)
    lm_2_width = models.DecimalField(max_digits=38, decimal_places=8, null=True, blank=True)
    lm_3_length = models.DecimalField(max_digits=38, decimal_places=8, null=True, blank=True)
    lm_3_width = models.DecimalField(max_digits=38, decimal_places=8, null=True, blank=True)
    element = models.CharField(null=True, blank=True, max_length=50)
    element_modifier = models.CharField(null=True, blank=True, max_length=50)
    # TODO convert this field to boolean
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
    taxon = models.ForeignKey(Taxon, related_name='drp_biology_occurrences')
    identification_qualifier = models.ForeignKey(IdentificationQualifier, related_name='drp_biology_occurrences')

    class Meta:
        verbose_name = "DRP Biology"
        verbose_name_plural = "DRP Biology"
        #db_table='drp_biology'

    def __unicode__(self):
        return str(self.taxon.__unicode__())


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
        verbose_name = "DRP Hydrology"
        verbose_name_plural = "DRP Hydrology"
        #db_table = 'drp_hydrology'