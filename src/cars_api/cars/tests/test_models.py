from django.test import TestCase

from cars.models import Car


class CarsTests(TestCase):

    def test_create_car(self):
        Car.objects.create(make="Volkswagen", model="Golf")
        self.assertEqual(Car.objects.count(), 1)


class RateTests(TestCase):

    def setUp(self, *args, **kwargs):
        Car.objects.create(make="Volkswagen", model="Golf")
        return super().setUp(*args, **kwargs)

    def test_create_car_rate(self):
        car = Car.objects.get(id=1)
        Rate.objects.create(rating=5, car=car)
        self.assertEqual(Rate.objects.count(), 1)
