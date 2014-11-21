paleocore
=========

## This is the codebase for the paleocore project.

### Note regarding settings.py:

This project does not store sensitive information (such as passwords etc) in settings.py as this is clearly not secure.  Instead, there is a file called secrets.py that is ignored by git (because it is listed in the .gitignore file) in which these sensitive data are stored.  settings.py imports these variables from secrets.py, and thus these data are only stored locally, rather than being made public on github. 

Django==1.6.2  
  
Django_Fiber==0.13 installs the following dependencies  
    Pillow==2.2.1  
    django-appconf==0.6  
    django-compressor==1.3  
    django-mptt==0.6.0  
    djangorestframework==2.3.8  
    easy-thumbnails==1.4  
   
unicodecsv==0.9.4  
simplejson==3.4.1  
django-tastypie==0.11.1  
pyshp==1.2.1  
  
fastkml==0.9  depends on:  
    pygeoif==0.1.4  
    dateutil==2.2  
      
lxml==3.4.0  
utm==0.3.1  
Shapely==1.4.3  
