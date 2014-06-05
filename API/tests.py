from tastypie.test import ResourceTestCase
from django.contrib.auth.models import User
from turkana.models import Turkana
from drp.models import drp_occurrence, drp_biology
from drp.tests import create_django_page_tree #should probably put this create page tree code in mysite.tests and import for all apps
from tastypie.models import ApiKey


class DRPResourceTest(ResourceTestCase):
    fixtures = ['API/fixtures/DRP_API_test_fixture']
    multi_db = True #must be true, or the test case won't load fixtures to non-default databases

    def setUp(self):
        super(DRPResourceTest, self).setUp()

        # Create a user.
        self.username = 'youzer'
        self.password = 'pass'
        self.user = User.objects.create_user(self.username, 'youzer@example.com', self.password)
        ApiKey.objects.create(user=self.user)
        self.apikey = ApiKey.objects.get(user=self.user).key


        self.assertEqual(drp_occurrence.objects.count(), 1)
        self.assertEqual(drp_biology.objects.count(), 1)
        self.testObject = drp_occurrence.objects.get(catalognumber="DIK-12-1")


    def get_basic_credentials(self):
        return self.create_basic(username=self.username, password=self.password)

    def test_unauthorized(self):
        self.assertHttpUnauthorized(self.api_client.get("/API/v1/drp_occurrence/?format='json'"))
        self.assertHttpUnauthorized(self.api_client.get("/API/v1/drp_biology/?format='json'"))
        self.assertHttpUnauthorized(self.api_client.get("/API/v1/drp_taxonomy/?format='json'"))

    def test_authorized(self):
        self.assertHttpOK(self.api_client.get("/API/v1/drp_occurrence/?format=json&username={user}&api_key={api}".format(user=self.username, api=self.apikey)))
        self.assertHttpOK(self.api_client.get("/API/v1/drp_taxonomy/?format=json&username={user}&api_key={api}".format(user=self.username, api=self.apikey)))
        self.assertHttpOK(self.api_client.get("/API/v1/drp_biology/?format=json&username={user}&api_key={api}".format(user=self.username, api=self.apikey)))

    def test_get_list_json(self):
        resp = self.api_client.get("/API/v1/drp_occurrence/?format=json&username={user}&api_key={api}".format(user=self.username, api=self.apikey))
        self.assertEqual(resp.status_code, 200)
        self.assertValidJSONResponse(resp)

        # make sure correct number of objects returned
        self.assertEqual(len(self.deserialize(resp)['objects']), 1)

    def test_get_list_csv(self):
        resp = self.api_client.get("/API/v1/drp_occurrence/?format=csv&username={user}&api_key={api}".format(user=self.username, api=self.apikey))
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp["content-type"], "text/csv; charset=utf-8")

        #this is a hacky test to make sure the csv doesn't contain any embeded json objects, i.e. that it has been approproately flattened by the csv serializer
        self.assertNotContains(resp, "{")

class TurkanaResourceTest(ResourceTestCase):
    # Use ``fixtures`` & ``urls`` as normal. See Django's ``TestCase``
    # documentation for the gory details.
    fixtures = ['API/fixtures/turkana_API_test_fixture']

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
        create_django_page_tree()

    def get_credentials(self):
        return self.create_basic(username=self.username, password=self.password)

    def test_get_list_json(self):
        resp = self.api_client.get('/API/v1/turkana/', format='json', authentication=self.get_credentials())
        self.assertEqual(resp.status_code, 200)
        self.assertValidJSONResponse(resp)

        # make sure correct number of objects returned
        self.assertEqual(len(self.deserialize(resp)['objects']), 6)

    def test_get_list_csv(self):
        resp = self.api_client.get('/API/v1/turkana/?format=csv', authentication=self.get_credentials())
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp["content-type"], "text/csv; charset=utf-8")

        #this is a hacky test to make sure the csv doesn't contain any embeded json objects, i.e. that it has been approproately flattened by the csv serializer
        self.assertNotContains(resp, "{")

    def test_get_detail_json(self):
        resp = self.api_client.get(self.detail_url, format='json', authentication=self.get_credentials())
        self.assertEqual(resp.status_code, 200)
        self.assertValidJSONResponse(resp)

        # Make sure correct number of fields returned
        self.assertEqual(len(self.deserialize(resp)), 99) #99 fields

    def test_get_detail_csv(self):
        resp = self.api_client.get(self.detail_url + '?format=csv', authentication=self.get_credentials())
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp["content-type"], "text/csv; charset=utf-8")

        #this is a hacky test to make sure the csv doesn't contain any embeded json objects, i.e. that it has been approproately flattened by the csv serializer
        self.assertNotContains(resp, "{")

    def test_only_get_allowed(self):
        resp = self.api_client.get('/API/v1/turkana/schema/?format=json')
        self.assertEqual(self.deserialize(resp)['allowed_detail_http_methods'],[u'get'])
