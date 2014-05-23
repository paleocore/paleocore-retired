from django.contrib.auth.models import User
from tastypie.authentication import Authentication
from tastypie import fields
from tastypie.contrib.gis.resources import ModelResource as geoModelResource
from tastypie.resources import ModelResource, ALL
from turkana.models import Turkana
from drp.models import drp_taxonomy
from serializers import CSVSerializer


class userResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        resource_name = 'user'
        excludes = ['email', 'password', 'is_active', 'is_staff', 'is_superuser']
        filtering = {
            'username': ALL,
        }

class turkanaResource(ModelResource):
    class Meta:
        queryset = Turkana.objects.all()
        allowed_methods=['get']
        resource_name = 'turkana'
        filtering = {
            'genus':['exact'],
            'year_found': ALL,
            'collecting_area' : ['exact'],

        }
        serializer = CSVSerializer()
        authentication = Authentication()

class drp_taxonomyResource(ModelResource):
    class Meta:
        queryset = drp_taxonomy.objects.all()
        allowed_methods=['get']
        resource_name = 'drp_taxonomy'
