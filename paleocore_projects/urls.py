from django.conf.urls import patterns, url
from paleocore_projects import views
from paleocore_projects.models import Project
from djgeojson.views import GeoJSONLayerView



urlpatterns = patterns('paleocore_projects.views',
                       # ex. /projects/
                       url(r'^data/(?P<pcoreapp>.+)/$', views.ProjectDataView.as_view(), name='data'),
                       url(r'^data/(?P<pcoreapp>.+)/(?P<occurrenceid>\d+)$', views.OccurrenceDetailView.as_view(), name='occurrence_detail'),
                       url(r'^data_json/(?P<pcoreapp>.+)/$', views.ajaxProjectData, name='data_json'),
                       url(r'^data_table/(?P<pcoreapp>.+)/$', views.projectDataTable, name='data_table'),
                       url(r'^(?P<pcoreapp>.+)/$', views.ProjectDetailView.as_view(), name='detail'),
                       url(r'^projects.geojson$', GeoJSONLayerView.as_view(model=Project, properties=("full_name","paleocore_appname")), name='projects_geojson'),
                       url(r'^$', views.ProjectIndexView.as_view(), name='index')
                       )