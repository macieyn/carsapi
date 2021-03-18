from django.db.models import Count

from rest_framework.generics import ListCreateAPIView, DestroyAPIView, CreateAPIView, ListAPIView
from rest_framework import filters

from cars.models import Car, Rate
from cars.serializers import CarSerializer, RateSerializer, CarPopularitySerializer


class CarsListCreateView(ListCreateAPIView):
    queryset = Car.objects
    serializer_class = CarSerializer


class CarsDestroyView(DestroyAPIView):
    queryset = Car.objects
    serializer_class = CarSerializer


class RateCreateView(CreateAPIView):
    queryset = Rate.objects
    serializer_class = RateSerializer


class CarPopularityListView(ListAPIView):
    queryset = Car.objects
    serializer_class = CarPopularitySerializer

    def get_queryset(self):
        q = super().get_queryset()
        return q.annotate(rates_number=Count('rates')).order_by('-rates_number')
