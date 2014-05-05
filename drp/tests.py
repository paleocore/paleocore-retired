from django.test import TestCase
from drp.models import drp_occurrence
from fiber.models import Page
from django.core.urlresolvers import reverse
from datetime import datetime
from django.utils import timezone


# def create_drp_occurrence():
#     new_occurrence = drp_occurrence(id=29, barcode=9999, basisofrecord="FossilSpecimen", itemtype="Floral",
#                                     catalognumber="DIK-9999-9", itemdescription="test", itemscientificname="test",
#                                     geom="POINT (658198.7081000003963709 1222366.8992999996989965)")
#     return(new_occurrence)


class OccurrenceMethodsTests(TestCase):
    """
    Test instance creation and methods
    """
    def test_drp_occurrence_create_simple(self):
        """
        Test instance creation and custom save methods
        """
        starting_record_count=drp_occurrence.objects.count()  # get current number of occurrence records
        # The simplest occurrence instance we can create needs only a location. The id is created automatically.
        new_occurrence=drp_occurrence(geom="POINT (658198.7081000003963709 1221366.8992999996989965)")
        new_occurrence.save()
        now = datetime.now()
        self.assertEqual(drp_occurrence.objects.count(), starting_record_count+1)  # test that one record has been added
        self.assertEqual(new_occurrence.catalognumber, "--")  # test catalog number generation in save method
        self.assertEqual(new_occurrence.datelastmodified.day, now.day)

    def test_drp_occurrence_create_faunal(self):
        self.assertEqual(drp_occurrence.objects.count(), 0)
        new_occurrence=drp_occurrence(
            itemtype="Faunal",
            geom="POINT (658298.7081000003963709 1221366.8992999996989965)")
        new_occurrence.save()
        self.assertEqual(drp_occurrence.objects.count(), 1)