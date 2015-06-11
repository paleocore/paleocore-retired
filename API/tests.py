from tastypie.test import ResourceTestCase
from django.contrib.auth.models import User
from django.contrib.gis.geos import Point, Polygon
from turkana.models import Turkana
from drp.models import Occurrence, Biology, Locality
from taxonomy.models import Taxon, IdentificationQualifier
from tastypie.models import ApiKey
from django.contrib.auth.models import Permission
from datetime import datetime


class DRPResourceTest(ResourceTestCase):
    fixtures = ['fixtures/fiber_data_150611.json', 'taxonomy/fixtures/taxonomy_data_150611.json']

    def setUp(self):
        super(DRPResourceTest, self).setUp()

        # Create a user.
        self.username = 'youzer'
        self.password = 'pass'
        self.user = User.objects.create_user(self.username, 'youzer@example.com', self.password)
        ApiKey.objects.create(user=self.user)
        self.apikey = ApiKey.objects.get(user=self.user).key

        # Create a DRP Locality
        starting_record_count = Locality.objects.count()  # get current record count
        poly = Polygon(
            ((41.2, 11.2), (41.4, 11.2), (41.4, 11.0), (41.2, 11.0), (41.2, 11.2))
        )
        Locality.objects.create(paleolocality_number=1, geom=poly)
        self.assertEqual(Locality.objects.count(), starting_record_count+1)

        # Create a DRP Occurrence instance
        occurrence_starting_record_count = Occurrence.objects.count()
        Occurrence.objects.create(basis_of_record="FossilSpecimen",
                                  item_type="Faunal",
                                  barcode=1,
                                  collection_code="DIK",
                                  paleolocality_number="1",
                                  item_number="1",
                                  geom=Point(41.3, 11.1),
                                  locality=Locality.objects.get(paleolocality_number=1),
                                  field_number=datetime.now())

        # Create a DRP Biology instance
        biology_starting_record_count = Biology.objects.count()
        Biology.objects.create(
            barcode=2,
            basis_of_record="HumanObservation",
            collection_code="DIK",
            paleolocality_number="1",
            item_number="2",
            geom=Point(41.31, 11.11),
            locality=Locality.objects.get(paleolocality_number=1),
            taxon=Taxon.objects.get(name__exact="Primates"),
            identification_qualifier=IdentificationQualifier.objects.get(name__exact="None"),
            field_number=datetime.now()
        )

        self.assertEqual(Occurrence.objects.count(), occurrence_starting_record_count+2)
        self.assertEqual(Biology.objects.count(), biology_starting_record_count+1)
        self.testObject = Occurrence.objects.get(catalog_number="DIK-1-1")

    def get_basic_credentials(self):
        return self.create_basic(username=self.username, password=self.password)

    def test_unauthenticated(self):
        self.assertHttpUnauthorized(self.api_client.get("/API/v1/drp/Occurrence/?format='json'"))
        self.assertHttpUnauthorized(self.api_client.get("/API/v1/Biology/?format='json'"))
        self.assertHttpUnauthorized(self.api_client.get("/API/v1/drp_taxonomy/?format='json'"))

    def test_unauthorizedGET(self):
        self.assertHttpUnauthorized(self.api_client.get("/API/v1/Occurrence/?format=json&username={user}&api_key={api}".format(user=self.username, api=self.apikey)))
        self.assertHttpUnauthorized(self.api_client.get("/API/v1/drp_taxonomy/?format=json&username={user}&api_key={api}".format(user=self.username, api=self.apikey)))
        self.assertHttpUnauthorized(self.api_client.get("/API/v1/Biology/?format=json&username={user}&api_key={api}".format(user=self.username, api=self.apikey)))

    ##need test for authenticated user that lacks post permissions
    def test_unauthorizedPOST(self):
        self.assertHttpUnauthorized(self.api_client.post("/API/v1/Occurrence/?format=json&username={user}&api_key={api}".format(user=self.username, api=self.apikey), data={"geom":"POINT (1 1)"}))
        self.assertHttpUnauthorized(self.api_client.post("/API/v1/drp_taxonomy/?format=json&username={user}&api_key={api}".format(user=self.username, api=self.apikey), data={"family":"Fungus", "taxon":"fungus","rank":"family", "hierarchysortorder":1}))
        #can't test biology, because there is no occurrence yet

    def test_authorizedPOST(self):
        self.user.user_permissions.add(Permission.objects.get(codename="add_Occurrence"))
        self.user.user_permissions.add(Permission.objects.get(codename="add_drp_taxonomy"))
        self.user.user_permissions.add(Permission.objects.get(codename="add_Biology"))
        self.assertHttpCreated(self.api_client.post("/API/v1/Occurrence/?format=json&username={user}&api_key={api}".format(user=self.username, api=self.apikey), data={"geom":"POINT (1 1)"}))
        self.assertHttpCreated(self.api_client.post("/API/v1/drp_taxonomy/?format=json&username={user}&api_key={api}".format(user=self.username, api=self.apikey), data={"family":"Fungus", "taxon":"fungus","rank":"family", "hierarchysortorder":1}))

        #need to test post for biology with related occurrence, currently doesn't work
        #ob = Occurrence.objects.all()[0] #get an object from the occurrence table to we can try to add a related biology entry
        #self.assertHttpCreated(self.api_client.post("/API/v1/Biology/?format=json&username={user}&api_key={api}".format(user=self.username, api=self.apikey), data={"occurrence":30}))

    def test_get_list_json(self):
        self.user.user_permissions.add(Permission.objects.get(codename="add_Occurrence")) #you need add permission to read from the API - see custom_authorization.py
        resp = self.api_client.get("/API/v1/Occurrence/?format=json&username={user}&api_key={api}".format(user=self.username, api=self.apikey))
        self.assertEqual(resp.status_code, 200)
        self.assertValidJSONResponse(resp)

        # make sure correct number of objects returned
        self.assertEqual(len(self.deserialize(resp)['objects']), 1)


class TurkanaResourceTest(ResourceTestCase):
    # Use ``fixtures`` & ``urls`` as normal. See Django's ``TestCase``
    # documentation for the gory details.
    fixtures = ['API/fixtures/turkana_API_test_fixture', 'fixtures/fiber_data_150611.json']

    def setUp(self):
        super(TurkanaResourceTest, self).setUp()

        # Create a user.
        self.username = 'youzer'
        self.password = 'pass'
        self.user = User.objects.create_user(self.username, 'youzer@example.com', self.password)

        # Fetch the ``Entry`` object we'll use in testing.
        # Note that we aren't using PKs because they can change depending
        # on what other tests are running.

        self.testObject = Turkana.objects.get(specimen_number__exact=492)

        # We also build a detail URI, since we will be using it all over.
        # DRY, baby. DRY.
        self.detail_url = '/API/v1/turkana/{0}/'.format(self.testObject.pk)

    def get_credentials(self):
        return self.create_basic(username=self.username, password=self.password)

    def test_get_list_json(self):
        resp = self.api_client.get('/API/v1/turkana/', format='json', authentication=self.get_credentials())
        self.assertEqual(resp.status_code, 200)
        self.assertValidJSONResponse(resp)

        # make sure correct number of objects returned
        self.assertEqual(len(self.deserialize(resp)['objects']), 6)

    def test_get_detail_json(self):
        resp = self.api_client.get(self.detail_url, format='json', authentication=self.get_credentials())
        self.assertEqual(resp.status_code, 200)
        self.assertValidJSONResponse(resp)

        # Make sure correct number of fields returned
        self.assertEqual(len(self.deserialize(resp)), 99) #99 fields

    # def test_only_get_allowed(self):
    #     resp = self.api_client.get('/API/v1/turkana/standard/?format=json')
    #     self.assertEqual(self.deserialize(resp)['allowed_detail_http_methods'], [u'get'])


