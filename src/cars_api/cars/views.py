from rest_framework.generics import ListCreateAPIView, DestroyAPIView, CreateAPIView

from cars.models import Car, Rate
from cars.serializers import CarSerializer, RateSerializer


class CarsListCreateView(ListCreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class CarsDestroyView(DestroyAPIView):
    queryset = Car.objects
    serializer_class = CarSerializer


class RateCreateView(CreateAPIView):
    queryset = Rate.objects
    serializer_class = RateSerializer