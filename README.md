paleocore
=========

## This is the codebase for the paleocore project.

### Note regarding settings.py:

This project does not store sensitive information (such as passwords etc) in settings.py as this is clearly not secure.  Instead, there is a file called secrets.py that is ignored by git (because it is listed in the .gitignore file) in which these sensitive data are stored.  settings.py imports these variables from secrets.py, and thus these data are only stored locally, rather than being made public on github. 

Django==1.6.2  
M2Crypto==0.20.2  
Pillow==2.4.0  
SSSDConfig==1.9.2  
South==0.7.6  
distribute==0.6.10  
django-appconf==0.6  
django-classy-tags==0.5  
django-compressor==1.3  
django-fiber==0.13  
django-guardian==1.2.0  
django-mptt==0.6.0  
django-sekizai==0.6.1  
django-tastypie==0.11.1  
djangorestframework==2.3.13  
easy-thumbnails==1.4  
ethtool==0.6  
html5lib==1.0b3  
iniparse==0.3.1  
iwlib==1.0  
pciutils==1.7.3  
psycopg2==2.5.2  
pyOpenSSL==0.10  
pycurl==7.19.0  
pygpgme==0.1  
python-dateutil==2.2  
python-dmidecode==3.10.13  
python-mimeparse==0.1.4  
qpid-python==0.14  
qpid-tools==0.14  
rhnlib==2.5.51  
simplejson==3.4.0  
six==1.6.1  
unicodecsv==0.9.4  
urlgrabber==3.9.1  
vectorformats==0.1  
yum-metadata-parser==1.1.2  
