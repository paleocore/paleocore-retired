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
from mlp.forms import UploadForm

# Create your views here.
class UploadView(FiberPageMixin, generic.FormView):
    template_name = 'mlp/upload.html'
    form_class = UploadForm
    context_object_name = 'upload'
    success_url = 'mlp/upload'

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