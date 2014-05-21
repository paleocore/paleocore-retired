from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings


from django.conf.urls.static import static

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # App URLS
    url(r'^schema/', include('schema.urls', namespace="schema")),
    url(r'^login/', include('login.urls', namespace="user_login")),
    url(r'^polls/', include('polls.urls', namespace="polls")),  # note the lack of a terminal dollar sign in the re
    url(r'^workshops/', include('meetings.urls', namespace="meetings")),
    url(r'^data/', include('data.urls', namespace="data")),  # note the lack of a terminal dollar sign in the re

    # Admin URLS
    url(r'^admin/', include(admin.site.urls)),

    # Django Fiber URLS
    (r'^api/v2/', include('fiber.rest_api.urls')),
    (r'^admin/fiber/', include('fiber.admin_urls')),   # Does this need to be placed above the admin entry?
    (r'^jsi18n/$', 'django.views.i18n.javascript_catalog', {'packages': ('fiber',), }),
    (r'', 'fiber.views.page'),  # This catches everything not matched above!
)

"""
The following code insures that user uploaded media are properly served with the
# development server. It is NOT meant for production. This is the solution given
# in the django 1.4 documentation.
# https://docs.djangoproject.com/en/1.4/howto/static-files/
"""
#if settings.DEBUG:
#    urlpatterns = patterns('',
#        url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
#            {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
#        url(r'', include('django.contrib.staticfiles.urls')),
#    ) + urlpatterns

"""
The following code insures users uploaded media are served with the development
server. It will NOT work when settings.DEBUG = False.
Details available from the Django 1.6 documentation:
https://docs.djangoproject.com/en/1.6/howto/static-files/

IMPORTANT: One key difference between the paleocore implementation and the documentation
is that the MEDIA_URL settings are added to the beginning of the url patterns. If appened
to the end as shown in the documentation the fiber.view.page entry catches and returns 404.
"""
urlpatterns = static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + urlpatterns