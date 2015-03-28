# This is an auto-generated Django model module created by ogrinspect.
from django.contrib.gis.db import models
from datetime import datetime
from taxonomy.models import Taxon, IdentificationQualifier

basisCHOICES = (("FossilSpecimen", "Fossil"), ("HumanObservation", "Observation"))
itemtypeCHOICES = (("Artifactual", "Artifactual"), ("Faunal", "Faunal"), ("Floral", "Floral"), ("Geological", "Geological"))


class Locality(models.Model):
    paleolocalitynumber = models.IntegerField(null=True,blank=True)
    collectioncode = models.CharField(null=True, blank=True, choices = (("DIK", "DIK"), ("ASB", "ASB")), max_length=10)
    paleosublocality = models.CharField(null=True, blank=True, max_length=50)
    description1 = models.TextField(null=True, blank=True, max_length=255)
    description2 = models.TextField(null=True, blank=True, max_length=255)
    description3 = models.TextField(null=True, blank=True, max_length=255)
    stratsection = models.CharField(null=True, blank=True, max_length=50)
    upperlimitinsection = models.IntegerField(null=True, blank=True)
    lowerlimitinsection = models.FloatField(null=True, blank=True)
    errornotes = models.CharField(max_length=255, null=True, blank=True)
    notes = models.CharField(max_length=254, null=True, blank=True)
    geom = models.PolygonField(srid=32637)
    objects = models.GeoManager()

    def __unicode__(self):
        return str(self.collectioncode) + " " + str(self.paleolocalitynumber)

    class Meta:
        verbose_name = "DRP Locality"
        verbose_name_plural = "DRP Localities"
        #db_table='drp_locality'
        ordering = ("collectioncode", "paleolocalitynumber", "paleosublocality")


# This is the DRP data model. It is only partly PaleoCore compliant.
class Occurrence(models.Model):
    #id = models.AutoField("id",primary_key=True,db_column="id",null=False,blank=True)
    barcode = models.IntegerField("Barcode",null=True, blank=True)
    datelastmodified = models.DateTimeField("Date Last Modified",null=True, blank=True)
    basisofrecord = models.CharField("Basis of Record",null=True, blank=True,max_length=50,choices=basisCHOICES)
    itemtype = models.CharField("Item Type",null=True, blank=True,max_length=255,choices=itemtypeCHOICES)
    institutionalcode = models.CharField("Institution",null=True, blank=True,max_length=20)
    collectioncode = models.CharField("Coll Code",null=True, blank=True,max_length=20,choices=(("DIK","DIK"),("ASB","ASB")))
    paleolocalitynumber = models.IntegerField("Locality #",null=True, blank=True)
    paleosublocality = models.CharField("Sublocality",null=True, blank=True,max_length=50)
    itemnumber = models.IntegerField("Item #",null=True, blank=True,max_length=50)
    itempart = models.CharField("Item Part",null=True, blank=True,max_length=10)
    catalognumber = models.CharField("Catalog Number", null=True, blank=True,max_length=255)
    remarks = models.TextField("Remarks",null=True, blank=True,max_length=2500)
    itemscientificname = models.CharField("Scientific Name",null=True, blank=True,max_length=255)
    itemdescription = models.CharField("Description",null=True, blank=True,max_length=255)
    continent = models.CharField(null=True, blank=True,max_length=50)
    country = models.CharField(null=True, blank=True,max_length=50)
    stateprovince = models.CharField(null=True, blank=True,max_length=50)
    locality_text = models.CharField(null=True, blank=True,max_length=255,db_column="locality")
    verbatimcoordinates = models.CharField(null=True, blank=True,max_length=50)
    verbatimcoordinatesystem = models.CharField(null=True, blank=True,max_length=50)
    georeferenceremarks = models.CharField(null=True, blank=True,max_length=50)
    utmzone = models.IntegerField(null=True, blank=True)
    utmeast = models.FloatField(null=True, blank=True)
    utmnorth = models.FloatField(null=True, blank=True)
    geodeticdatum = models.CharField(null=True, blank=True,max_length=20)
    collectingmethod = models.CharField("Collection Method",null=True, blank=True,max_length=50)
    relatedcatalogitems = models.CharField(null=True, blank=True,max_length=50)
    earliestdatecollected = models.DateTimeField(null=True, blank=True)
    dayofyear = models.IntegerField(null=True, blank=True)
    collector = models.CharField(null=True, blank=True,max_length=50)
    finder = models.CharField(null=True, blank=True,max_length=50)
    disposition = models.CharField(null=True, blank=True,max_length=255)
    collectionremarks = models.CharField("Remarks",null=True, blank=True,max_length=255)
    fieldnumber = models.DateTimeField("Field Number",null=True, blank=True)
    monthcollected = models.CharField(null=True, blank=True,max_length=20)
    yearcollected = models.IntegerField("Year",null=True, blank=True)
    individualcount = models.IntegerField(null=True, blank=True)
    preparationstatus = models.CharField(null=True, blank=True,max_length=50)
    strat_upper = models.CharField(null=True, blank=True,max_length=255,db_column="stratigraphicmarkerupper")
    distancefromupper = models.FloatField("Distance Upper",null=True, blank=True)
    strat_lower = models.CharField(null=True, blank=True,max_length=255,db_column="stratigraphicmarkerlower")
    distancefromlower = models.FloatField("Distance Lower",null=True, blank=True)
    strat_found = models.CharField(null=True, blank=True,max_length=255,db_column="stratigraphicmarkerfound")
    distancefromfound = models.FloatField("Distance Found",null=True, blank=True)
    strat_likely = models.CharField(null=True, blank=True,max_length=255,db_column="stratigraphicmarkerlikely")
    distancefromlikely = models.FloatField("Distance Likely",null=True, blank=True)
    stratigraphicmember = models.CharField("Member",null=True, blank=True,max_length=255)
    analyticalunit = models.CharField("Submember",null=True, blank=True,max_length=255)
    analyticalunit2 = models.CharField("Submember2",null=True, blank=True,max_length=255)
    analyticalunit3 = models.CharField("Submember3",null=True, blank=True,max_length=255)
    insitu = models.IntegerField("In Situ?",null=True,blank=True)
    ranked = models.IntegerField("Ranked?",null=True,blank=True)
    imageurl = models.CharField(null=True, blank=True,max_length=255)
    relatedinformation = models.CharField(null=True, blank=True,max_length=50)
    #localityid = models.IntegerField(null=True, blank=True)
    stratigraphicsection = models.CharField(null=True, blank=True,max_length=50)
    stratigraphicheightinmeters = models.FloatField(null=True, blank=True)
    weathering = models.IntegerField(null=True, blank=True)
    surfacemodification = models.CharField(null=True, blank=True,max_length=255)
    #point_x = models.FloatField(null=True, blank=True)
    #point_y = models.FloatField(null=True, blank=True)
    problem = models.IntegerField(null=True,blank=True,max_length=5)
    problemcomment = models.CharField(null=True, blank=True,max_length=255)
    dgupdate2013 = models.IntegerField(null=True, blank=True)
    dgupdatex = models.FloatField(null=True, blank=True)
    dgupdatey = models.FloatField(null=True, blank=True)
    geom = models.PointField(srid=32637, db_column="shape")
    objects = models.GeoManager()
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
        niceName = str(self.collectioncode) + "-" + str(self.paleolocalitynumber) + "-" + str(self.itemnumber) + str(self.itempart) + " [" + str(self.itemscientificname) + " " + str(self.itemdescription) + "]"
        return niceName.replace("None","").replace("--","")

    def save(self, *args, **kwargs):#custom save method for occurrence
        theCatalogNumber = str(self.collectioncode) + "-" + str(self.paleolocalitynumber) + str(self.paleosublocality) + "-" + str(self.itemnumber) + str(self.itempart)
        self.catalognumber = theCatalogNumber.replace("None","")
        self.datelastmodified = datetime.now()  # TODO change datelastmodified autonow option to accomplish this

        #call the normal drp_occurrence save method using alternate database
        super(Occurrence, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "DRP Occurrence"
        verbose_name_plural = "DRP Occurrences"
        # The DRP database is in the SDE standard in order to make it compatible with
        # ArcGIS 10.1. Django does not handle PostGIS DB schemas natively. This is a
        # work-around to point Django to the right location for the data tables.
        #db_table='drp_occurrence'
        ordering = ["collectioncode", "paleolocalitynumber", "itemnumber", "itempart"]


class Image(models.Model):
    occurrence = models.ForeignKey("Occurrence")
    image = models.ImageField(upload_to="uploads/images", null=True, blank=True)
    description = models.TextField(null=True, blank=True)


class File(models.Model):
    occurrence = models.ForeignKey("Occurrence")
    file = models.FileField(upload_to="uploads/files", null=True, blank=True)
    description = models.TextField(null=True, blank=True)


class Biology(Occurrence):
    infraspecificepithet = models.CharField(null=True,blank=True,max_length=50)
    infraspecificrank = models.CharField(null=True,blank=True,max_length=50)
    authoryearofscientificname = models.CharField(null=True,blank=True,max_length=50)
    nomenclaturalcode = models.CharField(null=True,blank=True,max_length=50)
    identificationqualifier = models.CharField(null=True,blank=True,max_length=50)
    identifiedby = models.CharField(null=True,blank=True,max_length=100)
    dateidentified = models.DateTimeField(null=True,blank=True)
    typestatus = models.CharField(null=True,blank=True,max_length=50)
    sex = models.CharField(null=True,blank=True,max_length=50)
    lifestage = models.CharField(null=True,blank=True,max_length=50)
    preparations = models.CharField(null=True,blank=True,max_length=50)
    morphobanknum = models.IntegerField(null=True,blank=True)
    side = models.CharField(null=True,blank=True,max_length=50)
    attributes = models.CharField(null=True,blank=True,max_length=50)
    faunanotes = models.TextField(null=True,blank=True,max_length=64000)
    toothupperorlower = models.CharField(null=True,blank=True,max_length=50)
    toothnumber = models.CharField(null=True,blank=True,max_length=50)
    toothtype = models.CharField(null=True,blank=True,max_length=50)
    umtoothrowlengthmm = models.FloatField(null=True,blank=True)
    um1lengthmm = models.FloatField(null=True,blank=True)
    um1widthmm = models.FloatField(null=True,blank=True)
    um2lengthmm = models.FloatField(null=True,blank=True)
    um2widthmm = models.FloatField(null=True,blank=True)
    um3lengthmm = models.FloatField(null=True,blank=True)
    um3widthmm = models.FloatField(null=True,blank=True)
    lmtoothrowlengthmm = models.FloatField(null=True,blank=True)
    lm1length = models.FloatField(null=True,blank=True)
    lm1width = models.FloatField(null=True,blank=True)
    lm2length = models.FloatField(null=True,blank=True)
    lm2width = models.FloatField(null=True,blank=True)
    lm3length = models.FloatField(null=True,blank=True)
    lm3width = models.FloatField(null=True,blank=True)
    element = models.CharField(null=True,blank=True,max_length=50)
    elementmodifier = models.CharField(null=True,blank=True,max_length=50)
    # TODO convert this field to boolean
    uli1 = models.IntegerField(null=True, blank=True)
    uli2 = models.IntegerField(null=True, blank=True)
    uli3 = models.IntegerField(null=True, blank=True)
    uli4 = models.IntegerField(null=True, blank=True)
    uli5 = models.IntegerField(null=True, blank=True)
    uri1 = models.IntegerField(null=True, blank=True)
    uri2 = models.IntegerField(null=True, blank=True)
    uri3 = models.IntegerField(null=True, blank=True)
    uri4 = models.IntegerField(null=True, blank=True)
    uri5 = models.IntegerField(null=True, blank=True)
    ulc = models.IntegerField(null=True, blank=True)
    urc = models.IntegerField(null=True, blank=True)
    ulp1 = models.IntegerField(null=True, blank=True)
    ulp2 = models.IntegerField(null=True, blank=True)
    ulp3 = models.IntegerField(null=True, blank=True)
    ulp4 = models.IntegerField(null=True, blank=True)
    urp1 = models.IntegerField(null=True, blank=True)
    urp2 = models.IntegerField(null=True, blank=True)
    urp3 = models.IntegerField(null=True, blank=True)
    urp4 = models.IntegerField(null=True, blank=True)
    ulm1 = models.IntegerField(null=True, blank=True)
    ulm2 = models.IntegerField(null=True, blank=True)
    ulm3 = models.IntegerField(null=True, blank=True)
    urm1 = models.IntegerField(null=True, blank=True)
    urm2 = models.IntegerField(null=True, blank=True)
    urm3 = models.IntegerField(null=True, blank=True)
    lli1 = models.IntegerField(null=True, blank=True)
    lli2 = models.IntegerField(null=True, blank=True)
    lli3 = models.IntegerField(null=True, blank=True)
    lli4 = models.IntegerField(null=True, blank=True)
    lli5 = models.IntegerField(null=True, blank=True)
    lri1 = models.IntegerField(null=True, blank=True)
    lri2 = models.IntegerField(null=True, blank=True)
    lri3 = models.IntegerField(null=True, blank=True)
    lri4 = models.IntegerField(null=True, blank=True)
    lri5 = models.IntegerField(null=True, blank=True)
    llc = models.IntegerField(null=True, blank=True)
    lrc = models.IntegerField(null=True, blank=True)
    llp1 = models.IntegerField(null=True, blank=True)
    llp2 = models.IntegerField(null=True, blank=True)
    llp3 = models.IntegerField(null=True, blank=True)
    llp4 = models.IntegerField(null=True, blank=True)
    lrp1 = models.IntegerField(null=True, blank=True)
    lrp2 = models.IntegerField(null=True, blank=True)
    lrp3 = models.IntegerField(null=True, blank=True)
    lrp4 = models.IntegerField(null=True, blank=True)
    llm1 = models.IntegerField(null=True, blank=True)
    llm2 = models.IntegerField(null=True, blank=True)
    llm3 = models.IntegerField(null=True, blank=True)
    lrm1 = models.IntegerField(null=True, blank=True)
    lrm2 = models.IntegerField(null=True, blank=True)
    lrm3 = models.IntegerField(null=True, blank=True)
    taxon = models.ForeignKey(Taxon, related_name='drp_biology_occurrences')
    identification_qualifier = models.ForeignKey(IdentificationQualifier, related_name='drp_biology_occurrences')

    class Meta:
        verbose_name = "DRP Biology"
        verbose_name_plural = "DRP Biology"
        #db_table='drp_biology'

    def __unicode__(self):
        return str(self.taxon.__unicode__())


class Hydrology(models.Model):
    length = models.FloatField(null=True, blank=True)
    name = models.CharField(null=True, blank=True, max_length=50)
    size = models.IntegerField(null=True, blank=True)
    mapsheet = models.CharField(null=True, blank=True, max_length=50)
    geom = models.LineStringField(srid=32637)
    objects = models.GeoManager()

    def __unicode__(self):
        return str(self.name)

    class Meta:
        verbose_name = "DRP Hydrology"
        verbose_name_plural = "DRP Hydrology"
        #db_table = 'drp_hydrology'