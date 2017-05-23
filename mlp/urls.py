from django.conf.urls import patterns, url
from mlp import views as mlp_views
from django.contrib.auth.decorators import login_required

urlpatterns = patterns('',
    # Project URLs are included by main urls.py

    # /projects/mlp/summary/
    url(r'summary/$', mlp_views.mlp_summary_view, name="mlp_summary"),

    # /projects/mlp/upload/
    url(r'^upload/$', login_required(mlp_views.UploadKMLView.as_view(), login_url='/login/'), name="mlp_upload_kml"),

    # /projects/mlp/download/
    url(r'^download/$', mlp_views.DownloadKMLView.as_view(), name="mlp_download_kml"),

    # /projects/mlp/confirmation/
    url(r'^confirmation/$', mlp_views.Confirmation.as_view(), name="mlp_upload_confirmation"),

    # /projects/mlp/upload/shapefile/
    # url(r'^upload/shapefile/', mlp_views.UploadShapefileView.as_view(), name="mlp_upload_shapefile"),

    # /projects/mlp/change_xy/
    url(r'^change_xy/', mlp_views.change_coordinates_view, name="mlp_change_xy"),

    # /projects/mlp/occurrence2biology/
    url(r'^occurrence2biology/', mlp_views.occurrence2biology_view, name="mlp_occurrence2biology"),

)
