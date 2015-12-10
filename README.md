paleocore
=========

## This is the codebase for the paleocore project.

### Note regarding settings.py:
Local settings are stored in mysite/secrets.py. This file is not included in the GitHub repository for security 
reasons and must be created during installation. A template for secrets.py is provided at mysite/secrets_template.py. 
Add your local configuration settings and rename the file secrets.py. 

### Python Environment 
Django==1.8.4
Pillow==3.0.0
Shapely==1.5.12
django-appconf==1.0.1
django-compressor==1.5
django-countries==3.3
django-fiber==1.2
django-geojson==2.8.1
django-leaflet==0.16.0
django-mptt==0.7.4
django-olwidget==0.61.0
django-tastypie==0.12.2
djangorestframework==2.4.8
easy-thumbnails==2.2
fastkml==0.11
lxml==3.4.4
psycopg2==2.6.1
pygeoif==0.6
pyshp==1.2.3
python-dateutil==2.4.2
python-mimeparse==0.1.4
six==1.9.0
unicodecsv==0.14.1
utm==0.4.0
wsgiref==0.1.2


#### Installation Notes
olwidget does not function correctly under Django 1.8 and requires manually patching the source files as described in the following two links.
https://github.com/bretwalker/olwidget/commit/f1fc2dec07abc905440e42516957d2f46122844e
https://github.com/Christophe31/olwidget/commit/4fbd91a3354f889749ef09ede8e330330476c0fe



