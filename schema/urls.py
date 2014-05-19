from django.conf.urls import patterns, url
from schema import views


urlpatterns = patterns('',
    url(r'^terms/$', 'schema.views.terms'),
    url(r'^term/(?P<id>\d+)', 'schema.views.term'),
    url(r'^ontology/(?P<category>\d+)','schema.views.classes'),
    url(r'ontologyTree/$', 'schema.views.ontologyTree'),
    url(r'ontologyTree/(?P<categoryID>\d+)','schema.views.ontologyTree'),
    url(r'^ontologyJSONtree/$', 'schema.views.ontologyJSONtree'),
)

# From IndexView of meetings app
# urlpatterns = patterns('',
#    url(r'^(?P<meeting_name>\w+)/abstracts/$', views.IndexView.as_view(), name='index'),
#    )