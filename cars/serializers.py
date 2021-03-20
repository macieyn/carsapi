from rest_framework import serializers
from rest_framework import status

from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist

from cars.models import Car, Rate
from cars.helpers import get_models_for_car_make


class CarSerializer(serializers.ModelSerializer):
    avg_rating = serializers.FloatField(read_only=True)

    class Meta:
        model = Car
        fields = ["id", "make", "model", "avg_rating"]
        
    def validate(self, data):
        make = data["make"]
        model = data["model"]

        models = get_models_for_car_make(make)
        
        if not models:
            message = f"There is no car make with name {make}"
            raise serializers.ValidationError(message, 'make')
        
        if model not in map(lambda x: x.get("Model_Name"), models):
            message = f"There is no car model with name {model} for {make}"
            raise serializers.ValidationError(message, 'model')
        
        return data




class RateSerializer(serializers.ModelSerializer):
    car_id = serializers.IntegerField()

    class Meta:
        model = Rate
        fields = ["rating", "car_id"]
        
    def validate_car_id(self, value):
        try:
            Car.objects.get(id=value)
        except ObjectDoesNotExist:
            message = f"There is no car with id={value}"
            raise serializers.ValidationError(message)
        return value


class CarPopularitySerializer(serializers.ModelSerializer):
    rates_number = serializers.IntegerField()

    class Meta:
        model = Car
        fields = ["id", "make", "model", "rates_number"]
