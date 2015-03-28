from django.test import TestCase
from drp.models import Occurrence, Biology, Locality
from taxonomy.models import Taxon, TaxonRank, IdentificationQualifier
from fiber.models import Page
from django.core.urlresolvers import reverse
from datetime import datetime
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib.admin.sites import AdminSite
from django.contrib.gis.geos import GEOSGeometry, Point, Polygon


def create_django_page_tree():
        mainmenu = Page(title='mainmenu')
        mainmenu.save()
        home = Page(title='home', parent=mainmenu, url='home', template_name='arcana_home.html')
        home.save()
        about = Page(title='about', parent=mainmenu, url='about', template_name='arcana_2col_left.html')
        about.save()
        workshops=Page(title='workshops', parent=mainmenu, url='workshops', template_name='')
        workshops.save()
        data = Page(title='data', parent=mainmenu, url='data', template_name='')
        data.save()
        tools = Page(title='tools', parent=mainmenu, url='tools', template_name='')
        tools.save()
        standards = Page(title='standards', parent=mainmenu, url='standards', template_name='')
        standards.save()


class LocalityMethodsTests(TestCase):
    """
    Test Locality instance creation and methods
    """
    def test_locality_save_simple(self):
        starting_record_count = Locality.objects.count()  # get current record count
        poly = Polygon(
            ((675158.6189000001, 1227037.2491999995), (675158.4829000002, 1226987.2874999996),
             (675218.1513999999, 1226987.2874999996), (675218.1513999999, 1226920.9891999997),
             (675158.6189000001, 1227037.2491999995))
        )
        new_locality = Locality(paleolocalitynumber=1, geom=poly)
        new_locality.save()
        self.assertEqual(Locality.objects.count(), starting_record_count+1)

    def test_locality_create_simple(self):
        starting_record_count = Locality.objects.count()  # get current record count
        poly = Polygon(
            ((675158.6189000001, 1227037.2491999995), (675158.4829000002, 1226987.2874999996),
             (675218.1513999999, 1226987.2874999996), (675218.1513999999, 1226920.9891999997),
             (675158.6189000001, 1227037.2491999995))
        )
        Locality.objects.create(paleolocalitynumber=1, geom=poly)
        self.assertEqual(Locality.objects.count(), starting_record_count+1)


class TaxonMethodsTests(TestCase):
    """
    Test Taxon instance creation and methods
    """
    def test_taxon_save_method(self):
        TaxonRank.objects.create(
            name="Domain",
            plural="Domains",
            ordinal=5
        )
        TaxonRank.objects.create(
            name="Kingdom",
            plural="Kingdoms",
            ordinal=10
        )
        phylum=TaxonRank.objects.create(
            name="Phylum",
            plural="Phyla",
            ordinal=20
        )
        taxonomic_class=TaxonRank.objects.create(
            name="Class",
            plural="Classes",
            ordinal=30
        )
        taxonomic_order=TaxonRank.objects.create(
            name="Order",
            plural="Orders",
            ordinal=40
        )


        taxon_starting_record_count = Taxon.objects.count()  # get current record count
        new_taxon = Taxon(
            name="Primates",
            rank=taxonomic_order
        )
        new_taxon.save()
        self.assertEqual(Taxon.objects.count(), taxon_starting_record_count+1)


class OccurrenceMethodTests(TestCase):
    """
    Test Occurrence instance creation and methods
    """

    def setup(self):
        poly = Polygon(
            ((675158.6189000001, 1227037.2491999995), (675158.4829000002, 1226987.2874999996),
             (675218.1513999999, 1226987.2874999996), (675218.1513999999, 1226920.9891999997),
             (675158.6189000001, 1227037.2491999995))
        )
        Locality.objects.create(paleolocalitynumber=1, geom=poly)

    def test_occurrence_save_simple(self):
        """
        Test Occurrence instance save method with the simplest possible attributes, coordinates only
        """
        starting_record_count = Occurrence.objects.count()  # get current number of occurrence records
        # The simplest occurrence instance we can create needs only a location.
        # Using the instance creation and then save methods
        poly = Polygon(
            ((675158.6189000001, 1227037.2491999995), (675158.4829000002, 1226987.2874999996),
             (675218.1513999999, 1226987.2874999996), (675218.1513999999, 1226920.9891999997),
             (675158.6189000001, 1227037.2491999995))
        )
        locality_2 = Locality.objects.create(paleolocalitynumber=2, geom=poly)
        new_occurrence = Occurrence(geom="POINT (658198.7081000003963709 1221366.8992999996989965)",
                                    locality=locality_2)
        new_occurrence.save()
        now = datetime.now()
        self.assertEqual(Occurrence.objects.count(), starting_record_count+1)  # test that one record has been added
        self.assertEqual(new_occurrence.catalognumber, "--")  # test catalog number generation in save method
        self.assertEqual(new_occurrence.datelastmodified.day, now.day)  # test date last modified is correct
        self.assertEqual(new_occurrence.point_X(), 658198.7081000003963709)
        self.assertEqual(new_occurrence.locality.paleolocalitynumber, 2)

    def test_occurrence_create_simple(self):
        """
        Test Occurrence instance creation with the simplest possible attributes, coordinates only
        """
        starting_record_count = Occurrence.objects.count()  # get current number of occurrence records
        # The simplest occurrence instance we can create needs only a location.
        # Using the instance creation and then save methods
        poly = Polygon(
            ((677158.6189000001, 1227037.2491999995), (677158.4829000002, 1228987.2874999996),
             (677218.1513999999, 1226987.2874999996), (677218.1513999999, 1226920.9891999997),
             (677158.6189000001, 1227037.2491999995))
        )
        locality_3 = Locality.objects.create(paleolocalitynumber=3, geom=poly)
        new_occurrence = Occurrence.objects.create(geom=Point(658198.7081000003963709, 1221366.8992999996989965),
                                                   locality=locality_3)
        now = datetime.now()
        self.assertEqual(Occurrence.objects.count(), starting_record_count+1)  # test that one record has been added
        self.assertEqual(new_occurrence.catalognumber, "--")  # test catalog number generation in save method
        self.assertEqual(new_occurrence.datelastmodified.day, now.day)  # test date last modified is correct
        self.assertEqual(new_occurrence.point_X(), 658198.7081000003963709)


class BiologyMethodTests(TestCase):
    """
    Test Biology instance methods
    """

    def biology_setup(self):
        poly = Polygon(
            ((677158.6189000001, 1227037.2491999995), (677158.4829000002, 1228987.2874999996),
             (677218.1513999999, 1226987.2874999996), (677218.1513999999, 1226920.9891999997),
             (677158.6189000001, 1227037.2491999995))
        )
        Locality.objects.create(paleolocalitynumber=4, geom=poly)

        taxonomic_order = TaxonRank.objects.create(
            name="Order",
            plural="Orders",
            ordinal=40
        )
        Taxon.objects.create(
            name="Primates",
            rank=taxonomic_order
        )

        IdentificationQualifier.objects.create(
            name="None",
            qualified=False
        )
        IdentificationQualifier.objects.create(
            name="cf.",
            qualified=True
        )
        IdentificationQualifier.objects.create(
            name="aff.",
            qualified=True
        )

    def test_biology_save_method(self):
        """
        Test Biology instance creation with save method
        """

        self.biology_setup()
        locality = Locality.objects.get(paleolocalitynumber__exact=4)
        new_taxon = Taxon.objects.get(name__exact="Primates")
        id_qual = IdentificationQualifier.objects.get(name__exact="None")

        starting_occurrence_record_count = Occurrence.objects.count()  # get current number of occurrence records
        starting_biology_record_count = Biology.objects.count()  # get the current number of biology records
        # The simplest occurrence instance we can create needs only a location.
        # Using the instance creation and then save methods

        new_bio = Biology(
            barcode=1111,
            basisofrecord="FossilSpecimen",
            institutionalcode="INST",
            collectioncode="COL",
            paleolocalitynumber="1",
            itemnumber="1",
            geom="POINT (658198.7081000003963709 1221366.8992999996989965)",
            locality=locality,
            taxon=new_taxon,
            identification_qualifier=id_qual
        )
        new_bio.save()
        now = datetime.now()
        self.assertEqual(Occurrence.objects.count(), starting_occurrence_record_count+1)
        self.assertEqual(Biology.objects.count(), starting_biology_record_count+1)

        self.assertEqual(new_bio.catalognumber, "COL-1-1")  # test catalog number generation in save method
        self.assertEqual(new_bio.datelastmodified.day, now.day)  # test date last modified is correct
        self.assertEqual(new_bio.point_X(), 658198.7081000003963709)

    def test_biology_create_observation(self):
        """
        Test Biology instance creation for observations
        """

        self.biology_setup()
        locality = Locality.objects.get(paleolocalitynumber__exact=4)
        new_taxon = Taxon.objects.get(name__exact="Primates")
        id_qual = IdentificationQualifier.objects.get(name__exact="None")

        occurrence_starting_record_count = Occurrence.objects.count()  # get current number of occurrence records
        biology_starting_record_count = Biology.objects.count()  # get the current number of biology records
        # The simplest occurrence instance we can create needs only a location.
        # Using the instance creation and then save methods
        new_occurrence = Biology.objects.create(
            barcode=1111,
            basisofrecord="HumanObservation",
            institutionalcode="INST",
            collectioncode="COL",
            paleolocalitynumber="1",
            itemnumber="1",
            geom="POINT (658198.7081000003963709 1221366.8992999996989965)",
            locality=locality,
            taxon=new_taxon,
            identification_qualifier=id_qual
        )
        now = datetime.now()
        self.assertEqual(Occurrence.objects.count(), occurrence_starting_record_count+1)  # test that one record has been added
        self.assertEqual(new_occurrence.catalognumber, "COL-1-1")  # test catalog number generation in save method
        self.assertEqual(new_occurrence.datelastmodified.day, now.day)  # test date last modified is correct
        self.assertEqual(new_occurrence.point_X(), 658198.7081000003963709)
        self.assertEqual(Biology.objects.count(), biology_starting_record_count+1)  # test that no biology record was added
        self.assertEqual(Biology.objects.filter(basisofrecord__exact="HumanObservation").count(), 1)


# class BiologySearchTest(TestCase):
#
#     def test_biology_searchbox(self):
#         """
#         Test Occurrence admin search box
#         :return:
#         """
#         user = User.objects.create_user('john', 'lennon@thebeatles.com', 'thewalruswaspaul')
#         user.is_superuser = True
#         user.is_staff = True
#         user.save()
#
#         self.client.login(username="john", password="thewalruswaspaul")
#         self.assertEqual(user.has_perm("drp.delete_Biology"), True)
#
#         create_django_page_tree()
#         response = self.client.get("/admin/drp/biology/", {"q": "asdfe"})
#         self.assertNotContains(response, "<h1>FieldError at /admin/")
#         self.assertEqual(response.status_code, 200)
#
#
#
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
        poly = Polygon(
            ((675158.6189000001, 1227037.2491999995), (675158.4829000002, 1226987.2874999996),
             (675218.1513999999, 1226987.2874999996), (675218.1513999999, 1226920.9891999997),
             (675158.6189000001, 1227037.2491999995))
        )
        self.locality = Locality.objects.create(
            paleolocalitynumber=1,
            collectioncode="DIK",
            description1="This is a nice locality",
            geom=poly
        )
        self.occurrence = Occurrence.objects.create(
            barcode=1111,
            basisofrecord="FossilSpecimen",
            itemtype="Faunal",
            institutionalcode="INST",
            collectioncode="COL",
            paleolocalitynumber="1",
            itemnumber="1",
            geom="POINT (658198.7081000003963709 1221366.8992999996989965)",
            locality=self.locality
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
        response = self.client.get("/admin/drp/occurrence/")
        self.assertEqual(response.status_code, 200)


class MockRequest(object):
    pass


class MockSuperUser(object):
    def has_perm(self, perm):
        return True

request = MockRequest()
request.user = MockSuperUser()
