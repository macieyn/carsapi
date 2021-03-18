from django.db import models
from django.db.models import Avg

# Create your models here.


class Car(models.Model):
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)

    @property
    def avg_rating(self):
        result = self.rates.all().aggregate(Avg("rating"))
        rates_avg = result.get("rating__avg") or 0
        rates_avg = round(rates_avg, 1)
        return rates_avg


class Rate(models.Model):
    car = models.ForeignKey("Car", on_delete=models.CASCADE, related_name="rates")
    rating = models.PositiveSmallIntegerField()
