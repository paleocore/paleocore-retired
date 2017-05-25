"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""
from django.contrib.auth.models import User
from .models import PaleocoreUser

from django.test import TestCase
from django.core.urlresolvers import reverse


class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)

class PaleocoreUserTests(TestCase):
    def test_paleocore_user_creation(self):
        starting_user_count = PaleocoreUser.objects.count()
        self.assertEqual(starting_user_count, 0)
        new_user = User.objects.create(username='testuser', password='secret', first_name='Test', last_name='User')
        new_paleo_user=PaleocoreUser.objects.create(user=new_user, institution="Someplace University")
        self.assertEqual(PaleocoreUser.objects.count(), starting_user_count+1)
        self.assertEqual(new_paleo_user.user.email, '')

class HomePageViews(TestCase):
    fixtures = ['fixtures/fiber_data_150611.json', ]

    def test_home_page_view(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    # def test_about_page_view(self):
    #     response = self.client.get('/about/')
    #     self.assertEqual(response.status_code, 200)

