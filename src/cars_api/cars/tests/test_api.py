from django.test import TestCase

from cars.models import Car


class CarsApiTests(TestCase):

    def setUp(self, *args, **kwargs):
        Car.objects.create(make="Volkswagen", model="Golf")
        Car.objects.create(make="Volkswagen", model="Passat")

    def test_get_cars(self):
        response = self.client.get('/cars/')
        data = response.json()
        self.assertEqual(len(data), 2)
        