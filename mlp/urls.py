from django.conf.urls import patterns, url
from mlp import views as mlp_views
from mlp import views


urlpatterns = patterns('',
    # e.g. /mlp/upload/kml/
    url(r'^upload/kml/$', mlp_views.UploadKMLView.as_view(), name="mlp_upload_kml"),

    # e.g. /mlp/upload/
    url(r'^upload/', mlp_views.UploadView.as_view(), name="mlp_upload"),

)
