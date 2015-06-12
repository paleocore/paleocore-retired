from django.test import TestCase
from paleosites.models import Site
from django.contrib.gis.geos import Point

class SiteModelTests(TestCase):
    """
    Tests for Site model and methods
    """
    def test_create_site_method(self):
        initial_site_record_count = Site.objects.count()  # initial count of site instances

        # create a new site
        Site.objects.create(
            site="Some Site Name",
            country="BG",
            data_source="OSA",
            altitude="500",
            site_type="Shelter",
            display=True,
            map_location=Point(42.11, 24.75),
            notes="""This is a test site"""
        )

        # test that a new site was added to the DB
        self.assertEqual(Site.objects.count(), initial_site_record_count+1)

        # test site attributes
        test_site = Site.objects.get(site__exact="Some Site Name")
        self.assertEqual(test_site.site, "Some Site Name")
        self.assertEqual(test_site.country, "BG")
        self.assertEqual(test_site.country.name, "Bulgaria")  # test django_counties attribute
        self.assertEqual(test_site.data_source, "OSA")
        self.assertEqual(test_site.site_type, "Shelter")
        self.assertTrue(test_site.display)
        self.assertEqual(test_site.map_location.x, 42.11)
        self.assertEqual(test_site.map_location.y, 24.75)
        self.assertEqual(test_site.map_location.coords, (42.11, 24.75))
        self.assertEqual(test_site.notes, "This is a test site")

    def test_site_model_methods(self):
        initial_site_record_count = Site.objects.count()  # initial count of site instances

        # create a new site
        Site.objects.create(
            site="Paris",
            country="FR",
            data_source="OSA",
            altitude="500",
            site_type="Shelter",
            display=True,
            map_location=Point(48.9, 2.45),
            notes="""This is anoter test site"""
        )

        # test that a new site was added to the DB
        self.assertEqual(Site.objects.count(), initial_site_record_count+1)

        # test site model methods
        paris=Site.objects.get(site="Paris")
        self.assertEqual(paris.longitude(), 48.9)
        self.assertEqual(paris.latitude(), 2.45)

