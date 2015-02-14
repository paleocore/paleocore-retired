from django.conf.urls import patterns, url
from paleocore_projects import views
from paleocore_projects.models import Project
from djgeojson.views import GeoJSONLayerView



urlpatterns = patterns('paleocore_projects.views',
                       # ex. /data/
                       url(r'^detail/(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
                       url(r'^detail/$', views.redirectDetailViewMissingPK, name='redirect_projects_detail'),
                       url(r'^projects.geojson$', GeoJSONLayerView.as_view(model=Project, properties=("full_name")), name='projects_geojson'),
                       url(r'^$', views.IndexView.as_view(), name='index')
                       )
