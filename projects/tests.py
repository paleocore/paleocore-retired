from django.test import TestCase
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from .models import Project
from mlp.models import Occurrence, Biology
from django.contrib.gis.geos import Point
from taxonomy.models import Taxon, IdentificationQualifier
from mysite.ontologies import BASIS_OF_RECORD_VOCABULARY, COLLECTOR_CHOICES, ITEM_TYPE_VOCABULARY
from random import random
from datetime import datetime


class ProjectViewsEmptyDB(TestCase):
    """
    Test PaleoCore project app with empty project table
    """
    fixtures = ['fixtures/fiber_data_150611.json', 'taxonomy/fixtures/taxonomy_data_150611.json']

    def test_index_view_with_empty_database(self):
        response = self.client.get('/projects/')  # expected url
        self.assertEqual(response.status_code, 200)
        response = self.client.get(reverse('projects:index'))  # reverse lookup
        self.assertEqual(response.status_code, 200)

        self.assertContains(response, "There are no projects to display")  # Test empty project list message
        self.assertEqual(len(response.context['project_list']), 0)  # number of projects returned to page
        self.assertContains(response, "leaflet-container")  # leaflet map


class ProjectMethodsTests(TestCase):
    """
    Test PaleoCore Project instance creation and methods
    """

    fixtures = ['fixtures/fiber_data_150611.json', 'taxonomy/fixtures/taxonomy_data_150611.json']

    def setUp(self):
        # Populate User table
        # Create a user.
        self.username = 'youzer'
        self.password = 'pass'
        self.user = User.objects.create_user(self.username, 'youzer@example.com', self.password)

        # Populate projects table
        starting_record_count = Project.objects.count()  # get current record count

        Project.objects.create(
            full_name="Dikika Research Project",
            short_name="drp",
            abstract="The San Francisco project is a public demonstration database.",
            attribution="This project was created by the PaleoCore development team.",
            paleocore_appname="san_francisco",
            occurrence_table_name="Occurrence",
            display_fields="""["id", "barcode", "catalog_number", "item_scientific_name", "item_description", "item_type"]""",
            display_filter_fields="""["item_type"]""",
            geom=Point(41.0, 11.0)
        )

        Project.objects.create(
            full_name="San Francisco (Demo)",
            short_name="san_francisco",
            abstract="The Dikika Research Project (DRP) studies Pliocene hominins and paleoenvironments. ",
            attribution="The project is lead by Dr. Zeray Alemseged of the California Academy of Sciences.",
            paleocore_appname="drp",
            occurrence_table_name="Occurrence",
            display_fields="""["id", "collection_code","paleolocality_number","item_number","item_part",'stratigraphic_member',"barcode", 'basis_of_record',
                    "item_scientific_name", "item_description","year_collected"]""",
            display_filter_fields="""["basis_of_record", "year_collected", "stratigraphic_member", "collection_code", "item_type"]""",
            geom=Point(-122.4, 37.8)
        )
        self.assertEqual(Project.objects.count(), starting_record_count+2)

        Project.objects.create(
            full_name="Turkana Database",
            short_name="turkana",
            abstract="The Turkana Database contains information on fossil collections from the Turkana Basin.",
            attribution="These data have previously been made available",
            paleocore_appname="turkana",
            occurrence_table_name="Turkana",
            display_fields="""('year_found', 'study_area', 'formation', 'member', 'genus', 'species')""",
            display_filter_fields="""["study_area", "formation", "body_element", "genus"]""",
            is_public=True,
            display_summary_info=True,
            geom=Point(36.3, 4.2)
        )
        self.assertEqual(Project.objects.count(), starting_record_count+3)

        Project.objects.create(
            full_name="Dublin Core",
            short_name="Dublin Core",
            abstract="The Dublin Core Metadata Initiative",

            paleocore_appname="projects",
            display_fields="""['id',]""",
            display_filter_fields="""[]""",
            is_public=False,
            display_summary_info=False,
            website="http://dublincore.org",
            geographic="Global"
        )
        self.assertEqual(Project.objects.count(), starting_record_count+4)

        # Populate mlp occurrence table
        id_qualifier = IdentificationQualifier.objects.get(name__exact="None")
        barcode_index = 1
        mammal_orders = (("Primates", "Primates"),
                         ("Perissodactyla", "Perissodactyla"),
                         ("Artiodactyla", "Artiodactyla"),
                         ("Rodentia", "Rodentia"),
                         ("Carnivora", "Carnivora"),)

        for basis_tuple_element in BASIS_OF_RECORD_VOCABULARY:
            for collector_tuple_element in COLLECTOR_CHOICES:
                for order_tuple_element in mammal_orders:
                    Biology.objects.create(
                        barcode=barcode_index,
                        basis_of_record=basis_tuple_element[0],
                        collection_code="MLP",
                        item_number=barcode_index,
                        geom=Point(-122+random(), 37+random()),
                        taxon=Taxon.objects.get(name__exact=order_tuple_element[0]),
                        identification_qualifier=id_qualifier,
                        field_number=datetime.now(),
                        collecting_method="Surface Standard",
                        collector=collector_tuple_element[0],
                        item_type="Faunal"
                    )
                    barcode_index += 1

        for basis_tuple_element in BASIS_OF_RECORD_VOCABULARY:
            for item_type_element in ITEM_TYPE_VOCABULARY:
                Occurrence.objects.create(
                    barcode=barcode_index,
                    basis_of_record=basis_tuple_element[0],
                    collection_code="MLP",
                    item_number=barcode_index,
                    geom=Point(-122+random(), 37+random()),
                    field_number=datetime.now(),
                    collecting_method="Surface Standard",
                    collector="Denne Reed",
                    item_type=item_type_element[0]
                )
                barcode_index += 1

        total_permutations = len(BASIS_OF_RECORD_VOCABULARY) * \
                             len(COLLECTOR_CHOICES * len(mammal_orders))
        self.assertEqual(Biology.objects.all().count(), total_permutations)
        self.assertEqual(Biology.objects.filter(basis_of_record__exact="FossilSpecimen").count(),
                         total_permutations/len(BASIS_OF_RECORD_VOCABULARY))
        object1 = Biology.objects.get(barcode=1)
        object2 = Biology.objects.get(barcode=2)
        self.assertNotEqual(object1.geom.x, object2.geom.x)
        self.assertNotEqual(object1.geom.y, object2.geom.y)
        self.assertEqual(object1.collecting_method, "Surface Standard")

    def test_project_index_view(self):
        response = self.client.get('/projects/')  # expected url
        self.assertEqual(response.status_code, 200)
        response = self.client.get(reverse('projects:index'))  # reverse lookup
        self.assertEqual(response.status_code, 200)

        self.assertContains(response, "Dikika")  # Dikika project title
        self.assertContains(response, "San Francisco")  # San Francisco project title
        self.assertContains(response, "Turkana Database")  # Turkaa project title
        self.assertEqual(len(response.context['project_list']), 3)  # number of projects returned to page
        self.assertContains(response, "leaflet-container")  # leaflet map

    def test_drp_project_detail_view(self):
        response = self.client.get(reverse('projects:detail', kwargs={"pcoreapp": "drp"}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "The project is lead")
        self.assertContains(response, "leaflet-container")  # leaflet map
        self.assertContains(response, "Admin Site for Project Members")  # button

    def test_san_francisco_detail_view(self):
        response = self.client.get(reverse('projects:detail', kwargs={"pcoreapp": "san_francisco"}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "This project was created")
        self.assertContains(response, "leaflet-container")  # leaflet map
        self.assertContains(response, "Admin Site for Project Members")  # button

    def test_turkana_detail_view(self):
        response = self.client.get(reverse('projects:detail', kwargs={"pcoreapp": "turkana"}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "The Turkana Database contains information on fossil")
        self.assertContains(response, "leaflet-container")  # leaflet map
        self.assertContains(response, "Admin Site for Project Members")  # button
        self.assertContains(response, "View Public Data")  # button

    def test_turkana_public_data_table_view(self):
        response = self.client.get(reverse('projects:data_table', kwargs={"pcoreapp": "turkana"}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'dataTable')

    def test_projects_geojson(self):
        response = self.client.get(reverse('projects:projects_geojson'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "FeatureCollection")  # geojson in response

    def test_turkana_project_data_json(self):
        response = self.client.get(reverse('projects:data_json',  kwargs={"pcoreapp": "turkana"}))
        self.assertEqual(response.status_code, 200)

    # This test needs some additional setup. Not sure exactly what is missing.
    # def test_mlp_project_data_json(self):
    #     response = self.client.get(reverse('projects:data_json',  kwargs={"pcoreapp": "mlp"}))
    #     self.assertEqual(response.status_code, 200)
