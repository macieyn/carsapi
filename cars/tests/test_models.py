from django.test import TestCase

from cars.models import Car, Rate


# class CarsTests(TestCase):
#     def test_create_car(self):
#         Car.objects.create(make="Volkswagen", model="Golf")
#         self.assertEqual(Car.objects.count(), 1)


class RateTests(TestCase):
    def setUp(self):
        self.car = Car.objects.create(make="Volkswagen", model="Golf")
        return super().setUp()

    def test_create_car_rate(self):
        Rate.objects.create(rating=5, car=self.car)
        self.assertEqual(Rate.objects.count(), 1)
