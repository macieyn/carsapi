from rest_framework import serializers

from cars.models import Car, Rate
from cars.validators import ExistInVPIC


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

class CarPopularitySerializer(serializers.ModelSerializer):

    class Meta:
        model = Car
        fields = ['id', 'make', 'model', 'rates_number']
