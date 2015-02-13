from django.conf.urls import patterns, url
from paleocore_projects import views
from paleocore_projects.models import Project
from djgeojson.views import GeoJSONLayerView



urlpatterns = patterns('paleocore_projects.views',
                       # ex. /data/
                       url(r'^$', views.IndexView.as_view(), name='index'),
                       url(r'^projects.geojson$', GeoJSONLayerView.as_view(model=Project), name='projects_data')
                       )
