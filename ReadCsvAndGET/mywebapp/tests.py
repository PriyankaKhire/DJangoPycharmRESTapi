from django.test import TestCase
from django.urls import reverse

from mywebapp.models import Alphabets

# Create your tests here.
class TestCsvAndGET(TestCase):

    def setUp(self):
        print("setUp: Setting up clean data")
        pass

    def tearDown(self):
        print("tearDown: Tearing down the data")
        pass

    @classmethod
    def setUpTestData(cls):
        print("setUpTestData: Setting up test data for all class methods")
        pass

    def test_firstTest(self):
        print("test_firstTest: This is the first test here")
        self.assertEqual(True, True)

class TestDataModels(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create some fake data
        Alphabets.objects.create(id=1, name="Alphabet")

    def test_id(self):
        alphabet = Alphabets.objects.get(id=1)
        self.assertEqual(alphabet.id, 1)

    def test_name(self):
        alphabet = Alphabets.objects.get(id=1)
        self.assertEqual(alphabet.name, "Alphabet")

class TestViews(TestCase):
    @classmethod
    def setUpTest(cls):
        Alphabets.objects.create(id=1, name="Alphabet1")
        Alphabets.objects.create(id=2, name="Alphabet2")
        Alphabets.objects.create(id=3, name="Alphabet3")

    def test_get_myWebAppView(self):
        response = self.client.get('/mywebapp/')
        self.assertEqual(response.status_code, 200)

    def test_get_getAllNamesView(self):
        response = self.client.get('/mywebapp/getAllAlphabets')
        self.assertEqual(response.status_code, 200)

    def test_get_getAlphabetByIdView(self):
        response = self.client.get('/mywebapp/getNameById')
        self.assertEqual(response.status_code, 400)

