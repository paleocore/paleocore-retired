from django.contrib.gis.db import models
from mysite import ontologies


class Occurrence(models.Model):
    global_id = models.IntegerField(blank=True, null=True)  # Global Unique Identifier
    reference = models.CharField("Reference", max_length=255, null=True, blank=True)
    #date_last_modified = models.DateTimeField("Date Last Modified", auto_now=True)
    basis_of_record = models.CharField("Basis of Record", max_length=255, blank=True, null=False,
                                       choices=ontologies.BASIS_OF_RECORD_VOCABULARY)  # NOT NULL
    item_type = models.CharField("Item Type", max_length=255, blank=True, null=True,
                                 choices=ontologies.ITEM_TYPE_VOCABULARY)
    collection_code = models.CharField("Collection Code", max_length=255, blank=True, null=True, default='MLP')
    institution_code = models.CharField("Institution Code", max_length=255, blank=True, null=True)
    item_number = models.IntegerField("Item #", null=True, blank=True)
    item_part = models.CharField("Item Part", max_length=255, null=True, blank=True)
    catalog_number = models.CharField("Catalog #", max_length=255, blank=True, null=True)
    paleo_locality = models.CharField("Paleo Locality", max_length=255, blank=True, null=True)
    paleo_locality_number = models.IntegerField("Paleo Locality Number", null=True, blank=True)
    sampling_protocol = models.CharField("Sampling Protocol", max_length=255, blank=True, null=True)
    # TODO add rich text field for remarks
    occurrence_remarks = models.TextField("Occurrence Remarks", max_length=255, null=True, blank=True)
    item_scientific_name = models.CharField("Sci Name", max_length=255, null=True, blank=True)
    item_description = models.CharField("Item Description", max_length=255, blank=True, null=True)
    continent = models.CharField("Continent", max_length=255, blank=True, null=True)
    country = models.CharField("Country", max_length=255, blank=True, null=True)
    state_province = models.CharField("State or Province", max_length=255, blank=True, null=True)
    locality = models.CharField("Locality", max_length=255, null=True, blank=True)
    verbatim_locality = models.CharField("Verbatim Locality", max_length=255, null=True, blank=True)
    location_remarks = models.CharField("Location Remarks", max_length=255, blank=True, null=True)
    verbatim_coordinates = models.CharField("Verbatim Coordinates", null=True, blank=True, max_length=255)
    verbatim_coordinate_system = models.CharField("Verbatim Coordinate System", null=True, blank=True, max_length=255)
    decimal_longitude = models.DecimalField("Longitude", max_digits=38, decimal_places=8, blank=True, null=True)
    decimal_latitude = models.DecimalField("Latitude", max_digits=38, decimal_places=8, blank=True, null=True)
    geodetic_datum = models.CharField("Geodetic Datum", null=True, blank=True, max_length=255)
    coordinate_uncertainty_in_meters = models.IntegerField("Coordinate Uncertainty", null=True, blank=True)
    georeference_remarks = models.CharField("Georeferencing Remarks", max_length=255, null=True, blank=True)
    collecting_method = models.CharField("Collecting Method", max_length=255, blank=True,
                                         choices=ontologies.COLLECTING_METHOD_VOCABULARY, null=True)
    related_catalog_items = models.CharField("Related Catalog Items", max_length=255, null=True, blank=True)
    collector = models.CharField(max_length=255, blank=True, null=True, choices=ontologies.COLLECTOR_CHOICES)
    found_by = models.CharField("Found By", max_length=255, blank=True, null=True)
    event_date = models.DateField("Date", null=True, blank=True)
    event_year = models.IntegerField("Year", blank=True, null=True)
    event_month = models.CharField("Month", max_length=255, blank=True, null=True)
    event_day = models.CharField("Day", max_length=255, blank=True, null=True)
    event_remarks = models.CharField("Event Remarks", max_length=255, blank=True, null=True)
    stratigraphic_marker_upper = models.CharField("Stratigraphic Marker Upper", max_length=255, blank=True, null=True)
    distance_from_upper = models.DecimalField("Distance From Upper", max_digits=38, decimal_places=8, blank=True,
                                              null=True)
    stratigraphic_marker_lower = models.CharField("Stratigraphic Marker Lower", max_length=255, blank=True, null=True)
    distance_from_lower = models.DecimalField("Distance From Lower", max_digits=38, decimal_places=8, blank=True, null=True)
    stratigraphic_group = models.CharField("Stratigraphic Group", max_length=255, blank=True, null=True)
    stratigraphic_formation = models.CharField("Stratigraphic Formation", max_length=255, blank=True, null=True)
    stratigraphic_member = models.CharField("Stratigraphic Member", max_length=255, blank=True, null=True)
    stratigraphic_bed = models.CharField("Stratigraphic Bed", max_length=255, blank=True, null=True)
    geochronological_age = models.IntegerField("Geochronological Age", blank=True, null=True)
    image = models.FileField(max_length=255, blank=True, upload_to="uploads/images/san_francisco", null=True)
    geom = models.GeometryField(srid=4326, blank=True, null=True)
    objects = models.GeoManager()


class PaleoSite(models.Model):
    """
    Namespaces
    dwc: Darwin Core
    dc: Dublin Core
    tdr: the Digital Archaeological Record tDAR
    """
    name = models.CharField(max_length=255, blank=False, null=False)  # REQUIRED
    setting = models.CharField(max_length=255, blank=True, null=True, choices=ontologies.SETTING_CHOICES)
    continent = models.CharField(max_length=255, blank=True, null=True, choices=ontologies.CONTINENT_CHOICES)
    country = models.CharField(max_length=255, blank=True, null=True, choices=ontologies.COUNTRY_CHOICES)  # dwc:country
    region = models.CharField(max_length=255, blank=True, null=True, choices=ontologies.REGION_CHOICES)  # dwc:locality
    research_project = models.CharField(max_length=255, blank=True, null=True)  # e.g.
    collection_code = models.CharField(null=True, blank=True, max_length=20)  # dwc:collection_code
    geological_member = models.CharField(max_length=255, blank=True, null=True)  # dwd:member
    cultural_term = models.CharField(max_length=255, blank=True, null=True)  # tdr:cultural_term, Stillbay
    technology_period = models.CharField(max_length=255, blank=True, null=True)  # e.g. MSA, ESA, UP, MP
    start_date = models.CharField(max_length=255, blank=True, null=True)  # tdr: start_date
    end_date = models.CharField(max_length=255, blank=True, null=True)  # tdr:end_date
    geological_epoch = models.CharField(max_length=255, blank=True, null=True,
                                        choices=ontologies.EPOCH_CHOICES)  # dwc:epoch
    date_description = models.CharField(max_length=255, blank=True, null=True)  # tdr:date_description, e.g. ESR, OSL
    material = geom = models.CharField(max_length=255, blank=True, null=True,
                                       choices=ontologies.MATERIAL_CHOICES)  # tdr:material_types
    references = models.TextField(null=True, blank=True, max_length=2500)  # dwc:references
    remarks = models.TextField(null=True, blank=True, max_length=2500)
    geom = models.PointField(srid=4326)
    objects = models.GeoManager()


