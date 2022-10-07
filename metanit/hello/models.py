from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
class Scholl(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()

class Cbr_data(models.Model):
    NumCode = models.CharField(max_length=3)
    CharCode = models.CharField(max_length=3)
    Nominal = models.CharField(max_length=10)
    Name = models.CharField(max_length=100)
    Value = models.DecimalField(max_digits=10, decimal_places=2)
    DateIn = models.CharField(max_length=10)

