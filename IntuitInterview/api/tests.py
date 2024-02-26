import django
from django.test import TestCase
from django.test import Client

from api.models import Player


# Create your tests here.
class IntuitInterviewTestCase(TestCase):
    def setUp(self):
        print("This is the setup for the client")
        self.client = Client()
        pass

    @classmethod
    def setUpClass(cls):
        print("This is the setup class ")
        django.setup()
        super(IntuitInterviewTestCase, cls).setUpClass()
        Player.objects.create(playerId='1', nameFirst='firstname')

    def test_get_negative(self):
        # Wrong player ID
        response = self.client.get('/players/?playerID=abbeych01')
        self.assertEqual(response.status_code, 400)

    # did't have time to cerate test db and then call it to see the positive http status code

class TestModel(TestCase):
    @classmethod
    def setUpClass(cls):
        super(TestModel, cls).setUpClass()
        Player.objects.create(playerId='1', nameFirst='firstname')

    def test_playerName(self):
        player = Player.objects.get(playerId='1')
        self.assertEqual(player.nameFirst, 'firstname')

    # test rest of the model here
