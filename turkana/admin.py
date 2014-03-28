from django.contrib.gis import admin

from paleocore.turkana.models import turkana


turkana_adminsite = admin.AdminSite("turkana_adminsite")
turkana_adminsite.register(turkana)
