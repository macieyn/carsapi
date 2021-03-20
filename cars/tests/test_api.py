from rest_framework import status
from rest_framework.test import APITestCase

from cars.models import Car, Rate


class CarsApiTests(APITestCase):
    def setUp(self, *args, **kwargs):
        self.car = Car.objects.create(make="Volkswagen", model="Golf")
        Car.objects.create(make="Volkswagen", model="Passat")
        Rate.objects.create(car=self.car, rating=5)
        return super().setUp()

    def test_get_cars(self):
        response = self.client.get("/cars/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_cars(self):
        response = self.client.post(
            "/cars/", {"make": "Volkswagen", "model": "Jetta"}, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        data = response.json()
        self.assertEqual(type(data), dict)
        self.assertEqual(Car.objects.count(), 3)

    def test_delete_cars(self):
        response = self.client.delete(f"/cars/{self.car.id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Car.objects.count(), 1)

    def test_delete_cars_not_found(self):
        response = self.client.delete("/cars/3/")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_correct_keys_in_response_payload(self):
        response = self.client.get("/cars/")
        data = response.json()
        self.assertEqual(len(data), 2)

        keys = data[0].keys()
        self.assertEqual(len(keys), 4)
        self.assertIn("id", keys)
        self.assertIn("make", keys)
        self.assertIn("model", keys)
        self.assertIn("avg_rating", keys)

    def test_post_cars_fictional_car(self):
        response = self.client.post(
            "/cars/", {"make": "Abbadaru", "model": "ZFX"}, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class RateApiTests(APITestCase):
    def setUp(self):
        self.car = Car.objects.create(make="Volkswagen", model="Golf")
        Car.objects.create(make="Volkswagen", model="Passat")
        return super().setUp()

    def test_get_rating_not_allowed(self):
        response = self.client.get("/rate/")
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_post_rating(self):
        response = self.client.post(
            "/rate/", {"car_id": self.car.id, "rating": 5}, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_put_rating_not_allowed(self):
        response = self.client.put("/rate/")
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_patch_rating_not_allowed(self):
        response = self.client.patch("/rate/")
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_delete_rating_not_allowed(self):
        response = self.client.delete("/rate/")
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_post_rating_out_of_scale(self):
        response = self.client.post(
            "/rate/", {"car_id": self.car.id, "rating": 6}, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_post_rating_wrong_car_id(self):
        response = self.client.post(
            "/rate/", {"car_id": 99, "rating": 5}, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class CarPopularityApiTests(APITestCase):
    def setUp(self):
        car = Car.objects.create(make="Volkswagen", model="Passat")
        Car.objects.create(make="Volkswagen", model="Golf")
        Rate.objects.create(car=car, rating=5)
        return super().setUp()

    def test_get_popular_cars(self):
        response = self.client.get("/popular/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_rating_not_allowed(self):
        response = self.client.post("/popular/")
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_put_rating_not_allowed(self):
        response = self.client.put("/popular/")
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_patch_rating_not_allowed(self):
        response = self.client.patch("/popular/")
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_delete_rating_not_allowed(self):
        response = self.client.delete("/popular/")
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_correct_keys_in_response_payload(self):
        response = self.client.get("/popular/")
        data = response.json()
        self.assertEqual(len(data), 2)

        keys = data[0].keys()
        self.assertEqual(len(keys), 4)
        self.assertIn("id", keys)
        self.assertIn("model", keys)
        self.assertIn("make", keys)
        self.assertIn("rates_number", keys)
