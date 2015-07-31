from django.conf.urls import patterns, url
from standard import views as standard_views
from standard import views


urlpatterns = patterns('',
    # e.g. /standard/
    url(r'^$', standard_views.PaleocoreTermsIndexView.as_view(), name="paleocore_terms_index"),

    # e.g. /standard/term/3/
    url(r'^term/(?P<id>\d+)', 'standard.views.term', name="term"),

    # e.g. /addTerm/PaleoCore/
    #url(r'^addTerm/(?P<referringCategory>\d+)', 'standard.views.addTerm', name="addTerm"),
    #url(r'^addClass/', 'standard.views.addClass', name="addClass"),
    #url(r'^addTerm/', 'standard.views.addTerm', name="addTermNoParameter"),

    # e.g. /standard/ontology/
    # url(r'^ontology/$', 'standard.views.ontology', name="ontology"),
    # url(r'^ontology/(?P<category>\d+)', 'standard.views.classes', name="ontologyClass"),
    # url(r'^ontologyTree/$', 'standard.views.ontologyTree', name="ontologyTreeNoParameter"),
    # url(r'^ontologyTree/(?P<categoryID>\d+)', 'standard.views.ontologyTree', name="ontologyTree"),
    # url(r'^ontologyJSONtree/$', 'standard.views.ontologyJSONtree', name="ontologyJSONtree"),
    # url(r'^(?P<project_name>\w+)/terms/$', views.TermsIndexView.as_view(), name='index'),
)

# From IndexView of meetings app
# urlpatterns = patterns('',
#    url(r'^(?P<meeting_name>\w+)/abstracts/$', views.IndexView.as_view(), name='index'),
#    )