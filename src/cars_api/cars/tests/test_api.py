from rest_framework import status
from rest_framework.test import APITestCase

from cars.models import Car


class CarsApiTests(APITestCase):

    def setUp(self, *args, **kwargs):
        Car.objects.create(make="Volkswagen", model="Golf")
        Car.objects.create(make="Volkswagen", model="Passat")

    def test_get_cars(self):
        response = self.client.get('/cars/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.json()
        self.assertEqual(len(data), 2)

    def test_post_cars(self):
        response = self.client.post('/cars/', {'make': 'Volkswagen', 'model': 'Polo'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        data = response.json()
        self.assertEqual(type(data), dict)
        self.assertEqual(Car.objects.count(), 3)

        