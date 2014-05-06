from django.test import TestCase
from drp.models import drp_occurrence
from fiber.models import Page
from django.core.urlresolvers import reverse
from datetime import datetime
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login

# def create_drp_occurrence():
#     new_occurrence = drp_occurrence(id=29, barcode=9999, basisofrecord="FossilSpecimen", itemtype="Floral",
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

    # def test_drp_occurrence_create_faunal(self):
    #     self.assertEqual(drp_occurrence.objects.count(), 0)
    #     new_occurrence=drp_occurrence(
    #         itemtype="Faunal",
    #         geom="POINT (658298.7081000003963709 1221366.8992999996989965)")
    #     new_occurrence.save()
    #     self.assertEqual(drp_occurrence.objects.count(), 1)


class BiologySearchTest(TestCase):

    def test_biology_searchbox(self):

        user = User.objects.create_user('john', 'lennon@thebeatles.com', 'thewalruswaspaul')
        user.is_superuser = True
        user.is_staff = True
        user.save()

        self.client.login(username="john", password="thewalruswaspaul")
        self.assertEqual(user.has_perm("drp.delete_drp_biology"), True)

        create_django_page_tree()
        response = self.client.get("/admin/drp/drp_biology/", {"q":"asdf"})
        self.assertNotContains(response, "<h1>FieldError at /admin/")
        self.assertEqual(response.status_code, 200)