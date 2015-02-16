from django.conf.urls import patterns, url
from paleocore_projects import views
from paleocore_projects.models import Project
from djgeojson.views import GeoJSONLayerView



urlpatterns = patterns('paleocore_projects.views',
                       # ex. /data/
                       url(r'^data/(?P<pcoreapp>.+)/$', views.ProjectDataView.as_view(), name='data'),
                       url(r'^data_json/(?P<pcoreapp>.+)/$', views.ajaxProjectData, name='data_json'),
                       url(r'^data_table/$', views.ProjectDataTable.as_view(), name='data_table'),
                       url(r'^detail/(?P<pk>\d+)/$', views.ProjectDetailView.as_view(), name='detail'),
                       url(r'^detail/$', views.redirectDetailViewMissingPK, name='redirect_projects_detail'),
                       url(r'^projects.geojson$', GeoJSONLayerView.as_view(model=Project, properties=("full_name")), name='projects_geojson'),
                       url(r'^$', views.ProjectIndexView.as_view(), name='index')
                       )
