from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # App URLS
    url(r'^polls/', include('polls.urls', namespace="polls")),  # note the lack of a terminal dollar sign in the re

    # Admin URLS
    url(r'^admin/', include(admin.site.urls)),

    # Django Fiber URLS
    (r'^api/v2/', include('fiber.rest_api.urls')),
    (r'^admin/fiber/', include('fiber.admin_urls')),   # Does this need to be placed above the admin entry?
    (r'^jsi18n/$', 'django.views.i18n.javascript_catalog', {'packages': ('fiber',), }),
    (r'', 'fiber.views.page'),
)
