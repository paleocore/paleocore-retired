from django.test import TestCase
from data.models import Project
from django.core.urlresolvers import reverse


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
    fixtures = ['fixtures/fiber_test_data.json']

    def test_data_index_view(self):
        """
        Index view should show fiber content and a list of projects in the nav bar
        """
        response = self.client.get(reverse('data:index'))  # get the index page
        self.assertEqual(response.status_code, 200)  # status code should be 200
        self.assertContains(response, "Dikika Research Project")
        self.assertContains(response, "Mille-Logya Research Project")


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