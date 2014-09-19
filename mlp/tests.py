from django.test import TestCase
from mlp.models import Occurrence, Biology
from fiber.models import Page
from django.core.urlresolvers import reverse
from datetime import datetime
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib.admin.sites import AdminSite


# Create your tests here.
class OccurrenceMethodsTests(TestCase):
    """
    Test mlp Occurrence instance creation and methods
    """
    def test_mlp_occurrence_save_simple(self):
        """
        Test mlp_occurrence instance save method with the simplest possible attributes.
        """
        starting_record_count = Occurrence.objects.count()  # get current number of occurrence records
        # The simplest occurrence instance we can create needs six bits of data.
        # Using the instance creation and then save methods
        new_occurrence = Occurrence(id=1, item_type="Faunal", basis_of_record="HumanObservation",
                                    collecting_method="Surface Standard", field_number=datetime.now(),
                                    geom="POINT (691311.7081000003963709 1272538.8992999996989965)")
        new_occurrence.save()
        now = datetime.now()
        self.assertEqual(Occurrence.objects.count(), starting_record_count+1)  # test that one record has been added
        self.assertEqual(new_occurrence.date_last_modified.day, now.day)  # test date last modified is correct
        self.assertEqual(new_occurrence.point_X(), 691311.7081000003963709)

    def test_mlp_create_method(self):
        """
        Test Occurrence instance create method with simple set of attributes.
        :return:
        """
        starting_record_count = Occurrence.objects.count()
        new_occurrence = Occurrence.objects.create(id=1, item_type="Faunal", basis_of_record="HumanObservation",
                                    collecting_method="Surface Standard", field_number=datetime.now(),
                                    geom="POINT (691311.7081000003963709 1272538.8992999996989965)")
        now = datetime.now()
        self.assertEqual(Occurrence.objects.count(), starting_record_count+1)  # test that one record has been added
        self.assertEqual(new_occurrence.date_last_modified.day, now.day)  # test date last modified is correct
        self.assertEqual(new_occurrence.point_X(), 691311.7081000003963709)
