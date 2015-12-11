from django.conf.urls import patterns, url
from san_francisco import views as san_francisco_views


urlpatterns = patterns('',
    ## Project URLs are included by main urls.py

    # /projects/san_francisco/upload/
    url(r'^upload/$', san_francisco_views.UploadKMLView.as_view(), name="san_francisco_upload_kml"),

    # /projects/san_francisco/download/
    url(r'^download/$', san_francisco_views.DownloadKMLView.as_view(), name="san_francisco_download_kml"),

    # /projects/san_francisco/confirmation/
    url(r'^confirmation/$', san_francisco_views.Confirmation.as_view(), name="san_francisco_upload_confirmation"),

    # /projects/san_francisco/upload/shapefile/
    url(r'^upload/shapefile/', san_francisco_views.UploadKMLView.as_view(), name="san_francisco_upload"),

    # /projects/san_francisco/change_xy/
    url(r'^change_xy/', san_francisco_views.change_coordinates_view, name="change_xy"),

)
