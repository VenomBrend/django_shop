from django.test import TestCase
from cats_shop.models import Breed, Cat, CatColor
from django.utils import timezone

# Create your tests here.


class TestURLs(TestCase):

    def test_index(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_register(self):
        response = self.client.get('/register/')
        self.assertEqual(response.status_code, 200)

    def test_login(self):
        response = self.client.get('/login/')
        self.assertEqual(response.status_code, 200)

    def test_logout(self):
        response = self.client.get('/logout/')
        self.assertEqual(response.status_code, 302)

    def test_catDetails(self):
        test_breed = Breed(name='breed1')
        test_breed.save()
        test_color = CatColor(name='color1')
        test_color.save()

        test_cat = Cat(breed=test_breed, sex=1,
                       cat_color=test_color, date=timezone.now(),
                       price=100.00)
        test_cat.save()

        response = self.client.get('/cat/{0}'.format(test_cat.id))
        self.assertEqual(response.status_code, 200)

    def test_checkout(self):
        response = self.client.get('/checkout/')
        self.assertEqual(response.status_code, 200)
