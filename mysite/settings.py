"""
Django settings for mysite project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

gettext = lambda s: s
PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = os.path.join(PROJECT_PATH, "media")

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = "/media/"

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '0!vdm@wj&wl$i@)9+m40+xw642v^l1y_&fhfh9)ri!r0bjw=)a'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',

    # Django Fiber Apps
    'django.contrib.staticfiles',
    'mptt',
    'compressor',
    'easy_thumbnails',
    'fiber',
    #'pages',

    # Project Apps
    'base',
    'polls',
)

# These entries extended by entries below in Django Fiber section
MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'mysite.urls'

WSGI_APPLICATION = 'mysite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',   # Postgres PostGIS spatial database backend
        'NAME': 'paleocore_dev',
        'USER': 'webdev',   # 'webdev' is the user for the local development server
        'PASSWORD': 'password',   # password for local postgres server
        #'HOST': 'paleocore-qa.tacc.utexas.edu',   # hostname for TACC development server
        'HOST': 'localhost',   # for local development server
        'PORT': '5432',   # default Postgres port
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/
STATIC_URL = '/static/'  # See also STATIC_ROOT entry in Django Fiber section
TEMPLATE_DIRS = [os.path.join(BASE_DIR, 'templates')]

# Path and URL for user uploaded media files
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

###########################
## Django Fiber Settings ##
###########################
import django.conf.global_settings as DEFAULT_SETTINGS

# Overides Middleware Classes defined above
MIDDLEWARE_CLASSES = DEFAULT_SETTINGS.MIDDLEWARE_CLASSES + (
    'fiber.middleware.ObfuscateEmailAddressMiddleware',
    'fiber.middleware.AdminPageMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = DEFAULT_SETTINGS.TEMPLATE_CONTEXT_PROCESSORS + (
    'django.core.context_processors.request',
)


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

