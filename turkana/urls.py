from django.conf.urls import patterns, url, include
from turkana.views import *


urlpatterns = patterns('',
    url(r'^$',turkana_home),
    )