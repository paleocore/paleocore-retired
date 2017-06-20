from django.conf import settings
from django.views import generic
from django.contrib.gis.geos import Point
from datetime import datetime
from fastkml.kml import KML
from fastkml import Placemark, Folder, Document
from lxml import etree

import os
from zipfile import ZipFile

from .models import Locality, Biology, Occurrence
from .forms import UploadKMLForm


class UploadKMLView(generic.FormView):
    """
    Change name to ImportKML
    """
    template_name = 'projects/upload_kml.html'
    form_class = UploadKMLForm
    context_object_name = 'upload'
    # For some reason reverse cannot be used to define the success_url. For example the following line raises an error.
    # e.g. success_url = reverse("projects:gdb:gdb_upload_confirmation")
    success_url = '/projects/gdb/confirmation/'  # but this does work.

    def form_valid(self, form):
        """
        This method is called when valid form data has been POSTed.
        :param form:
        :return: returns and HttpResponse acknowledging the data have been uploaded
        """
        upload_file = self.request.FILES['kmlfileUpload']  # get a handle on the file
        file_name, file_extension = os.path.splitext(upload_file.name)  # split extension

        def read_kml_file():
            """
            Function to open the uploaded file from the request, open the kml document in side the file and
            load the contents into a kml parser object.
            :return: returns a fastkml KLM() parser object
            """

            # TODO parse the kml file more smartly to locate the first placemark and work from there.
            # TODO ingest kmz and kml. See the zipfile python library

            kml_obj = KML()  # initiate a kml parser object
            kml_file = None  # initiate a kml file
            if file_extension in ['.kmz', 'kmz', u'.kmz', u'kmz']:
                kmz_file = ZipFile(upload_file, 'r')  # get a handle on the zipfile
                kml_file = kmz_file.open('doc.kml', 'r').read()  # open the kml file inside the kmz
            elif file_extension == ".kml":
                # read() loads entire file as one string
                kml_file = file
            kml_obj.from_string(kml_file)  # pass contents of kml string to kml document instance for parsing
            return kml_obj

        def get_placemarks(kml_obj):
            placemark_list = []
            # get the top level features object (this is essentially the layers list)
            level1_elements = list(kml_obj.features())
            # Check that the kml file is well-formed with a single document element.
            if len(level1_elements) == 1 and type(level1_elements[0]) == Document:
                document = level1_elements[0]

                #  If well-formed document, check if the file has folders, which correspond to layers
                level2_elements = list(document.features())
                if len(level2_elements) == 1 and type(level2_elements[0]) == Folder:
                    folder = level2_elements[0]

                    #  If a single folder is present import placemarks from that folder
                    #  Get features from the folder
                    level3_elements = list(folder.features())
                    #  Check that the features are Placemarks. If they are, return them in a list
                    if len(level3_elements) >= 1 and type(level3_elements[0]) == Placemark:
                        placemark_list = level3_elements

                elif len(level2_elements) >= 1 and type(level2_elements[0]) == Placemark:
                    placemark_list = level2_elements
            return placemark_list

        def placemark_valid(placemark):
            return True

        def import_placemark(p):
            """
            Parses the placemark data and writes it to the appropriate object.
            :param placemark:
            :return:
            """
            table = etree.fromstring(p.description)
            attributes = table.xpath("//text()|//img")
            # TODO test attributes is even length
            # Create a dictionary from the attribute list. The list has key value pairs as alternating
            # elements in the list, the line below takes the first and every other elements and adds them
            # as keys, then the second and every other element and adds them as values.
            # e.g.
            # attributes[0::2] = ["Basis of Record", "Time", "Item Type" ...]
            # attributes[1::2] = ["Collection", "May 27, 2017, 10:12 AM", "Faunal" ...]
            # zip creates a list of tuples  = [("Basis of Record", "Collection), ...]
            # which is converted to a dictionary.
            attributes_dict = dict(zip(attributes[0::2], attributes[1::2]))

            return attributes_dict

        kml = read_kml_file()
        placemarks = get_placemarks(kml)
        for p in placemarks:
            if type(p) is Placemark:
                p_dict = import_placemark(p)

        return super(UploadKMLView, self).form_valid(form)


class Confirmation(generic.ListView):
    template_name = 'projects/confirmation.html'
    model = Occurrence