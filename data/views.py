# Create your views here.

from django.views import generic
from models import *
from django.core.urlresolvers import reverse
from fiber.views import FiberPageMixin


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

        """Return a list of abstracts for the current meeting"""
        return Project.objects.all()

