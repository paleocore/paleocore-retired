from django.conf.urls import patterns, url
from data import views
from schema import views as schema_views


urlpatterns = patterns('data.views',
                       # ex. /data/
                       url(r'^$', views.IndexView.as_view(), name='index'),

                       #/data/drp -- passes through to fiber

                       # ex /data/drp/terms/
                       url(r'^(?P<project_name>\w+)/terms/$', schema_views.TermsIndexView.as_view(), name='terms_index'),

                       # ex. /data/search/turkana
                       #url(r'^search/(?P<project_name>\w+)/$', 'project_data_display'),
                       )
