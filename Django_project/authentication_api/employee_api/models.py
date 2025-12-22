from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=20)
    age= models.IntegerField(max_length=100)
    email= models.EmailField()
    position= models.CharField(max_length=40)
    created_at= models.DateTimeField(auto_now_add=True)
