from django.urls import path
from django.views.generic import TemplateView

from rest_framework.schemas import get_schema_view

from cars.views import (
    CarsListCreateView,
    CarsDestroyView,
    RateCreateView,
    CarPopularityListView,
)


urlpatterns = [
    path("cars/", CarsListCreateView.as_view(), name="car_list"),
    path("cars/<int:pk>/", CarsDestroyView.as_view(), name="car_destroy"),
    path("rate/", RateCreateView.as_view(), name="rate_create"),
    path("popular/", CarPopularityListView.as_view(), name="car_popularity"),
    path('openapi/', get_schema_view(
        title="Cars API",
        description="API for rating cars.",
        version="1.0.0"
    ), name='openapi-schema'),
    path('', TemplateView.as_view(
        template_name='swagger-ui.html',
        extra_context={'schema_url':'openapi-schema'}
    ), name='swagger-ui'),
]
