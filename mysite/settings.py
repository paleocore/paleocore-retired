"""
Django settings for mysite project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""
# Import sensitive data from separate file not on GitHub
from . import secrets

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

gettext = lambda s: s
PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
#MEDIA_ROOT = os.path.join(BASE_DIR, '../paleocore_media')
MEDIA_ROOT = secrets.MEDIA_ROOT

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = "/media/"

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = secrets.SECRET_KEY

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = secrets.DEBUG_MODE
TEMPLATE_DEBUG = secrets.TEMPLATE_DEBUG_MODE

ALLOWED_HOSTS = [secrets.ALLOWED_HOSTS]

POSTGIS_VERSION = (2, 0, 1)

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',  # enables django admin
    'django.contrib.auth',  # enable django authentication module
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.gis',  # enables geodjango
    'debug_toolbar',

    # Django Fiber Apps
    'mptt',
    'compressor',
    'easy_thumbnails',
    'fiber',

    # PaleoCore Apps
    'API',  # so that testing works
    'tastypie',  # to create database tables for API keys when syncdb is run
    'login',  # simple app for validating users in views
    'base',  # main site app
    'standard',  # paleocore standard
    'efossils',
    'paleosites',
    'olwidget',

    # Project Apps
    'mlp',  # Mille-Logya Project
    'drp',  # Dikika Research Project
    'hrp',  # Hadar Research Project
    'lgrp', # Ledi-Geraru Research Project
    'turkana',  # Turkana Project Data
    'cc',  # Combe Capelle project
    'fc',  # Fontechevade project
    'gdb',  # Great Divide Basin project
    'west_turkana',  # West Turkana research project
    'san_francisco',  # San Francisco demo project
    'omo_mursi',
    'projects',
    'taxonomy',
    'leaflet',
    'djgeojson',
    'django.contrib.humanize',
)

# These entries extended by entries BELOW in Django Fiber section
MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'mysite.urls'

WSGI_APPLICATION = 'mysite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',   # Postgres PostGIS spatial database backend
        #'ENGINE': 'django.contrib.gis.db.backends.spatialite',
        'PORT': secrets.DATABASE_PORT,  # 5432 default Postgres port
        #'NAME': 'C:\\Users\\turban\\Documents\\Development\\PyCharm\\paleocore\\paleocore.db',
        'NAME': secrets.DATABASE_NAME,  # 'paleocore_dev',
        'USER': secrets.DATABASE_USER,   # 'webdev' is the user for the local development server
        'PASSWORD': secrets.DATABASE_PASSWORD,   # password for local postgres server
        'HOST': secrets.DATABASE_HOST,   # for local development server
    },

    # 'drp_carmen': {
    #     'ENGINE': 'django.contrib.gis.db.backends.postgis',  # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
    #     'NAME': 'drp_dev',
    #     'USER': secrets.DRP_USER,                      # Not used with sqlite3.
    #     'PASSWORD': secrets.DRP_PASSWORD,                  # Not used with sqlite3.
    #     'HOST': secrets.DRP_HOST,                      # Set to empty string for localhost. Not used with sqlite3.
    #     'PORT': '5432',                      # Set to empty string for default. Not used with sqlite3.
    # }
}

# Points to the location of the database router configuration file
#DATABASE_ROUTERS = ['database_routers.paleocore_router.PaleocoreRouter']

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/Chicago'

USE_I18N = True

USE_L10N = True

USE_TZ = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/
STATIC_URL = '/static/'  # See also STATIC_ROOT entry in Django Fiber section
TEMPLATE_DIRS = [os.path.join(BASE_DIR, 'templates')]


# Path and URL for user uploaded media files



###########################
## Django Fiber Settings ##
###########################
import django.conf.global_settings as DEFAULT_SETTINGS

# Overides Middleware Classes defined above
MIDDLEWARE_CLASSES = DEFAULT_SETTINGS.MIDDLEWARE_CLASSES + (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'fiber.middleware.ObfuscateEmailAddressMiddleware',
    'fiber.middleware.AdminPageMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = DEFAULT_SETTINGS.TEMPLATE_CONTEXT_PROCESSORS + (
    'django.core.context_processors.request',
)

# Overrides default Fiber permissions class to prevent all staff users
# from gaining access to CMS
PERMISSION_CLASS='mysite.fiberPermissions.FiberPermissions'

"""
Added to appropriate section above
INSTALLED_APPS = (
    ...
    'django.contrib.staticfiles',
    'mptt',
    'compressor',
    'easy_thumbnails',
    'fiber',
    ...
)
"""

# import os  # Already imported above
# BASE_DIR = os.path.abspath(os.path.dirname(__file__)) # Already defined above

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
# STATIC_URL = '/static/' # Already defined above
STATICFILES_FINDERS = DEFAULT_SETTINGS.STATICFILES_FINDERS + (
    'compressor.finders.CompressorFinder',
)

