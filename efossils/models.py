from django.db import models

# Create your models here.
class Site(models.Model):
    name = models.CharField("Name #", max_length=255, blank=False, null=False)
