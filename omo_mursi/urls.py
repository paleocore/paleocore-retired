from django.conf.urls import patterns, url
from . import views as omo_mursi_views


urlpatterns = patterns('',
    # Project URLs are included by main urls.py

    # /projects/omo_mursi/upload/
    url(r'^upload/$', omo_mursi_views.UploadKMLView.as_view(), name="omo_mursi_upload_kml"),

    # /projects/omo_mursi/download/
    url(r'^download/$', omo_mursi_views.DownloadKMLView.as_view(), name="omo_mursi_download_kml"),

    # /projects/omo_mursi/confirmation/
    url(r'^confirmation/$', omo_mursi_views.Confirmation.as_view(), name="omo_mursi_upload_confirmation"),

    # /projects/omo_mursi/upload/shapefile/
    url(r'^upload/shapefile/', omo_mursi_views.UploadShapefileView.as_view(), name="omo_mursi_upload_shapefile"),

    # /projects/omo_mursi/change_xy/
    url(r'^change_xy/', omo_mursi_views.change_coordinates_view, name="omo_mursi_change_xy"),

)
