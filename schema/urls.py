from django.conf.urls import patterns, url
from schema import views


urlpatterns = patterns('',
    url(r'^terms/$', 'schema.views.terms', name="termsNoParameter"),
    url(r'^term/(?P<id>\d+)', 'schema.views.term', name="term"),
    url(r'^addTerm/(?P<referringCategory>\d+)', 'schema.views.addTerm', name="addTerm"),
    url(r'^addClass/', 'schema.views.addClass', name="addClass"),
    url(r'^addTerm/', 'schema.views.addTerm', name="addTermNoParameter"),
    url(r'^ontology/$', 'schema.views.ontology', name="ontology"),
    url(r'^ontology/(?P<category>\d+)','schema.views.classes', name="ontologyClass"),
    url(r'^ontologyTree/$', 'schema.views.ontologyTree', name="ontologyTreeNoParameter"),
    url(r'^ontologyTree/(?P<categoryID>\d+)','schema.views.ontologyTree', name="ontologyTree"),
    url(r'^ontologyJSONtree/$', 'schema.views.ontologyJSONtree', name="ontologyJSONtree"),
    url(r'^(?P<project_name>\w+)/terms/$', views.TermsIndexView.as_view(), name='index'),
)

# From IndexView of meetings app
# urlpatterns = patterns('',
#    url(r'^(?P<meeting_name>\w+)/abstracts/$', views.IndexView.as_view(), name='index'),
#    )