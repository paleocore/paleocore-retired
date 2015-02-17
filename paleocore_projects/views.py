from django.views import generic
from django.core.urlresolvers import reverse
from fiber.views import FiberPageMixin
from paleocore_projects.models import Project
from django.shortcuts import HttpResponseRedirect, HttpResponse, Http404
from django.db.models.loading import get_model
from django.core import serializers

class ProjectIndexView(FiberPageMixin, generic.ListView):
    template_name = 'paleocore_projects/project_list.html'
    context_object_name = 'project_list'

    # This doesn't quite work yet.  I get a list of counts returned to the template
    # But it doesn't necessarily match up with the projects in the project_list
    # returned by default in the context object
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(ProjectIndexView, self).get_context_data(**kwargs)
        counts={}
        for proj in Project.objects.all():
            model = get_model(proj.paleocore_appname, proj.occurrence_table_name)
            try:
                counts[proj.paleocore_appname] = model.objects.all().count()
            except:
                counts[proj.paleocore_appname] = "Unknown occurrence count"
        context["counts"] = counts
        return context

    def get_queryset(self):
        # build a query set of projects.
        return Project.objects.filter(display_summary_info=True)

    def get_fiber_page_url(self):
        return reverse('paleocore_projects:index')

class ProjectDetailView(FiberPageMixin, generic.DetailView):
    template_name = 'paleocore_projects/project_detail.html'
    context_object_name = 'project'

    def get_object(self):
        return Project.objects.get(paleocore_appname = self.kwargs["pcoreapp"])

    #I don't use fiber at all, so hard code a fiber page (pk=1)
    def get_fiber_page_url(self):
        return reverse('paleocore_projects:detail', kwargs={'pcoreapp':"drp"})

class ProjectDataView(FiberPageMixin, generic.ListView):
    template_name = 'paleocore_projects/project_data.html'
    context_object_name = 'occurrences'

    def get_queryset(self):
        proj = Project.objects.get(paleocore_appname = self.kwargs["pcoreapp"])
        model = get_model(proj.paleocore_appname, proj.occurrence_table_name)
        return model.objects.all()

    def get_fiber_page_url(self):
        return reverse('paleocore_projects:index')

def redirectDetailViewMissingPK(request):
    return HttpResponseRedirect(reverse('paleocore_projects:detail', kwargs={'pk':1}))


def ajaxProjectData(request, pcoreapp="drp"):
    response = HttpResponse(mimetype='application/json')
    project = Project.objects.get(paleocore_appname = pcoreapp)
    model = get_model(pcoreapp, project.occurrence_table_name)
    permission_string = pcoreapp + ".change_" + project.occurrence_table_name
    if request.user.has_perm(permission_string):
        serializers.serialize("json", model.objects.all(), fields=project.display_fields, stream=response)
    else:
        pass
    return response

class ProjectDataTable(FiberPageMixin, generic.DetailView):
    template_name = 'paleocore_projects/project_data.html'

    def get_object(self):
        return Project.objects.get(paleocore_appname = self.kwargs["pcoreapp"])

    def get_fiber_page_url(self):
        return reverse('paleocore_projects:index')