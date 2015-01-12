from django.contrib.gis.db import models
from mysite.ontologies import BASIS_OF_RECORD_VOCABULARY, ITEM_TYPE_VOCABULARY, COLLECTING_METHOD_VOCABULARY, \
    COLLECTOR_CHOICES, SIDE_VOCABULARY
from drp.models import drp_taxonomy
import utm


class Occurrence(models.Model):
    specimen_number = models.AutoField(primary_key=True)  # NOT NULL
    cm_specimen_number = models.IntegerField(null=True, blank=True)  # CM SPec #
    locality = models.ForeignKey("Locality", to_field="locality_number")
    date_collected = models.DateField(blank=True, null=True, editable=True)
    time_collected = models.CharField(null=True, blank=True, max_length=50)
    date_last_modified = models.DateTimeField("Date Last Modified", auto_now_add=True, auto_now=True)
    basis_of_record = models.CharField("Basis of Record", max_length=50, blank=True, null=False,
                                       choices=BASIS_OF_RECORD_VOCABULARY)  # NOT NULL
    item_type = models.CharField("Item Type", max_length=255, blank=True, null=True,
                                 choices=ITEM_TYPE_VOCABULARY)
    collecting_method = models.CharField("Collecting Method", max_length=50, blank=True,
                                         choices=COLLECTING_METHOD_VOCABULARY, null=True)
    related_catalog_items = models.CharField("Related Catalog Items", max_length=50, null=True, blank=True)
    item_scientific_name = models.CharField("Scientific Name", null=True, blank=True, max_length=255)  # Taxon
    item_description = models.CharField(null=True, blank=True, max_length=255)
    image = models.FileField(max_length=255, blank=True, upload_to="uploads/images/gdb", null=True)

    # Disposition fields
    loan_date = models.DateField(null=True, blank=True)
    loan_recipient = models.CharField(null=True, blank=True, max_length=255)
    on_loan = models.BooleanField(default=False)  # Loan Status

    # Geospatial
    geom = models.GeometryField(srid=4326, blank=True, null=True)

    def __unicode__(self):
        return str(self.specimen_number)

    class Meta:
        verbose_name = "GDB Occurrence"


class Biology(Occurrence):
    # Taxonomy fields
    kingdom = models.CharField(null=True, blank=True, max_length=50)
    phylum = models.CharField(null=True, blank=True, max_length=50)
    tax_class = models.CharField("Class", null=True, blank=True, max_length=50)  # Class
    tax_order = models.CharField("Order", null=True, blank=True, max_length=50)  # Order
    family = models.CharField(null=True, blank=True, max_length=50)
    subfamily = models.CharField(null=True, blank=True, max_length=50)
    tribe = models.CharField(null=True, blank=True, max_length=50)
    genus = models.CharField(null=True, blank=True, max_length=50)
    specific_epithet = models.CharField("Species Name", null=True, blank=True, max_length=50)  # Species
    infraspecific_epithet = models.CharField(null=True, blank=True, max_length=50)
    infraspecific_rank = models.CharField(null=True, blank=True, max_length=50)
    # Identification fields
    author_year_of_scientific_name = models.CharField(null=True, blank=True, max_length=50)
    nomenclatural_code = models.CharField(null=True, blank=True, max_length=50)
    identification_qualifier = models.CharField(null=True, blank=True, max_length=50)
    identified_by = models.CharField(null=True, blank=True, max_length=100)
    date_identified = models.DateTimeField(null=True, blank=True)
    type_status = models.CharField(null=True, blank=True, max_length=50)
    # Description fields
    sex = models.CharField(null=True, blank=True, max_length=50)
    life_stage = models.CharField(null=True, blank=True, max_length=50)
    preparations = models.CharField(null=True, blank=True, max_length=50)
    morphobank_num = models.IntegerField(null=True, blank=True)
    element = models.CharField(null=True, blank=True, max_length=50)
    side = models.CharField(null=True, blank=True, max_length=50)
    attributes = models.CharField(null=True, blank=True, max_length=50)
    notes = models.TextField(null=True, blank=True, max_length=64000)
    lower_tooth = models.CharField(null=True, blank=True, max_length=50)
    upper_tooth = models.CharField(null=True, blank=True, max_length=50)
    jaw = models.CharField(null=True, blank=True, max_length=50)
    mandible = models.CharField(null=True, blank=True, max_length=50)
    maxilla = models.CharField(null=True, blank=True, max_length=50)
    teeth = models.CharField(null=True, blank=True, max_length=50)
    cranial = models.CharField(null=True, blank=True, max_length=50)
    miscellaneous = models.CharField(null=True, blank=True, max_length=50)
    vertebral = models.CharField(null=True, blank=True, max_length=50)
    forelimb = models.CharField(null=True, blank=True, max_length=50)
    hindlimb = models.CharField(null=True, blank=True, max_length=50)
    NALMA = models.CharField(null=True, blank=True, max_length=50)
    sub_age = models.CharField(null=True, blank=True, max_length=50)  # Subage

    class Meta:
        verbose_name = "GDB Biology"
        verbose_name_plural = "GDB Biology Items"



class Locality(models.Model):
    locality_number = models.AutoField(primary_key=True)  # NOT NULL
    locality_field_number = models.CharField(null=True, blank=True, max_length=50)
    name = models.CharField(null=True, blank=True, max_length=50)  # Locality Name
    date_discovered = models.DateField(null=True, blank=True)
    formation = models.CharField(null=True, blank=True, max_length=50)  # Formation
    member = models.CharField(null=True, blank=True, max_length=50)
    NALMA = models.CharField(null=True, blank=True, max_length=50)
    survey = models.CharField(null=True, blank=True, max_length=50)
    quad_sheet = models.CharField(null=True, blank=True, max_length=50)
    verbatim_latitude = models.CharField(null=True, blank=True, max_length=50)  # Latitude
    verbatim_longitude = models.CharField(null=True, blank=True, max_length=50)  # Longitude
    verbatim_utm = models.CharField(null=True, blank=True, max_length=50)  # UTM
    verbatim_gps_coordinates = models.CharField(null=True, blank=True, max_length=50)  # GPS
    verbatim_elevation = models.IntegerField(null=True, blank=True)  # Elevation
    gps_date = models.DateField(null=True, blank=True, editable=True)
    resource_area = models.CharField(null=True, blank=True, max_length=50)
    notes = models.TextField(null=True, blank=True)
    cm_locality_number = models.IntegerField(null=True, blank=True)  # CM Loc #
    region = models.CharField(null=True, blank=True, max_length=50)
    blm_district = models.CharField(null=True, blank=True, max_length=50)
    county = models.CharField(null=True, blank=True, max_length=50)
    image = models.FileField(max_length=255, blank=True, upload_to="uploads/images/gdb", null=True)
    geom = models.GeometryField(srid=4326, blank=True, null=True)
    date_last_modified = models.DateTimeField("Date Last Modified", auto_now_add=True, auto_now=True)

    def __unicode__(self):
        """
        This method returns the locality number and name if both exist, or a string with
        just the locality number if there is no name.
        """
        if self.name:
            return str(self.locality_number)+"-"+self.name
        else:
            return str(self.locality_number)

    def update_geom_from_verbatim(self):
        if self.verbatim_latitude is not None:
            lat_dms = self.verbatim_latitude
            lon_dms = self.verbatim_longitude
            lat_string = lat_dms.split()
            lon_string = lon_dms.split()
            if len(lat_string) == 4 and len(lon_string) == 4:
                lat_dd = (float(lat_string[2])/60+float(lat_string[1]))/60+float(lat_string[0])
                if lat_string[3]=="S":
                    lat_dd *= -1  # southern latitudes should be negative
                lon_dd = (float(lon_string[2])/60+float(lon_string[1]))/60+float(lon_string[0])
                if lon_string[3]=="W":
                    lon_dd *= -1
            return "POINT ("+str(lon_dd)+" "+str(lat_dd)+")"

    def point_x(self):
        try:
            return self.geom.coords[1]
        except:
            return 0

    def point_y(self):
        try:
            return self.geom.coords[0]
        except:
            return 0

    def easting(self):
        try:
            utmPoint = utm.from_latlon(self.geom.coords[1], self.geom.coords[0])
            return utmPoint[0]
        except:
            return 0

    def northing(self):
        try:
            utmPoint = utm.from_latlon(self.geom.coords[1], self.geom.coords[0])
            return utmPoint[1]
        except:
            return 0


    class Meta:
        verbose_name_plural = "GDB Localities"






