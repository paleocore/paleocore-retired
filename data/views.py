# Create your views here.

from django.views import generic
from models import *
from django.core.urlresolvers import reverse
from fiber.views import FiberPageMixin
from turkana.models import Turkana


class AbstractIndexView(FiberPageMixin, generic.ListView):
    # A class to combine the context for the fiber page with the general context.
    def get_fiber_page_url(self):
        return reverse('data:index')


class IndexView(AbstractIndexView):
    template_name = 'data/projects.html'
    context_object_name = 'project_list'

    def get_queryset(self):
        # build a query set of abstracts for a given meeting. The meeting_name is passed from meetings/urls.py
        #self.project = get_object_or_404(Project, title=self.kwargs["meeting_name"])


        return Project.objects.all()


class TurkanaIndexFiberView(FiberPageMixin, generic.ListView):
    def get_fiber_page_url(self):
        return reverse('data:turkana')

class TurkanaIndexView(TurkanaIndexFiberView):
    template_name = 'data/turkana.html'
    context_object_name = 'turkana_list'
    paginate_by = 25
    model = Turkana

