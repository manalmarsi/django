from django.db import models

# Create your models here.
from django.db import models


class Employe(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    email = models.EmailField()
<<<<<<< HEAD

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

=======

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
>>>>>>> f40ded6063f4fde36eafc1953ad440b90930e5e9
