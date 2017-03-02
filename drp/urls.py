from django.conf.urls import patterns, url
from drp import views as drp_views
from django.contrib.auth.decorators import login_required

urlpatterns = patterns('',
    # Project URLs are included by main urls.py


    # /projects/drp/summary/
    url(r'summary/$', drp_views.drp_summary_view, name="drp_summary"),

    # /projects/drp/upload/
    #url(r'^upload/$', login_required(mlp_views.UploadKMLView.as_view(), login_url='/login/'), name="drp_upload_kml"),

    # /projects/drp/download/
    #url(r'^download/$', drp_views.DownloadKMLView.as_view(), name="drp_download_kml"),

    # /projects/mlp/confirmation/
    #url(r'^confirmation/$', drp_views.Confirmation.as_view(), name="drp_upload_confirmation"),

    # /projects/mlp/upload/shapefile/
    # url(r'^upload/shapefile/', mlp_views.UploadShapefileView.as_view(), name="mlp_upload_shapefile"),

    # /projects/mlp/change_xy/
    #url(r'^change_xy/', drp_views.change_coordinates_view, name="drp_change_xy"),
)