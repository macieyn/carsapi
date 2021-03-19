import requests

from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist

from rest_framework import status
from rest_framework import serializers

from cars.models import Car


class ExistInVPIC:
    def __call__(self, data):
        make = data["make"]
        model = data["model"]

        response = requests.get(
            f"https://vpic.nhtsa.dot.gov/api/vehicles/getmodelsformake/{make}?format=json"
        )
        returned_data = response.json()
        models = returned_data.get("Results")

        if not models:
            message = f"There is no car make with name {make}"
            raise serializers.ValidationError(message, status.HTTP_400_BAD_REQUEST)

        if model not in map(lambda x: x.get("Model_Name"), models):
            message = f"There is no car model with name {model} for {make}"
            raise serializers.ValidationError(message, status.HTTP_400_BAD_REQUEST)


class FitRatingScale:
    def __call__(self, data):
        rating = data["rating"]
        if not (settings.RATING_SCALE_BOTTOM <= rating <= settings.RATING_SCALE_TOP):
            message = "Rating is out of scale. Acceptable values are from " \
            f"{settings.RATING_SCALE_BOTTOM} to {settings.RATING_SCALE_TOP}"
            raise serializers.ValidationError(message, status.HTTP_400_BAD_REQUEST)


class CarIdExist:
    def __call__(self, data):
        car_id = data["car_id"]
        try:
            Car.objects.get(id=car_id)
        except ObjectDoesNotExist:
            message = f"There is no car with id={car_id}"
            raise serializers.ValidationError(message, status.HTTP_400_BAD_REQUEST)
