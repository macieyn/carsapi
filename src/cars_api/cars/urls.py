from django.urls import path

from cars.views import CarsListCreateView

urlpatterns = [
    path('cars/', CarsListCreateView.as_view(), name="car_list")
]
