from django.conf.urls import patterns, url
from mlp import views as mlp_views


urlpatterns = patterns('',
    # Project URLs are included by main urls.py

    # /projects/mlp/upload/
    url(r'^upload/$', mlp_views.UploadKMLView.as_view(), name="mlp_upload_kml"),

    # /projects/mlp/download/
    url(r'^download/$', mlp_views.DownloadKMLView.as_view(), name="mlp_download_kml"),

    # /projects/mlp/confirmation/
    url(r'^confirmation/$', mlp_views.Confirmation.as_view(), name="mlp_upload_confirmation"),

    # /projects/mlp/upload/shapefile/
    url(r'^upload/shapefile/', mlp_views.UploadShapefileView.as_view(), name="mlp_upload_shapefile"),

    # /projects/mlp/change_xy/
    url(r'^change_xy/', mlp_views.ChangeXYView, name="mlp_change_xy"),

)
