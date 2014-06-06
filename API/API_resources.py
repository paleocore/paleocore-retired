from django.contrib.auth.models import User
from tastypie.authentication import Authentication, ApiKeyAuthentication
from tastypie import fields
#from tastypie.contrib.gis.resources import ModelResource as geoModelResource
from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS
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
        #dictionary of fields to allow filtering on, including which filter types are allowed. ALL is a shortcut to allow all filter types for a field
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
        serializer = CSVSerializer() #custom csv serializer in serializers.py
        authentication = ApiKeyAuthentication()#will require a username and api_key as url parameters, otherwise return 401 unauthorized

class drp_biologyResource(ModelResource):
    occurrence = fields.ToOneField("API.API_resources.drp_occurrenceResource", attribute="occurrence") #foreign key to occurrence
    class Meta:
        queryset = drp_biology.objects.all()
        allowed_methods=['get']
        resource_name = 'drp_biology'
        filtering = {
            "barcode": ALL,
            "tax_class": ALL,
            "tax_order": ALL,
            "family": ALL,
            "tribe": ALL,
            "genus": ALL,
            "specificepithet": ALL,
            "infraspecificepithet": ALL,
            "infraspecificrank": ALL,
            "identifiedby": ALL,
            "identificationqualifier": ALL,
            "sex": ALL,
            "lifestage": ALL,
            "side": ALL,
            "faunanotes": ALL,
            "toothupperorlower": ALL,
            "toothnumber": ALL,
            "toothtype": ALL,
        }
        serializer = CSVSerializer()
        authentication = ApiKeyAuthentication()

class drp_occurrenceResource(ModelResource):
    biology = fields.ToOneField("API.API_resources.drp_biologyResource", attribute="drp_biology", full=True, null=True) #link for the reverse lookup of biology
    class Meta:
        queryset = drp_occurrence.objects.all()
        allowed_methods=['get']
        resource_name = 'drp_occurrence'
        filtering = {
            "biology": ALL_WITH_RELATIONS, #allows you to filter on biology fields from occurrence API resource
            "barcode": ALL,
            "basisofrecord": ALL,
            "itemtype": ALL,
            "institutionalcode": ALL,
            "collectioncode": ALL,
            "paleolocalitynumber": ALL,
            "paleosublocality": ALL,
            "itemnumber": ALL,
            "itempart": ALL,
            "catalognumber": ALL,
            "remarks": ALL,
            "itemscientificname": ALL,
            "itemdescription": ALL,
            "continent": ALL,
            "country": ALL,
            "stateprovince": ALL,
            "locality": ALL,
            "collectingmethod": ALL,
            "relatedcatalogitems": ALL,
            "fieldnumber": ALL,
            "yearcollected": ALL,
            "individualcount": ALL,
            "strat_upper": ALL,
            "distancefromupper": ALL,
            "strat_lower": ALL,
            "distancefromlower": ALL,
            "strat_found": ALL,
            "distancefromfound": ALL,
            "strat_likely": ALL,
            "distancefromlikely": ALL,
            "stratigraphicmember": ALL,
            "analyticalunit": ALL,
            "analyticalunit2": ALL,
            "analyticalunit3": ALL,
            "insitu": ALL,
            "weathering": ALL,
            "surfacemodification": ALL,
            "problem": ALL,
            "problemcomment": ALL,
            "geom": ALL,
        }
        serializer = CSVSerializer()
        authentication = ApiKeyAuthentication()
