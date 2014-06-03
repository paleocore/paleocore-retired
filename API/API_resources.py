from django.contrib.auth.models import User
from tastypie.authentication import Authentication, ApiKeyAuthentication
from tastypie import fields
from tastypie.contrib.gis.resources import ModelResource as geoModelResource
from tastypie.resources import ModelResource, ALL
from turkana.models import Turkana
from drp.models import drp_taxonomy, drp_occurrence, drp_biology
from serializers import CSVSerializer



#each resource to be exposed at a particular URL in the API requires a subclass of tastypie.resources.ModelResource
#these often correspond directly to classes in models.py
#the queryset can be modified, as well as the resource name (i.e. the url in the API)
#as well as which fields can be filtered on, etc
#these classes are registered to the API in the main urls.py


class turkanaResource(ModelResource):
    class Meta:
        queryset = Turkana.objects.all()
        allowed_methods=['get']
        resource_name = 'turkana'
        filtering = {
            'genus': ALL,
            'specimen_number':ALL,
            'year_found': ALL,
            'collecting_area' : ALL,
            'study_area' : ALL,
            'locality' : ALL,
            'formation' : ALL,
            'member' : ALL,
            'level' : ALL,
            'stratigraphic_unit' : ALL,
            'excavation' : ALL,
            'square_number' : ALL,
            'age_estimate' : ALL,
            'age_max' : ALL,
            'age_min' : ALL,
            'stratigraphic_code' : ALL,
            'matrix' : ALL,
            'weathering' : ALL,
            'surface' : ALL,
            'color' : ALL,
            'identifier' : ALL,
            'year_identified' : ALL,
            'publication_author' : ALL,
            'year_published' : ALL,
            'year_published_suffix' : ALL,
            'class_field' : ALL,
            'order' : ALL,
            'family' : ALL,
            'family_code' : ALL,
            'subfamily' : ALL,
            'tribe' : ALL,
            'tribe_code' : ALL,
            'genus_qualifier' : ALL,
            'genus' : ALL,
            'genus_code' : ALL,
            'species_qualifier' : ALL,
            'species' : ALL,
            'body_element' : ALL,
            'body_element_code' : ALL,
            'part_description' : ALL,
            'side' : ALL,
            'sex' : ALL,
            'age' : ALL,
            'remarks' : ALL,
            'date_entered' : ALL,
            'signed' : ALL,
            'storage_location' : ALL,
            'body_size' : ALL,

        }
        max_limit=0
        serializer = CSVSerializer()
        authentication = Authentication()#this means no authentication, which is OK in this case

class drp_taxonomyResource(ModelResource):
    class Meta:
        queryset = drp_taxonomy.objects.all()
        allowed_methods=['get']
        resource_name = 'drp_taxonomy'
        serializer = CSVSerializer()
        authentication = ApiKeyAuthentication()

class drp_biologyResource(ModelResource):
    occurrence = fields.ToOneField("API.API_resources.drp_occurrenceResource", attribute="occurrence")
    class Meta:
        queryset = drp_biology.objects.all()
        allowed_methods=['get']
        resource_name = 'drp_biology'
        serializer = CSVSerializer()
        authentication = ApiKeyAuthentication()

class drp_occurrenceResource(ModelResource):
    biology = fields.ToOneField("API.API_resources.drp_biologyResource", attribute="drp_biology", full=True)
    class Meta:
        queryset = drp_occurrence.objects.all()
        allowed_methods=['get']
        resource_name = 'drp_occurrence'
        filtering = {
            "barcode": ALL,
        }
        serializer = CSVSerializer()
        authentication = ApiKeyAuthentication()
