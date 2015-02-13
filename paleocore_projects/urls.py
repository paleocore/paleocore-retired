from django.conf.urls import patterns, url
from paleocore_projects import views




urlpatterns = patterns('paleocore_projects.views',
                       # ex. /data/
                       url(r'^$', views.IndexView.as_view(), name='index'),

                       )
