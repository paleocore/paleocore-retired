from django.conf.urls import patterns, url
from san_francisco import views as san_francisco_views


urlpatterns = patterns('',

    # e.g. /san_francisco/upload/
    url(r'^upload/$', san_francisco_views.UploadKMLView.as_view(), name="san_francisco_upload_kml"),
    url(r'^download/$', san_francisco_views.DownloadKMLView.as_view(), name="san_francisco_download_kml"),
    url(r'^confirmation/$', san_francisco_views.Confirmation.as_view(), name="san_francisco_upload_confirmation"),
    url(r'^upload/shapefile/', san_francisco_views.UploadView.as_view(), name="san_francisco_upload"),
    url(r'^change_xy/', san_francisco_views.ChangeXYView, name="change_xy"),

)
