from django.conf.urls import patterns, url
from lgrp import views as lgrp_views
from django.contrib.auth.decorators import login_required

urlpatterns = patterns('',
    # Project URLs are included by main urls.py

    # /projects/lgrp/upload/
    url(r'^upload/$', login_required(lgrp_views.UploadKMLView.as_view(), login_url='/login/'), name="lgrp_upload_kml"),

    # /projects/lgrp/download/
    url(r'^download/$', lgrp_views.DownloadKMLView.as_view(), name="lgrp_download_kml"),

    # /projects/lgrp/confirmation/
    url(r'^confirmation/$', lgrp_views.Confirmation.as_view(), name="lgrp_upload_confirmation"),

    # /projects/lgrp/upload/shapefile/
    # url(r'^upload/shapefile/', lgrp_views.UploadShapefileView.as_view(), name="lgrp_upload_shapefile"),

    # /projects/lgrp/change_xy/
    url(r'^change_xy/', lgrp_views.change_coordinates_view, name="lgrp_change_xy"),

)