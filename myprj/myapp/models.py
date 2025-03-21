from django.db import models

# Create your models here.
from django.db import models

class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birth_date = models.DateField()
    department = models.ForeignKey('Department', on_delete=models.CASCADE)

class Department(models.Model):
    name = models.CharField(max_length=100)
