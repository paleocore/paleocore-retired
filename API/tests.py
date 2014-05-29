from tastypie.test import ResourceTestCase
from django.contrib.auth.models import User
from turkana.models import Turkana
from drp.tests import create_django_page_tree #should probably put this create page tree code in mysite.tests and import for all apps

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
