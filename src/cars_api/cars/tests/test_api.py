from rest_framework import status
from rest_framework.test import APITestCase

from cars.models import Car, Rate


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
        response = self.client.post('/cars/', {'make': 'Volkswagen', 'model': 'Jetta'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        data = response.json()
        self.assertEqual(type(data), dict)
        self.assertEqual(Car.objects.count(), 3)

    def test_post_cars_fictional_car(self):
        response = self.client.post('/cars/', {'make': 'Abbadaru', 'model': 'ZFX'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        
    def test_delete_cars(self):
        response = self.client.delete('/cars/1/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Car.objects.count(), 1)

    def test_delete_cars_not_found(self):
        response = self.client.delete('/cars/3/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class RateApiTests(APITestCase):

    def setUp(self):
        Car.objects.create(make="Volkswagen", model="Golf")
        Car.objects.create(make="Volkswagen", model="Passat")
        return super().setUp()

    def test_get_rating_not_allowed(self):
        response = self.client.get('/rate/')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_post_rating(self):
        response = self.client.post('/rate/', {"car_id" : 1, "rating" : 5}, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
