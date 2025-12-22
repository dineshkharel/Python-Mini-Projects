from django.db import models


# Create your models here.
class Employee(models.Model):
    full_name = models.CharField(max_length=20)
    email = models.CharField(unique=True)
    age = models.IntegerField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)


def __str__(self):
    return self.full_name
