from django.db import models


class Contact(models.Model):
    type_choices = [('Emergency', 'Emergency'), ('Administration',
                                                 'Administration'), ('Faculty', 'Faculty')]
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    type = models.CharField(max_length=50, choices=type_choices)


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


class Found(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/found')
    description = models.TextField(max_length=500)
    roll = models.ForeignKey(Users, on_delete=models.CASCADE)


class CabSharing(models.Model):
    id = models.AutoField(primary_key=True)
    to_address = models.CharField(max_length=500)
    from_address = models.CharField(max_length=500)
    roll = models.ForeignKey(Users, on_delete=models.CASCADE)
    time = models.DateTimeField()


class Mess(models.Model):
    day_choices = [('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'),
                   ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('Saturday', 'Saturday'), ('Sunday', 'Sunday')]
    meal_choices = [('Breakfast', 'Breakfast'),
                    ('Lunch', 'Lunch'), ('Dinner', 'Dinner')]
    day = models.CharField(max_length=10, choices=day_choices)
    meal = models.CharField(max_length=10, choices=meal_choices)
    items = models.TextField(max_length=1000)


class Restaurants(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    cuisine = models.CharField(max_length=100)
    distance = models.FloatField()
    price = models.CharField(max_length=100)
