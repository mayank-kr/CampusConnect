from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    type = models.CharField(max_length=50)


class Users(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=100)
    roll = models.CharField(max_length=20, primary_key=True)
    contact = models.CharField(max_length=20)
    dept = models.CharField(max_length=10)
    batch = models.IntegerField()
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
