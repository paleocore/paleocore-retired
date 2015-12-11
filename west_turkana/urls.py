from django.conf.urls import patterns, url
import views as west_turkana_views


urlpatterns = patterns('',
    # Project URLs are included by main urls.py

    # /projects/west_turkana/upload/
    url(r'^upload/$', west_turkana_views.UploadKMLView.as_view(), name="west_turkana_upload_kml"),

    # /projects/west_turkana/download/
    url(r'^download/$', west_turkana_views.DownloadKMLView.as_view(), name="west_turkana_download_kml"),

    # /projects/west_turkana/confirmation/
    url(r'^confirmation/$', west_turkana_views.Confirmation.as_view(), name="west_turkana_upload_confirmation"),

    # /projects/west_turkana/upload/shapefile/
    url(r'^upload/shapefile/', west_turkana_views.UploadShapefileView.as_view(), name="west_turkana_upload_shapefile"),

    # /projects/west_turkana/change_xy/
    url(r'^change_xy/', west_turkana_views.change_coordinates_view, name="west_turkana_change_xy"),

)
