from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.conf import settings
from django.views import generic
import os
from models import *
from standard.models import Term
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import permission_required
from fiber.views import FiberPageMixin
import shapefile
from mlp.forms import UploadForm, UploadKMLForm
from fastkml import kml
from lxml import etree
import django.contrib.gis
import datetime
from django.contrib.gis.gdal import DataSource
from django.contrib.gis.geos import GEOSGeometry
import utm


class UploadKMLView(FiberPageMixin, generic.FormView):
    template_name = 'mlp/upload_kml.html'
    form_class = UploadKMLForm
    context_object_name = 'upload'
    success_url = '/mlp/confirmation/'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        KML_file = self.request.FILES['kmlfileUpload']
        KML_file_name = self.request.FILES['kmlfileUpload'].name
        kml_file_on_disk = default_storage.save(KML_file_name, ContentFile(KML_file.read()))
        KML_file_path = os.path.join(settings.MEDIA_ROOT)

        k = kml.KML()
        kmlf = open(KML_file_path + "/" + KML_file_name, 'r')
        kmldoc = kmlf.read()  # read() loads entire file as one string
        kmlf.close()
        k.from_string(kmldoc)
        features = k._features

        f2 = list(features[0].features())
        firstFeature = f2[1]
        occurrences = f2[1:]

        for firstFeature in occurrences:

            firstFeatureName = firstFeature.name
            firstFeatureDescription = firstFeature.description
            table = etree.fromstring(firstFeatureDescription)
            attributes = table.xpath("//text()")
            # TODO test attributes is even length
            attributes_dict = dict(zip(attributes[0::2], attributes[1::2]))

            mlp_occ = Occurrence()

            ###################
            # REQUIRED FIELDS #
            ###################
            # TODO validate no duplicate barcodes
            mlp_occ.barcode = attributes_dict.get("Barcode")
            # TODO validate values match structured vocabulary in mysite.ontologies.BASIS_OF_RECORD_VOCABULARY
            if attributes_dict.get("Basis Of Record") in ("Fossil", "FossilSpecimen", "Collection"):
                mlp_occ.basis_of_record = "FossilSpecimen"
            elif attributes_dict.get("Basis Of Record") in ("Observation", "HumanObservation"):
                mlp_occ.basis_of_record = "HumanObservation"

            #mlp_occ.basis_of_record = attributes_dict.get("Basis Of Record")

            # TODO validate values match structured vocabular in mysite.ontologies.ITEM_TYPE_VOCABULARY
            mlp_occ.item_type = attributes_dict.get("Item Type")

            field_number_datetime = datetime.datetime.strptime(attributes_dict.get("Time"), "%b %d, %Y, %H:%M %p")
            mlp_occ.field_number = field_number_datetime

            utmPoint = utm.from_latlon(firstFeature.geometry.y, firstFeature.geometry.x)
            pnt = GEOSGeometry("POINT (" + str(utmPoint[0]) + " " + str(utmPoint[1]) + ")", 32637)  # WKT
            mlp_occ.geom = pnt

            #######################
            # NON-REQUIRED FIELDS #
            #######################
            mlp_occ.item_number = mlp_occ.barcode
            mlp_occ.catalog_number = "MLP-" + str(mlp_occ.item_number)
            mlp_occ.remarks = attributes_dict.get("Remarks")
            mlp_occ.item_scientific_name = attributes_dict.get("Scientific Name")
            mlp_occ.item_description = attributes_dict.get("Description")

            mlp_occ.collecting_method = attributes_dict.get("Collection Method")
            mlp_occ.collector = attributes_dict.get("Collector")
            mlp_occ.individual_count = attributes_dict.get("Count")
            mlp_occ.year_collected = mlp_occ.field_number.year

            if attributes_dict.get("In Situ") in ('No', "NO", 'no'):
                mlp_occ.in_situ = False
            elif attributes_dict.get("In Situ") in ('Yes', "YES", 'yes'):
                mlp_occ.in_situ = True

            mlp_occ.save()

        return super(UploadKMLView, self).form_valid(form)

    def get_fiber_page_url(self):
        return reverse('mlp:mlp_upload_kml')


class Confirmation(FiberPageMixin, generic.ListView):
    template_name = 'mlp/confirmation.html'
    model = Occurrence

    def get_fiber_page_url(self):
        return reverse('mlp:upload_confirmation')


class UploadView(FiberPageMixin, generic.FormView):
    template_name = 'mlp/upload.html'
    form_class = UploadForm
    context_object_name = 'upload'
    success_url = 'confirmation'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        shapefileProper = self.request.FILES['shapefileUpload']
        shapefileIndex = self.request.FILES['shapefileIndexUpload']
        shapefileData = self.request.FILES['shapefileDataUpload']
        shapefileProperName = self.request.FILES['shapefileUpload'].name
        shapefileIndexName = self.request.FILES['shapefileIndexUpload'].name
        shapefileDataName = self.request.FILES['shapefileDataUpload'].name
        shapefileProperSaved = default_storage.save(shapefileProperName, ContentFile(shapefileProper.read()))
        shapefileIndexSaved = default_storage.save(shapefileIndexName, ContentFile(shapefileIndex.read()))
        shapefileDataSaved = default_storage.save(shapefileDataName, ContentFile(shapefileData.read()))
        shapefilePath = os.path.join(settings.MEDIA_ROOT)
        shapefileName = shapefileProperName[:shapefileProperName.rfind('.')]
        sf = shapefile.Reader(shapefilePath + "\\" + shapefileName)
        # sf = shapefile.Reader("C:\\Users\\turban\\Documents\\Development\\PyCharm\\paleocore\\media\\air_photo_areas")

        shapes = sf.shapes()
        return super(UploadView, self).form_valid(form)

    def get_fiber_page_url(self):
        return reverse('mlp:mlp_upload')