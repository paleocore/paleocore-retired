import json
import re
from django.views import generic
from models import *
from django.core.urlresolvers import reverse
from fiber.views import FiberPageMixin
from django.db.models import Q, get_app, get_models
from django.shortcuts import render_to_response, render
from django.template import RequestContext
from django.shortcuts import get_object_or_404

"""
Define the apps that should be listed on the data page and included in
global searches.
"""
apps = {'turkana': 'default', 'drp': 'drp_carmen'}

projects = {}

for app_name in apps.keys():
    app = get_app(app_name)
    for model in get_models(app):
        projects[model.__name__] = model


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

"""
class TurkanaIndexFiberView(FiberPageMixin, generic.ListView):
    def get_fiber_page_url(self):
        return reverse('data:turkana')

class TurkanaIndexView(TurkanaIndexFiberView):
    template_name = 'data/turkana.html'
    context_object_name = 'turkana_list'
    paginate_by = 25
    model = Turkana
"""


def project_data_display(request, project_name):
    project = projects[str(project_name)]
    fields = project.fields_to_display()

    if request.method == 'GET':
        # Populating a dictionary with key/values of the form "field: CHOICE_SET",
        # where CHOICE_SET is a tuple of tuples populated with all of the distinct
        # values of that field and the null option, which is seen as "Select:"
        choices_list = {}
        for field in fields:
            choices_list[field] = (('', 'Select:'),)
            # We need the "using" so that data can be hosted on multiple databases
            for datum in sorted(project.objects.using(apps[project._meta.app_label]).values_list(field).distinct()):
                if datum[0] is not None:
                    choices_list[field] += ((datum[0], datum[0]),)

        selector_choices = json.dumps(choices_list)

        site_data = project.objects.all()

        return render_to_response('data/project_data_display.html', {'fields': fields,
                                                                'project_name': project_name,
                                                                'selector_choices': selector_choices,
                                                                'data': site_data}, RequestContext(request))

    if request.is_ajax():
        post_action = request.POST['post_action']
        if post_action == 'search_box_query':
            query = request.POST['query']
            query_set = None
            datum_attributes_lists = []

            if query.strip():
                query_set = project.objects.filter(get_query(fields, query)).all()

            # This is necessary because of our generalization. There is no way to call the fields of each specific piece
            # of data in the templates, because the fields vary. Therefore, that work must be done here.
            for item in query_set:
                datum_attributes_lists.append([item[field] for field in fields])

            return render_to_response('data/project_data_display.html',
                                      {'datum_attributes_lists': datum_attributes_lists, 'fields': fields},
                                      RequestContext(request))

####################################FOR QUERY PURPOSES###########################################

#Credit: http://www.julienphalip.com/blog/2008/08/16/adding-search-django-site-snap/

#Splits the query string in invidual keywords, getting rid of unecessary spaces and grouping quoted words together.


def normalize_query(query_string,
                    findterms=re.compile(r'"([^"]+)"|(\S+)').findall,
                    normspace=re.compile(r'\s{2,}').sub):
    return [normspace(' ', (t[0] or t[1]).strip()) for t in findterms(query_string)]

#Returns a query, that is a combination of Q objects. That combination aims to search keywords within a model by
#testing the given search fields.


def get_query(fields, query_string):
    query = None  # Query to search for every search term
    terms = normalize_query(query_string)
    for term in terms:
        or_query = None  # Query to search for a given term in each field
        for field in fields:
            q = Q(**{'%s__icontains' % field: term})
            if or_query is None:
                or_query = q
            else:
                or_query = or_query | q
        if query is None:
            query = or_query
        else:
            query = query & or_query
    return query