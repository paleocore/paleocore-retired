import os
import sys

sys.path.append('/usr/local/django')
sys.path.append('/usr/local/django/paleocore')
sys.path.append('/usr/local/django/paleocore/mysite')

os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()