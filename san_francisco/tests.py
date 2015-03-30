from django.test import TestCase
from san_francisco.models import Occurrence
from fiber.models import Page
# from django.core.urlresolvers import reverse
from datetime import datetime
# from django.utils import timezone
# from django.contrib.auth.models import User
# from django.contrib.auth import authenticate,login
# from django.contrib.admin.sites import AdminSite


###################
# Factory Methods #
###################
def create_django_page_tree():
    mainmenu = Page(title='mainmenu')
    mainmenu.save()
    home = Page(title='home', parent=mainmenu, url='home', template_name='arcana_home.html')
    home.save()
    data = Page(title='Data', parent=home, url='data', template_name='')
    data.save()
    san_francisco = Page(title='san_francisco', parent=home, url='san_francisco', template_name='')
    data.save()
    upload = Page(title='upload', parent=san_francisco, url='upload', template_name='')
    data.save()
    kml = Page(title='Data', parent=upload, url='kml', template_name='')
    kml.save()
    data.save()


######################################
# Tests for models and their methods #
######################################
class OccurrenceMethodsTests(TestCase):
    """
    Test san_francisco Occurrence instance creation and methods
    """
    def test_san_francisco_occurrence_save_simple(self):
        """
        Test san_francisco_occurrence instance save method with the simplest possible attributes.
        """
        starting_record_count = Occurrence.objects.count()  # get current number of occurrence records
        # The simplest occurrence instance we can create needs six bits of data.
        # Using the instance creation and then save methods
        new_occurrence = Occurrence(id=1, item_type="Faunal", basis_of_record="HumanObservation",
                                    collecting_method="Surface Standard", field_number=datetime.now(),
                                    geom="POINT (40.8352906016 11.5303732536)")
        new_occurrence.save()
        now = datetime.now()
        self.assertEqual(Occurrence.objects.count(), starting_record_count+1)  # test that one record has been added
        self.assertEqual(new_occurrence.date_last_modified.day, now.day)  # test date last modified is correct
        self.assertEqual(new_occurrence.point_x(), 40.8352906016)
        self.assertEqual(new_occurrence.point_y(), 11.5303732536)

    def test_san_francisco_create_method(self):
        """
        Test Occurrence instance create method with simple set of attributes.
        :return:
        """
        starting_record_count = Occurrence.objects.count()
        new_occurrence = Occurrence.objects.create(id=1, item_type="Faunal", basis_of_record="HumanObservation",
                                                   collecting_method="Surface Standard", field_number=datetime.now(),
                                                   geom="POINT (40.8352906016 11.5303732536)")
        now = datetime.now()
        self.assertEqual(Occurrence.objects.count(), starting_record_count+1)  # test that one record has been added
        self.assertEqual(new_occurrence.date_last_modified.day, now.day)  # test date last modified is correct
        self.assertEqual(new_occurrence.point_x(), 40.8352906016)

    def test_san_francisco_create_method_invalid_item_type(self):
        """
        """
        starting_record_count = Occurrence.objects.count()
        new_occurrence = Occurrence.objects.create(id=1, item_type="Fake", basis_of_record="HumanObservation",
                                                   collecting_method="Surface Standard", field_number=datetime.now(),
                                                   geom="POINT (40.8352906016 11.5303732536)")
        now = datetime.now()
        self.assertEqual(Occurrence.objects.count(), starting_record_count+1)  # test that one record has been added
        self.assertEqual(new_occurrence.date_last_modified.day, now.day)  # test date last modified is correct
        self.assertEqual(new_occurrence.point_x(), 40.8352906016)
        self.assertEqual(new_occurrence.item_type, "Fake")

    def test_san_francisco_save_method_valid_item_type(self):
        """
        """
        starting_record_count = Occurrence.objects.count()
        new_occurrence = Occurrence()
        new_occurrence.item_type = "Faunal"
        new_occurrence.basis_of_record = "HumanObservation"
        new_occurrence.collecting_method = "Surface Standard"
        new_occurrence.field_number = datetime.now()
        new_occurrence.geom = "POINT (40.8352906016 11.5303732536)"
        new_occurrence.save()

        now = datetime.now()
        self.assertEqual(Occurrence.objects.count(), starting_record_count+1)  # test that one record has been added
        self.assertEqual(new_occurrence.date_last_modified.day, now.day)  # test date last modified is correct
        self.assertEqual(new_occurrence.point_x(), 40.8352906016)
        self.assertEqual(new_occurrence.item_type, "Faunal")

    def test_san_francisco_save_method_invalid_item_type(self):
        """
        """
        starting_record_count = Occurrence.objects.count()
        new_occurrence = Occurrence()
        new_occurrence.item_type = "Fake"
        new_occurrence.basis_of_record = "HumanObservation"
        new_occurrence.collecting_method = "Surface Standard"
        new_occurrence.field_number = datetime.now()
        new_occurrence.geom = "POINT (40.8352906016 11.5303732536)"
        new_occurrence.save()

        now = datetime.now()
        self.assertEqual(Occurrence.objects.count(), starting_record_count+1)  # test that one record has been added
        self.assertEqual(new_occurrence.date_last_modified.day, now.day)  # test date last modified is correct
        self.assertEqual(new_occurrence.point_x(), 40.8352906016)
        self.assertEqual(new_occurrence.item_type, "Fake")