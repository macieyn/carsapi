from django.db import models

# Create your models here.

class Car(models.Model):
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)

    @property
    def avg_rating(self):
        try:
            rates = self.rate_set.all()
            return sum(rates) / rates.count()
        except ZeroDivisionError:
            return 0.0


class Rate(models.Model):
    car = models.ForeignKey("Car", on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField()
