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


class Sell(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    roll = models.ForeignKey(Users, on_delete=models.CASCADE)
    price = models.FloatField()
    sold = models.BooleanField(default=False)


class Buy(models.Model):
    id = models.OneToOneField(Sell, on_delete=models.CASCADE, primary_key=True)
    roll = models.ForeignKey(Users, on_delete=models.CASCADE)


class Lost(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/lost')
    description = models.TextField(max_length=500)
    roll = models.ForeignKey(Users, on_delete=models.CASCADE)
