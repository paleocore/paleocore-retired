from django.conf.urls import patterns, url, include
from paleocore.turkana.views import *
from paleocore.turkana.admin import turkana_adminsite

urlpatterns = patterns('',
    url(r'^admin/',include(turkana_adminsite.urls)),
    url(r'^$',turkana_home),
    )