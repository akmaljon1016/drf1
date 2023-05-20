from django.db import models

# Create your models here.
from django.db import models


class Employee(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    password = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)
    surname = models.CharField(max_length=30, default="new")


class Programmer(models.Model):
    name = models.CharField(max_length=30)
    skil = models.CharField(max_length=30)
