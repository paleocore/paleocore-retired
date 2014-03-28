from django.conf.urls import patterns, url
from data import views


urlpatterns = patterns('',
                       # /data/
                       url(r'^$', views.IndexView.as_view(), name='index'),
                       # /data/turkana
                       url(r'^turkana/$', views.TurkanaIndexView.as_view(), name='turkana'),

                       )

