from django.conf.urls import patterns, url
from data import views


urlpatterns = patterns('data.views',
                       # /data/
                       url(r'^$', views.IndexView.as_view(), name='index'),
                       # /data/turkana
                       url(r'^(?P<project_name>\w+)/$', 'project_data_display'),

                       )
