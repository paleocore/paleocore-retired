from django.conf.urls import patterns, url
from data import views
from tastypie.models import ApiKey
from API.views import get_or_create_API_key


urlpatterns = patterns('',
                       url(r'$^', get_or_create_API_key , name='get_or_create_API_key'),
                       )
