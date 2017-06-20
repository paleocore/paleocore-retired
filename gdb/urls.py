from django.conf.urls import patterns, url
from gdb import views as gdb_views
from django.contrib.auth.decorators import login_required

urlpatterns = patterns('',
   # /projects/gdb/upload/
   url(r'^upload/$', login_required(gdb_views.UploadKMLView.as_view(), login_url='/login/'),
       name="gdb_upload_kml"),

   # /projects/gdb/confirmation/
   url(r'^confirmation/$', gdb_views.Confirmation.as_view(), name="gdb_upload_confirmation"),


)
