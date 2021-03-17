from django.test import TestCase


class CarsTests(TestCase):

    def test_create_car(self):
        Car.objects.create(make="Volkswagen", model="Golf")
        self.assertEqual(Car.objects.count(), 1)
