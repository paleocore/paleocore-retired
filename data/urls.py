from django.conf.urls import patterns, url
from data import views


urlpatterns = patterns('data.views',
                       # ex. /data/
                       url(r'^$', views.IndexView.as_view(), name='index'),
                       #/data/drp -- passes through to fibder
                       # ex. /data/search/turkana
                       #url(r'^search/(?P<project_name>\w+)/$', 'project_data_display'),
                       )
