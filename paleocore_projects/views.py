from django.views import generic
from django.core.urlresolvers import reverse
from fiber.views import FiberPageMixin
from paleocore_projects.models import Project


class IndexView(FiberPageMixin, generic.ListView):
    template_name = 'paleocore_projects/projects.html'
    context_object_name = 'project_list'

    def get_queryset(self):
        # build a query set of projects.
        return Project.objects.filter(displaySummaryInfo=True)

    def get_fiber_page_url(self):
        return reverse('paleocore_projects:index')