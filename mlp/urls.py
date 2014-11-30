from django.conf.urls import patterns, url
from mlp import views as mlp_views


urlpatterns = patterns('',

    # e.g. /mlp/upload/
    url(r'^upload/$', mlp_views.UploadKMLView.as_view(), name="mlp_upload_kml"),
    url(r'^download/$', mlp_views.DownloadKMLView.as_view(), name="mlp_download_kml"),

    # /mlp/confirmation
    url(r'^confirmation/$', mlp_views.Confirmation.as_view(), name="upload_confirmation"),

    # e.g. /mlp/upload/
    url(r'^upload/shapefile/', mlp_views.UploadView.as_view(), name="mlp_upload"),
    url(r'^change_xy/', mlp_views.ChangeXYView, name="change_xy"),

)
