from django.test import TestCase
from drp.models import *
from django.contrib.gis.geos import Point

class AddDeleteOccurrence(TestCase):
    def setUp(self):
        newRecord = drp_occurrence(geom=Point(1,1))
        newRecord.save()

    def test_record_exists(self):
        nrecords = drp_occurrence.objects.all().count()
        self.assertEqual(nrecords, 1)



class ProjectIndexViewTests(TestCase):
    fixtures = ['fixtures/fiber_test_data.json']
