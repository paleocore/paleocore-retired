from django.contrib.auth.models import User
from tastypie.authentication import ApiKeyAuthentication, Authentication
from API.custom_authorization import CustomDjangoAuthorization
from tastypie.authorization import DjangoAuthorization
from tastypie import fields
#from tastypie.contrib.gis.resources import ModelResource as geoModelResource
from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS
from turkana.models import Turkana
from drp.models import Occurrence, Biology, Hydrology, Locality



#each resource to be exposed at a particular URL in the API requires a subclass of tastypie.resources.ModelResource
#these often correspond directly to classes in models.py, but in some cases
#there are multiple resources for a particular models.py class, with different treatment of related records
#the queryset can be modified for each resource, as well as the resource name (i.e. the url in the API)
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
        authentication = Authentication()#this means no authentication, which is OK in this case, because only allowed method is GET

#####DRP API resources
#####common settings to be used for all DRP API resources
drp_authentication = ApiKeyAuthentication()#will require a username and api_key as url parameters, otherwise return 401 unauthorized
drp_authorization = CustomDjangoAuthorization(appname="drp", modelname="drp_occurrence")#look to custom Django Authorization class to determine permissions
drp_allowed_methods=['get','post']

# class drp_taxonomyResource(ModelResource):
#     class Meta:
#         max_limit=0
#         queryset = drp_taxonomy.objects.all()
#         allowed_methods= drp_allowed_methods
#         resource_name = 'drp_taxonomy'
#         authorization = drp_authorization
#         authentication = drp_authentication

class LocalityResource(ModelResource):
    class Meta:
        filtering = {
            "collectioncode": ALL,
            "paleolocalitynumber": ALL,
            "paleosublocalitynumber": ALL,
        }
        max_limit=0
        queryset = Locality.objects.all()
        allowed_methods= drp_allowed_methods
        resource_name = 'drp_locality'
        authorization = drp_authorization
        authentication = drp_authentication

class HydrologyResource(ModelResource):
    class Meta:
        max_limit=0
        queryset = Hydrology.objects.all()
        allowed_methods= drp_allowed_methods
        resource_name = 'drp_hydrology'
        authorization = drp_authorization
        authentication = drp_authentication

####DRP Biology API resources
drp_biology_filtering = {
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
drp_biology_excludes = ["lrp3","lrp4","llc","lli1","lli2","lli3","lli4","lli5","llm1","llm2","llm3","llp1","llp2","llp3","llp4","lrc","lri1","lri2","lri3","lri4","lri5","lrm1","lrm2","lrm3","lrp1","lrp2","lrp","ulp1","ulp2","ulp3","ulp4","urc","uri1","uri2","uri3","uri4","uri5","urm1","urm2","urm3","urp1","urp2","urp3","urp4","ulc","uli1","uli2","uli3","uli4","uli5","ulm1","ulm2","ulm3"]

class BiologyResource(ModelResource):
    #occurrence = fields.ToOneField("API.API_resources.drp_occurrenceResource", attribute="occurrence") #foreign key to occurrence
    class Meta:
        queryset = Biology.objects.all()
        max_limit=0
        allowed_methods=drp_allowed_methods
        resource_name = 'drp_biology'
        filtering = drp_biology_filtering
        excludes = drp_biology_excludes
        authorization = drp_authorization
        authentication = drp_authentication

class BiologyFullRelatedResource(ModelResource):
    occurrence = fields.ToOneField("API.API_resources.drp_occurrenceResource", attribute="occurrence", full=True) #foreign key to occurrence
    class Meta:
        queryset = Biology.objects.all()
        max_limit=0
        allowed_methods=drp_allowed_methods
        resource_name = 'drp_biology_full_related'
        filtering = drp_biology_filtering
        excludes = drp_biology_excludes


###drp_occurrence resources
drp_occurrence_filtering = {
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

class OccurrenceResource(ModelResource):
    #biology = fields.ToOneField("API.API_resources.drp_biologyResource", attribute="drp_biology", null=True, blank=True) #link for the reverse lookup of biology
    class Meta:
        max_limit=0
        queryset = Occurrence.objects.all()
        allowed_methods=drp_allowed_methods
        resource_name = 'drp_occurrence'
        filtering = drp_occurrence_filtering
        authorization = drp_authorization
        authentication = drp_authentication

class OccurrenceFullRelatedResource(ModelResource):
    biology = fields.ToOneField("API.API_resources.drp_biologyResource", attribute="Biology", full=True, null=True, blank=True) #link for the reverse lookup of biology
    class Meta:
        max_limit=0
        queryset = Occurrence.objects.all()
        allowed_methods=drp_allowed_methods
        resource_name = 'drp_occurrence_full_related'
        filtering = drp_occurrence_filtering
        authorization = drp_authorization
        authentication = drp_authentication