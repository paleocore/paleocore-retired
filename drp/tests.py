from django.test import TestCase
from drp.models import Occurrence, Biology
from fiber.models import Page
from django.core.urlresolvers import reverse
from datetime import datetime
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib.admin.sites import AdminSite

# def create_Occurrence():
#     new_occurrence = Occurrence(id=29, barcode=9999, basisofrecord="FossilSpecimen", itemtype="Floral",
#                                     catalognumber="DIK-9999-9", itemdescription="test", itemscientificname="test",
#                                     geom="POINT (658198.7081000003963709 1222366.8992999996989965)")
#     return(new_occurrence)


def create_django_page_tree():
        mainmenu=Page(title='mainmenu')
        mainmenu.save()
        home=Page(title='home', parent=mainmenu, url='home', template_name='arcana_home.html')
        home.save()
        about=Page(title='about', parent=mainmenu, url='about', template_name='arcana_2col_left.html')
        about.save()
        workshops=Page(title='workshops', parent=mainmenu, url='workshops', template_name='')
        workshops.save()
        data = Page(title='data', parent=mainmenu, url='data', template_name='')
        data.save()
        tools = Page(title='tools', parent=mainmenu, url='tools', template_name='')
        tools.save()
        standards = Page(title='standards', parent=mainmenu, url='standards', template_name='')
        standards.save()


class OccurrenceMethodsTests(TestCase):
    """
    Test Occurrence instance creation and methods
    """
    def test_Occurrence_save_simple(self):
        """
        Test Occurrence instance save method with the simplest possible attributes, coordinates only
        """
        starting_record_count = Occurrence.objects.count()  # get current number of occurrence records
        # The simplest occurrence instance we can create needs only a location.
        # Using the instance creation and then save methods
        new_occurrence = Occurrence(geom="POINT (658198.7081000003963709 1221366.8992999996989965)")
        new_occurrence.save()
        now = datetime.now()
        self.assertEqual(Occurrence.objects.count(), starting_record_count+1)  # test that one record has been added
        self.assertEqual(new_occurrence.catalognumber, "--")  # test catalog number generation in save method
        self.assertEqual(new_occurrence.datelastmodified.day, now.day)  # test date last modified is correct
        self.assertEqual(new_occurrence.point_X(), 658198.7081000003963709)

    def test_Occurrence_create_simple(self):
        """
        Test Occurrence instance creation with the simplest possible attributes, coordinates only
        """
        starting_record_count = Occurrence.objects.count()  # get current number of occurrence records
        # The simplest occurrence instance we can create needs only a location.
        # Using the instance creation and then save methods
        new_occurrence = Occurrence.objects.create(geom="POINT (658198.7081000003963709 1221366.8992999996989965)")
        now = datetime.now()
        self.assertEqual(Occurrence.objects.count(), starting_record_count+1)  # test that one record has been added
        self.assertEqual(new_occurrence.catalognumber, "--")  # test catalog number generation in save method
        self.assertEqual(new_occurrence.datelastmodified.day, now.day)  # test date last modified is correct
        self.assertEqual(new_occurrence.point_X(), 658198.7081000003963709)

    def test_Occurrence_create_fossil_specimen(self):
        """
        Test Occurrence instance creation with the simplest possible attributes, coordinates only
        """
        starting_record_count = Occurrence.objects.count()  # get current number of occurrence records
        starting_record_count_biology = Biology.objects.count()  # get the current number of biology records
        # The simplest occurrence instance we can create needs only a location.
        # Using the instance creation and then save methods
        new_occurrence = Occurrence.objects.create(
            barcode = 1111,
            basisofrecord="FossilSpecimen",
            institutionalcode = "INST",
            collectioncode = "COL",
            paleolocalitynumber="1",
            itemnumber="1",
            geom="POINT (658198.7081000003963709 1221366.8992999996989965)")
        now = datetime.now()
        self.assertEqual(Occurrence.objects.count(), starting_record_count+1)  # test that one record has been added
        self.assertEqual(new_occurrence.catalognumber, "COL-1-1")  # test catalog number generation in save method
        self.assertEqual(new_occurrence.datelastmodified.day, now.day)  # test date last modified is correct
        self.assertEqual(new_occurrence.point_X(), 658198.7081000003963709)
        self.assertEqual(Biology.objects.count(), starting_record_count_biology)  # test that no biology record was added

    def test_Occurrence_create_observation(self):
        """
        Test Occurrence instance creation with the simplest possible attributes, coordinates only
        """
        starting_record_count = Occurrence.objects.count()  # get current number of occurrence records
        starting_record_count_biology = Biology.objects.count()  # get the current number of biology records
        # The simplest occurrence instance we can create needs only a location.
        # Using the instance creation and then save methods
        new_occurrence = Occurrence.objects.create(
            barcode = 1111,
            basisofrecord="HumanObservation",
            institutionalcode = "INST",
            collectioncode = "COL",
            paleolocalitynumber="1",
            itemnumber="1",
            geom="POINT (658198.7081000003963709 1221366.8992999996989965)")
        now = datetime.now()
        self.assertEqual(Occurrence.objects.count(), starting_record_count+1)  # test that one record has been added
        self.assertEqual(new_occurrence.catalognumber, "COL-1-1")  # test catalog number generation in save method
        self.assertEqual(new_occurrence.datelastmodified.day, now.day)  # test date last modified is correct
        self.assertEqual(new_occurrence.point_X(), 658198.7081000003963709)
        self.assertEqual(Biology.objects.count(), starting_record_count_biology)  # test that no biology record was added

    def test_Biology_create(self):
        """
        Test Occurrence instance creation with the simplest possible attributes, coordinates only
        """
        starting_record_count = Biology.objects.count()  # get the current number of biology records
        # The simplest occurrence instance we can create needs only a location.
        # Using the instance creation and then save methods
        new_biology = Biology.objects.create(
            barcode = 1111,
            basisofrecord="FossilSpecimen",
            itemtype = "Faunal",
            institutionalcode = "INST",
            collectioncode = "COL",
            paleolocalitynumber="1",
            itemnumber="1",
            family="Bovidae",
            geom="POINT (658198.7081000003963709 1221366.8992999996989965)")
        now = datetime.now()
        self.assertEqual(Biology.objects.count(), starting_record_count+1)  # test that one record has been added
        self.assertEqual(new_biology.catalognumber, "COL-1-1")  # test catalog number generation in save method
        self.assertEqual(new_biology.datelastmodified.day, now.day)  # test date last modified is correct
        self.assertEqual(new_biology.point_X(), 658198.7081000003963709)


    def test_Occurrence_create_floral(self):
        """
        Test Occurrence instance creation with the simplest possible attributes, coordinates only
        """
        starting_record_count = Occurrence.objects.count()  # get current number of occurrence records
        starting_record_count_biology = Biology.objects.count()  # get the current number of biology records
        # The simplest occurrence instance we can create needs only a location.
        # Using the instance creation and then save methods
        new_occurrence = Occurrence.objects.create(
            barcode = 1111,
            basisofrecord="FossilSpecimen",
            itemtype = "Floral",
            institutionalcode = "INST",
            collectioncode = "COL",
            paleolocalitynumber="1",
            itemnumber="1",
            geom="POINT (658198.7081000003963709 1221366.8992999996989965)")
        now = datetime.now()
        self.assertEqual(Occurrence.objects.count(), starting_record_count+1)  # test that one record has been added
        self.assertEqual(new_occurrence.catalognumber, "COL-1-1")  # test catalog number generation in save method
        self.assertEqual(new_occurrence.datelastmodified.day, now.day)  # test date last modified is correct
        self.assertEqual(new_occurrence.point_X(), 658198.7081000003963709)
        self.assertEqual(Biology.objects.count(), starting_record_count_biology)  # test that no biology record was added


class BiologySearchTest(TestCase):

    def test_biology_searchbox(self):
        """
        Test Occurrence admin search box
        :return:
        """
        user = User.objects.create_user('john', 'lennon@thebeatles.com', 'thewalruswaspaul')
        user.is_superuser = True
        user.is_staff = True
        user.save()

        self.client.login(username="john", password="thewalruswaspaul")
        self.assertEqual(user.has_perm("drp.delete_Biology"), True)

        create_django_page_tree()
        response = self.client.get("/admin/drp/Biology/", {"q": "asdfe"})
        self.assertNotContains(response, "<h1>FieldError at /admin/")
        self.assertEqual(response.status_code, 200)



class MockRequest(object):
    pass


class MockSuperUser(object):
    def has_perm(self, perm):
        return True

request = MockRequest()
request.user = MockSuperUser()


class OccurrenceAdminTests(TestCase):
    """
    Tests for the Occurrence admin pages. These tests based on django admin tests on github
    https://github.com/django/django/blob/master/tests/modeladmin/tests.py
    """

    def setUp(self):
        self.occurrence = Occurrence.objects.create(
            barcode=1111,
            basisofrecord="FossilSpecimen",
            itemtype="Faunal",
            institutionalcode="INST",
            collectioncode="COL",
            paleolocalitynumber="1",
            itemnumber="1",
            geom="POINT (658198.7081000003963709 1221366.8992999996989965)"
        )
        self.site = AdminSite()

    def test_occurrence_admin_download_csv_action(self):
        user = User.objects.create_user('john', 'lennon@thebeatles.com', 'thewalruswaspaul')
        user.is_superuser = True
        user.is_staff = True
        user.save()

        self.client.login(username="john", password="thewalruswaspaul")
        self.assertEqual(user.has_perm("drp.delete_Biology"), True)

        create_django_page_tree()
        response = self.client.get("/admin/drp/Occurrence/")
        self.assertEqual(response.status_code, 200)


class MockRequest(object):
    pass

class MockSuperUser(object):
    def has_perm(self, perm):
        return True

request = MockRequest()
request.user = MockSuperUser()
