from django.conf.urls import patterns, url


urlpatterns = patterns('',
    # e.g. /paleosites/
    url(r'^$', 'paleosites.views.home', name='home'),
    # e.g. /paleosites/index/
    url(r'^index', 'paleosites.views.home', name='home'),
    # e.g. /paleosites/kml/
    url(r'^kml/', 'paleosites.views.all_kml', name='all_kml'),
    # e.g. /paleosites/map/
    url(r'^map/', 'paleosites.views.map_page', name='map_page'),
)
