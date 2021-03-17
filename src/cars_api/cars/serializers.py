from rest_framework import serializers

from cars.models import Car, Rate
from cars.validators import ExistInVPIC


class CarSerializer(serializers.ModelSerializer):

    class Meta:
        model = Car
        fields = ['make', 'model']
        validators = [ExistInVPIC()]


class RateSerializer(serializers.ModelSerializer):
    car_id = serializers.IntegerField()

    class Meta:
        model = Rate
        fields = ['rating', 'car_id']
