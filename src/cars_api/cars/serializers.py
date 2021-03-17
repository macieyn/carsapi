from rest_framework import serializers

from cars.models import Car
from cars.validators import ExistInVPIC


class CarSerializer(serializers.ModelSerializer):

    class Meta:
        model = Car
        fields = ['make', 'model']
        validators = [ExistInVPIC()]