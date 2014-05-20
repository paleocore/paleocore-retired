from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url('','login.views.user_login', name="user_login"),


)


