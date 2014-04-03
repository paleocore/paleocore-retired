import os
import sys

sys.path.append('/usr/local/django')
sys.path.append('/usr/local/django/paleocore')
sys.path.append('/usr/local/django/paleocore/mysite')

os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()