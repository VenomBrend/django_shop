from django.test import TestCase
from cats_shop.models import Breed


class BreedTestCase(TestCase):

    def setUp(self):
        self.breed = Breed(name='breed1')

    def test_breedName(self):
        self.assertEqual(str(self.breed), 'breed1')
