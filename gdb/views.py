from django.conf import settings
from django.views import generic
from django.contrib.gis.geos import Point
from django.utils.html import escape
from datetime import datetime
from fastkml.kml import KML
from fastkml import Placemark, Folder, Document
from lxml import etree

import os
from zipfile import ZipFile

from .models import Locality, Biology, Occurrence
from .forms import UploadKMLForm
from mysite.settings import MEDIA_ROOT


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

        # dictionary mapping form fields (keys) to model fields (values)
        mapping = {
            'Locality': 'locality_number',
            'Existing Locality': 'locality_number',
            'Date & Time': 'date_collected',
            'DateTime': 'date_time_collected',
            'Field Number': 'field_number',
            'Basis': 'basis_of_record',
            'Item Type': 'item_type',
            'Method': 'collecting_method',
            'Image': 'image',
            'NALMA': 'NALMA',
            'Item Description': 'item_description',
            'Notes': 'notes'
        }

        def read_kml_file():
            """
            Function to open the uploaded file from the request, open the kml document in side the file and
            load the contents into a kml parser object.
            :return: returns a fastkml KLM() parser object
            """

            # TODO parse the kml file more smartly to locate the first placemark and work from there.

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

        def placemark_valid(pd):

            # locality
            # date collected
            # field number
            # basis of record
            # item type
            # collecting method
            # image
            # NALMA
            # notes
            return True

        def parse_placemark(placemark):
            """
            Parses the placemark data and writes it to the appropriate object.
            :param placemark:
            :return: returns a dictionary of key value pairs
            """
            data = placemark.description
            clean_data = data.replace('&', '&amp;')  # need to replace some special characters with html encodings
            table = etree.fromstring(clean_data)
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
            result_dict = {}
            for i in attributes_dict:
                    result_dict[mapping[i]] = attributes_dict[i]  # adds a new entry to the dictionary

            # Clean dictionary entries
            if result_dict['locality_number'] == '-None Selected-':
                result_dict['locality_number'] = None
            result_dict['image_file'] = table.xpath("//img/@src")[0]  # add image file name

            return result_dict

        def import_data(model, x, y, placemark_dictionary):
            new_obj = None
            datetime_format = "%b %d, %Y, %I:%M %p"
            if model == Biology:
                pd = placemark_dictionary
                datetime.strptime(pd['date_time_collected'], datetime_format)
                if placemark_dictionary['locality_number']:
                    locality = Locality.objects.get(pk=pd['locality_number'])
                else:
                    locality = None

                new_obj = Biology.objects.create(
                    locality=locality,
                    date_time_collected=datetime.strptime(pd['date_time_collected'], datetime_format),
                    date_last_modified=datetime.now(),
                    basis_of_record=pd['basis_of_record'],
                    item_type=pd['item_type'],
                    collecting_method=pd['collecting_method'],
                    item_description=pd['item_description'],
                    geom=Point(x, y, srid=4326),
                )
            elif model == Locality:
                pd = placemark_dictionary
                datetime.strptime(pd['date_time_collected'], datetime_format)
                new_obj = Locality.objects.create(
                    locality_field_number=pd['locality_field_number'],
                    name=pd['name'],
                    date_discovered=datetime.date(pd['date_collected']),
                    formation=pd['formation'],
                    # member=pd['member'],
                    NALMA=pd['NALMA'],
                    quad_sheet=pd['quad_sheet'],
                    resource_area=pd['resource_area'],
                    region=pd['region'],
                    blm_district=pd['blm_district'],
                    county=pd['county'],
                    notes=pd['notes'],
                    geom=Point(x, y, srid=4326),
                )

            return new_obj

        def import_images(placemark_dictionary, bio):
            image_tag = placemark_dictionary['image_file']  # e.g. 182.jpg
            for file_info in kmz_file.filelist:
                if file_info.orig_filename == image_tag:
                    # grab the image file itself
                    media_path = os.path.join(MEDIA_ROOT, 'uploads/images/gdb')
                    image_file = kmz_file.extract(file_info, media_path)
                    # image_path = image_file[:image_file.rfind(os.sep)]
                    # construct new file name
                    new_file_name = 'uploads/images/gdb' + os.sep + image_tag
                    # rename extracted file with DB record ID
                    # os.rename(image_file, new_file_name)
                    # need to strip off "media" folder from relative path saved to DB
                    # bio.image = new_file_name[new_file_name.find(os.sep) + 1:]
                    bio.image = new_file_name
                    bio.save()
                    break

        def get_doc_type(kml_obj):
            """
            Parses a kml/kmz document to determine what model or models the data are for. For
            example if the form is for Locality data or for Biology data
            :param kml_obj: a fastkml KML object
            :return: returns the appropriate model name as a string, e.g. 'Biology', 'Locality' etc.
            """
            model_name = None
            level1_elements = list(kml_obj.features())
            if len(level1_elements) == 1 and type(level1_elements[0]) == Document:
                document = level1_elements[0]
                doc_name = document.name.strip()
                if doc_name in ['Prospecting', 'Biology', 'Fossils']:
                    model_name = 'Biology'
                elif doc_name in ['Locality', 'New Locs']:
                    model_name = 'Locality'

            return model_name

        # Parse the form data and get a handle on the import file
        upload_file = self.request.FILES['kmlfileUpload']  # get a handle on the file
        file_name, file_extension = os.path.splitext(upload_file.name)  # split extension

        # Read in the kml and pass the data to the kml parser
        my_kml_obj = KML()  # initiate a kml parser object
        kml_file = None  # initiate a kml file
        if file_extension in ['.kmz', 'kmz', u'.kmz', u'kmz']:
            kmz_file = ZipFile(upload_file, 'r')  # get a handle on the zipfile
            kml_file = kmz_file.open('doc.kml', 'r').read()  # open the kml file inside the kmz
        elif file_extension == ".kml":
            # read() loads entire file as one string
            kml_file = file
        my_kml_obj.from_string(kml_file)  # pass contents of kml string to kml document instance for parsing

        model = get_doc_type(my_kml_obj)
        placemarks = get_placemarks(my_kml_obj)
        for p in placemarks:
            if type(p) is Placemark:
                p_dict = parse_placemark(p)
                if placemark_valid(p_dict):
                    nb = import_data(model, p.geometry.x, p.geometry.y, p_dict)
                    import_images(p_dict, nb)

        return super(UploadKMLView, self).form_valid(form)


class Confirmation(generic.ListView):
    template_name = 'projects/confirmation.html'
    model = Occurrence
