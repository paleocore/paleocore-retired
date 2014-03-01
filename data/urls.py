from django.conf.urls import patterns, url
from data import views

urlpatterns = patterns('',
                       url(r'^$', views.IndexView.as_view(), name='index'),
                       )

