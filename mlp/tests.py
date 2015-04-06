from django.test import TestCase
from mlp.models import Occurrence
from fiber.models import Page
from django.core.urlresolvers import reverse
from datetime import datetime
from mlp.forms import UploadKMLForm
from django.core.files.uploadedfile import SimpleUploadedFile
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
    mlp = Page(title='mlp', parent=home, url='mlp', template_name='')
    data.save()
    upload = Page(title='upload', parent=mlp, url='upload', template_name='')
    data.save()
    kml = Page(title='Data', parent=upload, url='kml', template_name='')
    kml.save()
    data.save()


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
                                    geom="POINT (40.8352906016 11.5303732536)")
        new_occurrence.save()
        now = datetime.now()
        self.assertEqual(Occurrence.objects.count(), starting_record_count+1)  # test that one record has been added
        self.assertEqual(new_occurrence.date_last_modified.day, now.day)  # test date last modified is correct
        self.assertEqual(new_occurrence.point_x(), 40.8352906016)
        self.assertEqual(new_occurrence.point_y(), 11.5303732536)

    def test_mlp_create_method(self):
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

    def test_mlp_create_method_invalid_item_type(self):
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

    def test_mlp_save_method_valid_item_type(self):
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

    def test_mlp_save_method_invalid_item_type(self):
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


class MilleLogyaViews(TestCase):
    fixtures = [
        'base/fixtures/fiber_test_data_150403.json',
        'taxonomy/fixtures/taxonomy_test_data_150403.json',
        'mlp/fixtures/mlp_test_data_150406.json'
    ]

    def test_upload_view(self):
        response = self.client.get(reverse('mlp:mlp_upload_kml'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Upload a kml")

    def test_confirmation_view(self):
        response = self.client.get(reverse('mlp:mlp_upload_confirmation'))
        self.assertEqual(response.status_code, 200)

    def test_download_view(self):
        response = self.client.get(reverse('mlp:mlp_download_kml'))
        self.assertEqual(response.status_code, 200)

    def test_kml_form_with_no_data(self):
        # get starting count of records in DB
        occurrence_starting_record_count = Occurrence.objects.count()
        self.assertEqual(occurrence_starting_record_count, 87)

        # create an empty form
        post_dict = {}
        file_dict = {}
        form = UploadKMLForm(post_dict, file_dict)

        # test that form is not valid with empty data
        self.assertFalse(form.is_valid())

        # get the post response and test page reload and error message
        response = self.client.post(reverse('mlp:mlp_upload_kml'), file_dict, follow=True)
        self.assertEqual(response.status_code, 200)  # test reload
        self.assertContains(response, 'Upload a')
        self.assertContains(response, 'This field is required')

        # test nothing is saved to DB
        self.assertEqual(Occurrence.objects.count(), occurrence_starting_record_count)

    def test_kml_upload_form_with_with_valid_data(self):
        """
        Test the import kml form. This test uses a sample kmz file with one placemark.
        This code based on stack overflow question at
        http://stackoverflow.com/questions/7304248/writing-tests-for-forms-in-django
        :return:
        """
        upload_file = open('mlp/fixtures/MLP_test.kmz', 'rb')
        post_dict = {}
        file_dict = {'kmlfileUpload': SimpleUploadedFile(upload_file.name, upload_file.read())}
        upload_file.close()
        form = UploadKMLForm(post_dict, file_dict)
        self.assertTrue(form.is_valid())

        # get current number of occurrence records in DB and verify count
        occurrence_starting_record_count = Occurrence.objects.count()
        self.assertEqual(occurrence_starting_record_count, 87)

        # follow redirect to confirmation page
        response = self.client.post('/mlp/upload/', file_dict, follow=True)

        # test redirect to confirmation page
        self.assertRedirects(response, '/mlp/confirmation/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'upload was successful!')  # test message in conf page

        # test that new occurence was added to DB
        self.assertEqual(Occurrence.objects.count(), occurrence_starting_record_count+1)