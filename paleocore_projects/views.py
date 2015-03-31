from django.views import generic
from django.core.urlresolvers import reverse
from fiber.views import FiberPageMixin
from paleocore_projects.models import Project
from django.shortcuts import HttpResponseRedirect, HttpResponse, render_to_response, get_object_or_404
from django.db.models.loading import get_model
from django.template import RequestContext
import json
from ast import literal_eval
from django.forms.models import model_to_dict

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


class OccurrenceDetailView(FiberPageMixin, generic.DetailView):
    template_name = 'paleocore_projects/occurrence_detail.html'
    context_object_name = 'occurrence'

    def get_context_data(self, **kwargs):
        context = super(OccurrenceDetailView, self).get_context_data(**kwargs)
        proj = Project.objects.get(paleocore_appname = self.kwargs["pcoreapp"])
        context['project'] = proj.full_name
        return context

    def get_object(self):
        proj = Project.objects.get(paleocore_appname = self.kwargs["pcoreapp"])
        model = get_model(proj.paleocore_appname, proj.occurrence_table_name)
        #test for permissions if project is NOT public
        if not proj.is_public:
            permission_string = self.kwargs["pcoreapp"] + ".change_" + proj.occurrence_table_name
            if not self.request.user.has_perm(permission_string):
                return {"unauthorized":"You are not authorized to view this data."}
                #bail out if user doesn't have permission for non public project
        return model_to_dict(model.objects.get(pk = self.kwargs["occurrenceid"]))

    #I don't use fiber at all, so hard code a fiber page (pk=1)
    def get_fiber_page_url(self):
        return reverse('paleocore_projects:detail', kwargs={'pcoreapp':"drp"})

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


#view that returns ajax data for a given project
#after testing that user has permission for the project
def ajaxProjectData(request, pcoreapp):
    response = HttpResponse(mimetype='application/json')
    project = Project.objects.get(paleocore_appname = pcoreapp)

    #test for permissions if project is NOT public
    if not project.is_public:
        permission_string = pcoreapp + ".change_" + project.occurrence_table_name
        if not request.user.has_perm(permission_string):
            return HttpResponse(json.dumps([{"error":"unauthorized"}]))
            #bail out if user doesn't have permission for non public project

    #go fetch whatever model is the occurrence table equivalent for this app
    model = get_model(pcoreapp, project.occurrence_table_name)

    #build up admin style filter arguments from url string
    filterArgs = {}
    for key,value in request.GET.iteritems():
        if value:
            if value <> "":
                filterArgs[key] = value

    try: #remove url GET parameter put in by DataTables
        cleanedFilterArgs = filterArgs
        cleanedFilterArgs.pop("_")
    except:
        cleanedFilterArgs = filterArgs

    responsedict = {"data":[]}
    if filterArgs:
        objects = model.objects.filter(** cleanedFilterArgs).values_list(* literal_eval(project.display_fields))
        for object in objects:
            responsedict["data"].append(object)
        response.write(json.dumps(responsedict))
    else:
        objects = model.objects.all().values_list(* literal_eval(project.display_fields))
        for object in objects:
            responsedict["data"].append(object)
        response.write(json.dumps(responsedict))

    return response

#all this does is render a template with two context variables
#it is kind of like a detail generic class based view with added context
#but I couldn't figure out how to access the request.GET parameters using a generic view
#so I opted for a simple functional view.
def projectDataTable(request, pcoreapp="drp"):
    project = get_object_or_404(Project, paleocore_appname = pcoreapp)
    filterArgs = {}
    for key,value in request.GET.iteritems():
        if value:
            if value <> "":
                filterArgs[key] = value

    #build list of unique values for fields to filter on
    model = get_model(project.paleocore_appname, project.occurrence_table_name)
    filterChoices = {}
    for field in literal_eval(project.display_filter_fields):
        filterChoices[field] = sorted(model.objects.order_by().values_list(field, flat=True).distinct())

    return render_to_response('paleocore_projects/project_data.html',
                             {"project": project,
                              "displayFields":literal_eval(project.display_fields),
                              "filterChoices":filterChoices,
                              "filterArgs":filterArgs },
                          context_instance=RequestContext(request))
