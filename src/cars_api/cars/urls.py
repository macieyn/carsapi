from django.urls import path

from cars.views import CarsListCreateView, CarsDestroyView

urlpatterns = [
    path('cars/', CarsListCreateView.as_view(), name="car_list"),
    path('cars/<int:pk>/', CarsDestroyView.as_view(), name="car_destroy")
]
