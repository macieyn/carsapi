from rest_framework.generics import ListCreateAPIView, DestroyAPIView

from cars.models import Car
from cars.serializers import CarSerializer


class CarsListCreateView(ListCreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class CarsDestroyView(DestroyAPIView):
    queryset = Car.objects
    serializer_class = CarSerializer
