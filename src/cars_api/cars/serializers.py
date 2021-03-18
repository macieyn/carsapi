from rest_framework import serializers

from cars.models import Car, Rate
from cars.validators import ExistInVPIC, FitRatingScale


class CarSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    avg_rating = serializers.FloatField(read_only=True)

    class Meta:
        model = Car
        fields = ['id', 'make', 'model', 'avg_rating']
        validators = [ExistInVPIC()]


class RateSerializer(serializers.ModelSerializer):
    car_id = serializers.IntegerField()

    class Meta:
        model = Rate
        fields = ['rating', 'car_id']
        validators = [FitRatingScale()]


class CarPopularitySerializer(serializers.ModelSerializer):
    rates_number = serializers.IntegerField()

    class Meta:
        model = Car
        fields = ['id', 'make', 'model', 'rates_number']
