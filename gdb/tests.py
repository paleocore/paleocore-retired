from django.test import TestCase
from models import Occurrence, Biology, Locality
from datetime import datetime
from fiber.models import Page


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
    def test_gdb_locality_save_simple(self):
        """
        Test Locality instance save method with the simplest possible attributes.
        """
        starting_record_count = Locality.objects.count()  # get current number of occurrence records
        # The simplest occurrence instance we can create needs six bits of data.
        # Using the instance creation and then save methods
        new_locality = Locality(locality_number=195,
                                locality_field_number="WP 204",
                                name="FG-195",
                                geom="POINT (-108.79805556 42.01944444)")
        new_locality.save()
        now = datetime.now()
        #self.assertEqual(Locality.objects.count(), starting_record_count+1)  # test that one record has been added
        self.assertEqual(new_locality.date_last_modified.day, now.day)  # test date last modified is correct
        self.assertEqual(new_locality.geom.coords[0], -108.79805556)
        self.assertEqual(new_locality.geom.coords[1], 42.01944444)

    def test_gdb_locality_create_method(self):
        """
        Test Locality instance create method with simple set of attributes.
        :return:
        """
        starting_record_count = Locality.objects.count()
        new_locality = Locality.objects.create(locality_number=195,
                                locality_field_number="WP 204",
                                name="FG-195",
                                geom="POINT (-108.79805556 42.01944444)")
        now = datetime.now()
        self.assertEqual(Locality.objects.count(), starting_record_count+1)  # test that one record has been added
        self.assertEqual(new_locality.date_last_modified.day, now.day)  # test date last modified is correct
        self.assertEqual(new_locality.geom.coords[0], -108.79805556)
        self.assertEqual(new_locality.geom.coords[1], 42.01944444)
