from django.views import generic
from django.core.urlresolvers import reverse
from fiber.views import FiberPageMixin
from paleocore_projects.models import Project
from django.shortcuts import HttpResponseRedirect


class IndexView(FiberPageMixin, generic.ListView):
    template_name = 'paleocore_projects/project_list.html'
    context_object_name = 'project_list'

    def get_queryset(self):
        # build a query set of projects.
        return Project.objects.filter(displaySummaryInfo=True)

    def get_fiber_page_url(self):
        return reverse('paleocore_projects:index')

class DetailView(FiberPageMixin, generic.DetailView):
    template_name = 'paleocore_projects/project_detail.html'
    context_object_name = 'project'
    model = Project

    #I don't use fiber at all, so hard code a fiber page (pk=1)
    def get_fiber_page_url(self):
        return reverse('paleocore_projects:detail', kwargs={'pk':1})

def redirectDetailViewMissingPK(request):
    return HttpResponseRedirect(reverse('paleocore_projects:detail', kwargs={'pk':1}))