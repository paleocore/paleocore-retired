from django.test import TestCase
from data.models import Project
from django.core.urlresolvers import reverse
from schema.models import Term, Project


# # Factory method to create a fiber page tree with five pages.
# def create_django_page_tree():
#     mainmenu=Page(title='mainmenu')
#     mainmenu.save()
#     home=Page(title='home', parent=mainmenu, url='home', template_name='base/home.html')
#     home.save()
#     join=Page(title='join', parent=home, url='join', template_name='base/join.html')
#     join.save()
#     members=Page(title='members', parent=home, url='members', template_name='base/members')
#     members.save()
#     meetings = Page(title='meetings', parent=mainmenu, url='meetings', template_name='')
#     meetings.save()


class ProjectIndexViewTests(TestCase):
    fixtures = ['fixtures/fiber_data_140530.json', 'fixtures/schema_data_140530.json']

    def test_data_index_view(self):
        """
        Index view should show fiber content and a list of projects in the nav bar
        """
        response = self.client.get(reverse('data:index'))  # get the index page
        self.assertEqual(response.status_code, 200)  # status code should be 200
        self.assertContains(response, "Dikika Research Project")
        self.assertContains(response, "Mille-Logya Research Project")

    def test_drp_term_view(self):
        """
        The view at data/drp/terms should include a list of the terms used in the drp terms database
        """
        # sanity checks for url, and data
        self.assertEqual(reverse('data:terms_index', kwargs={"project_name": "drp"}), "/data/drp/terms/")
        drp = Project.objects.get(name__exact="drp") # check existence of the project in the test db
        drp_terms = Term.objects.filter(project__exact=drp) # check the existence of the terms in the test db
        self.assertEqual(drp_terms.count(), 39)  # There should be something like 39 terms associated with the drp

        response = self.client.get(reverse('data:terms_index', kwargs={"project_name": "drp"}))
        self.assertEqual(response.status_code, 200)  # status code should be 200
        self.assertContains(response, "<h3>barcode</h3>")
        self.assertContains(response, "<h3>catalogNumber</h3>")

    def test_mlp_term_view(self):
        """
        The view at /data/mlp/terms/ should return 404 for now
        """
        self.assertEqual(reverse('data:terms_index', kwargs={"project_name": "mlp"}), "/data/mlp/terms/")
        response = self.client.get(reverse('data:terms_index', kwargs={"project_name": "mlp"}))
        self.assertEqual(response.status_code, 404)  # status code should be 400

    def test_turkana_term_view(self):
        """
        The view at /data/turkana/terms/ should return 404 for now
        """
        self.assertEqual(reverse('data:terms_index', kwargs={"project_name": "turkana"}), "/data/turkana/terms/")
        response = self.client.get(reverse('data:terms_index', kwargs={"project_name": "turkana"}))
        self.assertEqual(response.status_code, 404)  # status code should be 400


    # def test_index_view_with_no_projects(self):
    #     """
    #     If no projects an appropriate message should be displayed
    #     """
    #     response = self.client.get(reverse('data:index'))
    #     self.assertEqual(response.status_code, 200)
    #     #self.assertContains(response, "No projects are available")
    #     #self.assertQuerysetEqual(response.context['project_list'], [])
    #
    # def test_index_view_with_one_project(self):
    #     """
    #     If a project is present should list it.
    #     """
    #     create_project(title="Test Project", short_title="TP")
    #     response = self.client.get(reverse('data:index'))
    #     self.assertQuerysetEqual(
    #         response.context['project_list'],
    #         ['<Project: Test Project>']
    #     )