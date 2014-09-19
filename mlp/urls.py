from django.conf.urls import patterns, url
from mlp import views as mlp_views
from mlp import views


urlpatterns = patterns('',
    url(r'^upload/', mlp_views.UploadView.as_view(), name="mlp_upload"),
)
