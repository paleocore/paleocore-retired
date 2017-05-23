from django.views import generic
from projects.models import Project
from django.shortcuts import HttpResponse, render_to_response
from django.db.models.loading import get_model
from django.template import RequestContext
import json
from ast import literal_eval
from django.forms.models import model_to_dict
from django.shortcuts import get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from mysite.settings import INSTALLED_APPS


class ProjectIndexView(generic.ListView):
    template_name = 'projects/project_list.html'
    context_object_name = 'project_list'

    def get_queryset(self):
        # build a query set of projects.
        return Project.objects.filter(display_summary_info=True,  # get projects with public summaries
                                      is_standard=False,  # don't get standards such as darwin core
                                      paleocore_appname__in=INSTALLED_APPS)  # verify project app is installed


class ProjectDetailView(generic.DetailView):
    template_name = 'projects/project_detail.html'
    context_object_name = 'project'

    def get_object(self):
        return Project.objects.get(paleocore_appname=self.kwargs["pcoreapp"])


class ProjectSummaryView(generic.DateDetailView):
    template_name = 'projects/project_summary.html'
    context_object_name = 'project'

    def get_object(self):
        return Project.objects.get(paleocore_appname=self.kwargs["pcoreapp"])


class OccurrenceDetailView(generic.DetailView):
    template_name = 'projects/occurrence_detail.html'
    context_object_name = 'occurrence'

    def get_context_data(self, **kwargs):
        context = super(OccurrenceDetailView, self).get_context_data(**kwargs)
        proj = Project.objects.get(paleocore_appname=self.kwargs["pcoreapp"])
        context['project'] = proj.full_name
        return context

    def get_object(self):
        proj = get_object_or_404(Project, paleocore_appname=self.kwargs["pcoreapp"])
        try:
            model = get_model(proj.paleocore_appname, proj.occurrence_table_name)
        except ObjectDoesNotExist:
            raise Http404("Django application does not exist")
        # test for permissions if project is NOT public
        if not proj.is_public:
            permission_string = self.kwargs["pcoreapp"] + ".change_" + proj.occurrence_table_name
            if not self.request.user.has_perm(permission_string):
                return {"unauthorized": "You are not authorized to view this data."}
                # bail out if user doesn't have permission for non public project

        detail_object = get_object_or_404(model, pk=self.kwargs["occurrence_id"])
        return model_to_dict(detail_object)


class ProjectDataView(generic.ListView):
    template_name = 'projects/project_data.html'
    context_object_name = 'occurrences'

    def get_queryset(self):
        proj = Project.objects.get(paleocore_appname=self.kwargs["pcoreapp"])
        model = get_model(proj.paleocore_appname, proj.occurrence_table_name)
        return model.objects.all()


# view that returns ajax data for a given project
# after testing that user has permission for the project
def ajaxProjectData(request, pcoreapp):
    response = HttpResponse(content_type='application/json')
    project = Project.objects.get(paleocore_appname=pcoreapp)

    # test for permissions if project is NOT public
    if not project.is_public:
        permission_string = pcoreapp + ".change_" + project.occurrence_table_name
        if not request.user.has_perm(permission_string):
            return HttpResponse(json.dumps([{"error": "unauthorized"}]))
            # bail out if user doesn't have permission for non public project

    # go fetch whatever model is the occurrence table equivalent for this app
    model = get_model(pcoreapp, project.occurrence_table_name)

    # build up admin style filter arguments from url string
    filterArgs = {}
    for key, value in request.GET.iteritems():
        if value:
            if value != "":
                filterArgs[key] = value

    try:  # remove url GET parameter put in by DataTables
        cleaned_filter_args = filterArgs
        cleaned_filter_args.pop("_")
    except:
        cleaned_filter_args = filterArgs

    responsedict = {"data":[]}
    if filterArgs:
        objects = model.objects.filter(** cleaned_filter_args).values_list(* literal_eval(project.display_fields))
        for obj in objects:
            responsedict["data"].append(obj)
        response.write(json.dumps(responsedict))
    else:
        model_objects = model.objects.all().values_list(* literal_eval(project.display_fields))
        for model_object in model_objects:
            responsedict["data"].append(model_object)
        response.write(json.dumps(responsedict))

    return response


# all this does is render a template with two context variables
# it is kind of like a detail generic class based view with added context
# but I couldn't figure out how to access the request.GET parameters using a generic view
# so I opted for a simple functional view.
def projectDataTable(request, pcoreapp="drp"):
    project = get_object_or_404(Project, paleocore_appname = pcoreapp)
    filter_args = {}
    for key, value in request.GET.iteritems():
        if value:
            if value != "":
                filter_args[key] = value

    # build list of unique values for fields to filter on
    model = get_model(project.paleocore_appname, project.occurrence_table_name)
    filter_choices = {}
    for field in literal_eval(project.display_filter_fields):
        filter_choices[field] = sorted(model.objects.order_by().values_list(field, flat=True).distinct())

    return render_to_response('projects/project_data.html',
                              {"project": project,
                               "displayFields": literal_eval(project.display_fields),
                               "filterChoices": filter_choices,
                               "filterArgs": filter_args},
                              context_instance=RequestContext(request))
