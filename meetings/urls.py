from django.conf.urls import patterns, url
from meetings import views

urlpatterns = patterns('',
                       url(r'^(?P<meeting_name>\w+)/abstracts/$', views.IndexView.as_view(), name='index'),
                       )

