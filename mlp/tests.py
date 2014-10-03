from django.test import TestCase
from mlp.models import Occurrence, Biology
from fiber.models import Page
from django.core.urlresolvers import reverse
from datetime import datetime
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib.admin.sites import AdminSite


###################
# Factory Methods #
###################
def create_django_page_tree():
    mainmenu=Page(title='mainmenu')
    mainmenu.save()
    Home = Page(title='Home', parent=mainmenu, url='home', template_name='arcana_home.html')
    Home.save()
    data = Page(title='Data', parent=Home, url='data', template_name='')
    data.save()
    MLP = Page(title='MLP', parent=Home, url='mlp', template_name='')
    data.save()
    Upload = Page(title='Upload', parent=MLP, url='upload', template_name='')
    data.save()
    kml = Page(title='Data', parent=Upload, url='kml', template_name='')
    data.save()
    #members=Page(title='members', parent=home, url='members', template_name='base/members')
    #members.save()
    #meetings = Page(title='meetings', parent=mainmenu, url='meetings', template_name='')
    #meetings.save()


######################################
# Tests for models and their methods #
######################################
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
        self.assertEqual(new_occurrence.point_x(), 691311.7081000003963709)

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
        self.assertEqual(new_occurrence.point_x(), 691311.7081000003963709)


###################
# Page View Tests #
###################
class MLPViewTests(TestCase):
    """
    Test MLP page views with Django-Fiber
    """
    def test_mlp_home_view(self):
        create_django_page_tree()
        response = self.client.get(reverse('mlp:mlp_upload_kml'))  # this line fails!
        #self.assertEqual(response.status_code, 200)
        #self.assertQuerysetEqual(response.context['meeting_list'], [])
