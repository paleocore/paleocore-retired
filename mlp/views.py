from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.conf import settings
from django.views import generic
import os
import shutil
from models import *
from models import mlp_occurrence
from django.core.urlresolvers import reverse
from fiber.views import FiberPageMixin
import shapefile
from mlp.forms import UploadForm, UploadKMLForm, DownloadKMLForm, ChangeXYForm
from fastkml import kml
from fastkml import Placemark
from lxml import etree
from datetime import datetime
from django.contrib.gis.geos import GEOSGeometry
import utm
from zipfile import ZipFile
from shapely.geometry import Point, LineString, Polygon
from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.contrib import messages


class DownloadKMLView(FiberPageMixin, generic.FormView):
    template_name = 'mlp/download_kml.html'
    form_class = DownloadKMLForm
    context_object_name = 'download'
    success_url = '/mlp/confirmation/'

    def form_valid(self, form):
        k = kml.KML()
        ns = '{http://www.opengis.net/kml/2.2}'
        d = kml.Document(ns, 'docid', 'MLP Observations', 'KML Document')
        f = kml.Folder(ns, 'fid', 'MLP Observations Root Folder', 'Contains place marks for specimens and observations.')
        k.append(d)
        d.append(f)
        os = mlp_occurrence.objects.all()
        for o in os:
            if (o.geom):
                p = kml.Placemark(ns, 'id', 'name', 'description')
                #coord = utm.to_latlon(o.geom.coords[0], o.geom.coords[1], 37, 'P')
                pnt = Point(o.geom.coords[0], o.geom.coords[1])
                p.name = o.__str__()
                d = "<![CDATA[<table>"
                openrow = "<tr><td>"
                middlerow = "</td><td style='font-weight:bold'>"
                closerow = "</td></tr>"

                d += openrow
                d += ''.join(("Basis of Record", middlerow))
                d += ''.join(filter(None, (o.basis_of_record, closerow, openrow)))
                d += ''.join(("Time", middlerow))
                d += ''.join(filter(None, (str(o.field_number), closerow, openrow)))
                d += ''.join(("Item Type", middlerow))
                d += ''.join(filter(None, (o.item_type, closerow, openrow)))
                d += ''.join(("Collector", middlerow))
                d += ''.join(filter(None, (o.collector, closerow, openrow)))
                d += ''.join(("Collection Method", middlerow))
                d += ''.join(filter(None, (o.collecting_method, closerow, openrow)))
                d += ''.join(("Count", middlerow))
                d += ''.join(filter(None, (str(o.individual_count), closerow, openrow)))
                d += ''.join(("Bar Code", middlerow))
                d += ''.join(filter(None, (str(o.barcode), closerow, openrow)))
                d += ''.join(("Scientific Name", middlerow))
                d += ''.join(filter(None, (o.item_scientific_name, closerow, openrow)))
                d += ''.join(("Description", middlerow))
                d += ''.join(filter(None, (o.item_description, closerow, openrow)))
                d += ''.join(("Remarks", middlerow))
                d += ''.join(filter(None, (o.remarks, closerow, openrow)))
                d += ''.join(("In Situ", middlerow))
                d += ''.join(filter(None, (str(o.in_situ), closerow)))
                d += "</table>"
                p.description = d
                p.geometry = pnt
                f.append(p)
        r = k.to_string(prettyprint=True)
        response = HttpResponse(r, mimetype='text/plain')
        response['Content-Disposition'] = 'attachment; filename="mlp.kml"'
        return response

    def get_fiber_page_url(self):
        return reverse('mlp:mlp_download_kml')


class UploadKMLView(FiberPageMixin, generic.FormView):
    template_name = 'mlp/upload_kml.html'
    form_class = UploadKMLForm
    context_object_name = 'upload'
    success_url = '/mlp/confirmation/'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.

        # TODO parse the kml file more smartly to locate the first placemark and work from there.
        # TODO ingest kmz and kml. See the zipfile python library
        KML_file_upload = self.request.FILES['kmlfileUpload']  # get a handle on the file
        KML_file_upload_name = self.request.FILES['kmlfileUpload'].name  # get the file name
        KML_file_name = KML_file_upload_name[:KML_file_upload_name.rfind('.')]  # get the file name no extension
        KML_file_extension = KML_file_upload_name[KML_file_upload_name.rfind('.')+1:]  # get the file extension

        #default_storage.save(KML_file_upload_name, ContentFile(KML_file_upload.read()))  # save a temp copy of the file to the default location, /media/
        KML_file_path = os.path.join(settings.MEDIA_ROOT)

        # TODO: Check for file extension other than kml or kmz
        KML_file = kml.KML()
        if KML_file_extension == "kmz":
            KMZ_file = ZipFile(KML_file_upload, 'r')
            #KMZ_file = ZipFile(KML_file_path + "/" + KML_file_upload_name, 'r')
            KML_document = KMZ_file.open('doc.kml', 'r').read()
        else:
            KML_document = open(KML_file_path + "/" + KML_file_upload_name, 'r').read()  # read() loads entire file as one string

        KML_file.from_string(KML_document)
        # get the top level features object (this is essentially the layers list)
        layers = KML_file._features
        # We expect only a single layer (i.e. occurrences)
        # get the first element and then get the features associated with that layer.
        occurrences = list(layers[0].features())

        feature_count = 0

        for o in occurrences:

            # Check to make sure that the object is a Placemark, filter out folder objects
            if type(o) is Placemark:

                table = etree.fromstring(o.description)
                attributes = table.xpath("//text()")
                # TODO test attributes is even length
                attributes_dict = dict(zip(attributes[0::2], attributes[1::2]))

                mlp_occ = mlp_occurrence()

                ###################
                # REQUIRED FIELDS #
                ###################

                # Validate Basis of Record
                if attributes_dict.get("Basis Of Record") in ("Fossil", "FossilSpecimen", "Collection"):
                    mlp_occ.basis_of_record = "FossilSpecimen"
                elif attributes_dict.get("Basis Of Record") in ("Observation", "HumanObservation"):
                    mlp_occ.basis_of_record = "HumanObservation"

                # Validate Item Type
                item_type = attributes_dict.get("Item Type")
                if item_type in ("Artifact", "Artifactual", "Archeology", "Archaeological"):
                    mlp_occ.item_type = "Artifactual"
                elif item_type in ("Faunal", "Fauna"):
                    mlp_occ.item_type = "Faunal"
                elif item_type in ("Floral", "Flora"):
                    mlp_occ.item_type = "Floral"
                elif item_type in ("Geological", "Geology"):
                    mlp_occ.item_type = "Geological"

                # Field Number
                try:
                    mlp_occ.field_number = datetime.strptime(attributes_dict.get("Time"), "%b %d, %Y, %I:%M %p")  # parse field nubmer
                    mlp_occ.year_collected = mlp_occ.field_number.year  # set the year collected form field number
                except ValueError:
                    mlp_occ.field_number = datetime.now()
                    mlp_occ.problem = True
                    try:
                        error_string = "Upload error, missing field number, using current date and time instead."
                        mlp_occ.problem_comment = mlp_occ.problem_comment + " " +error_string
                    except TypeError:
                        mlp_occ.problem_comment = error_string

                #utmPoint = utm.from_latlon(o.geometry.y, o.geometry.x)

                # Process point, comes in as well known text string
                # Assuming point is in GCS WGS84 datum = SRID 4326
                pnt = GEOSGeometry("POINT (" + str(o.geometry.x) + " " + str(o.geometry.y) + ")", 4326)  # WKT
                mlp_occ.geom = pnt

                #######################
                # NON-REQUIRED FIELDS #
                #######################
                mlp_occ.barcode = attributes_dict.get("Barcode")
                mlp_occ.item_number = mlp_occ.barcode
                mlp_occ.catalog_number = "MLP-" + str(mlp_occ.item_number)
                mlp_occ.remarks = attributes_dict.get("Remarks")
                mlp_occ.item_scientific_name = attributes_dict.get("Scientific Name")
                mlp_occ.item_description = attributes_dict.get("Description")


                # Validate Collecting Method
                collection_method = attributes_dict.get("Collection Method")
                if collection_method in ("Surface Standard", "Standard"):
                    mlp_occ.collecting_method = "Surface Standard"
                elif collection_method in ("Surface Intensive", "Intensive"):
                    mlp_occ.collecting_method = "Surface Intensive"
                elif collection_method in ("Surface Complete", "Complete"):
                    mlp_occ.collecting_method = "Surface Complete"
                elif collection_method in ("Exploratory Survey", "Exploratory"):
                    mlp_occ.collecting_method = "Exploratory Survey"
                elif collection_method in ("Dry Screen 5mm", "Dry Screen 5 Mm", "Dry Screen 5 mm"):
                    mlp_occ.collecting_method = "Dry Screen 5mm"
                elif collection_method in ("Dry Screen 2mm", "Dry Screen 2 Mm", "Dry Screen 2 mm"):
                    mlp_occ.collecting_method = "Dry Screen 2mm"
                elif collection_method in ("Dry Screen 1mm", "Dry Screen 1 Mm", "Dry Screen 1 mm"):
                    mlp_occ.collecting_method = "Dry Screen 1mm"
                # else:
                #     mlp_occ.collecting_method = None
                #     mlp_occ.problem = True
                #     mlp_occ.problem_comment = mlp_occ.problem_comment + " problem importing collecting method"

                mlp_occ.collecting_method = attributes_dict.get("Collection Method")
                mlp_occ.collector = attributes_dict.get("Collector")
                mlp_occ.individual_count = attributes_dict.get("Count")
                #if mlp_occ:
                #    mlp_occ.year_collected = mlp_occ.field_number.year

                if attributes_dict.get("In Situ") in ('No', "NO", 'no'):
                    mlp_occ.in_situ = False
                elif attributes_dict.get("In Situ") in ('Yes', "YES", 'yes'):
                    mlp_occ.in_situ = True

                ##############
                # Save Image #
                ##############
                image_file = ""
                image_added = False
                # Now look for images if this is a KMZ
                if KML_file_extension.lower() == "kmz":
                    # grab image names from XML
                    image_tags = table.xpath("//img/@src")
                    # grab the name of the first image
                    try:
                        image_tag = image_tags[0]
                        # grab the file info from the zip list
                        for file_info in KMZ_file.filelist:
                            if image_tag == file_info.orig_filename:
                                # grab the image file itself
                                image_file = KMZ_file.extract(file_info, "media/uploads/images/mlp")
                                image_added = True
                                break
                    except IndexError:
                        pass

                mlp_occ.save()
                # need to save record before adding image in order to obtain the DB ID
                if image_added:
                    # strip off the file name from the path
                    image_path = image_file[:image_file.rfind(os.sep)]
                    # construct new file name
                    new_file_name = image_path + os.sep + str(mlp_occ.id) + "_" + image_tag
                    # rename extracted file with DB record ID
                    os.rename(image_file, new_file_name)
                    # need to strip off "media" folder from relative path saved to DB
                    mlp_occ.image = new_file_name[new_file_name.find(os.sep)+1:]
                    mlp_occ.save()
                feature_count += 1

                # TODO If item type is Fauna or Flora add to Biology table

                    # loop through each attachment
                    # for attachment in image_tags:
                    #     # find the relevant attachment
                    #     for file_info in KMZ_file.filelist:
                    #         if attachment == file_info.orig_filename:
                    #             # extract file from kmz to the working directory
                    #             attachment_file = KMZ_file.extract(file_info)  # get a file object
                    #             # calculate new file name based on record id and original name
                    #             new_file_name = str(mlp_occ.id) + "_" + file_info.orig_filename
                    #             # calculate destination directory
                    #             #complete_name = os.path.join(KML_file_path, "imports/" + new_file_name)
                    #             # move file
                    #             #shutil.move(attachment_file, complete_name)
                    #             # save image name to DB
                    #             mlp_occ.image = new_file_name
                    #             mlp_occ.save()
                    #             break
                    #         break


        return super(UploadKMLView, self).form_valid(form)

    def get_fiber_page_url(self):
        return reverse('mlp:mlp_upload_kml')


class Confirmation(FiberPageMixin, generic.ListView):
    template_name = 'mlp/confirmation.html'
    model = mlp_occurrence

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

def ChangeXYView(request):
    if request.method == "POST":
        form = ChangeXYForm(request.POST)
        if form.is_valid():
            obs = mlp_occurrence.objects.get(pk=request.POST["DB_id"])
            latlong = utm.to_latlon(int(request.POST["new_easting"]), int(request.POST["new_northing"]),37,"N")
            pnt = GEOSGeometry("POINT (" + str(latlong[1]) + " " + str(latlong[0]) + ")", 4326)  # WKT
            obs.geom = pnt
            obs.save()
            messages.add_message(request, messages.INFO, 'Successfully Updated Coordinates For %s.' % obs.catalog_number )
            return redirect("/admin/mlp/occurrence")
    else:
        selected = list(request.GET.get("ids", "").split(","))
        if len(selected) > 1:
            messages.error(request,"You can't change the coordinates of multiple points at once.")
            return redirect("/admin/mlp/occurrence")
        selected_object = mlp_occurrence.objects.get(pk=int(selected[0]))
        initialData = { "DB_id":selected_object.id,
                        "barcode":selected_object.barcode,
                        "old_easting":selected_object.easting,
                        "old_northing":selected_object.northing,
                        "item_scientific_name":selected_object.item_scientific_name,
                        "item_description":selected_object.item_description
                    }
        theForm = ChangeXYForm(initial = initialData)
        return render_to_response('mlp/changeXY.html',
                                {"theForm":theForm},
                              RequestContext(request))

