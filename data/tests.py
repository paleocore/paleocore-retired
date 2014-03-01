from django.test import TestCase
from data.models import Project
from django.core.urlresolvers import reverse

# Create your tests here.

class ProjectIndexViewTests(TestCase):
    def test_index_view_with_no_projects(self):
        """
        If no projects an appropriate mesage should be displayed
        """
        response = self.client.get(reverse('data:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No projects are available")
        self.assertQuerysetEqual(response.context['project_list'], [])

    def test_index_view_with_one_project(self):
        """
        If a project is present should list it.
        """
        create_project(title="Test Project", short_title="TP")
        response = self.client.get(reverse('data:index'))
        self.assertQuerysetEqual(
            response.context['project_list'],
            ['<Project: Test Project>']
        )