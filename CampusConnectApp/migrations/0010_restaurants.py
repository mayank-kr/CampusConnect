# Generated by Django 4.1.7 on 2023-04-09 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("CampusConnectApp", "0009_mess"),
    ]

    operations = [
        migrations.CreateModel(
            name="Restaurants",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=100)),
                ("cuisine", models.CharField(max_length=100)),
                ("distance", models.FloatField()),
                ("price", models.CharField(max_length=100)),
            ],
        ),
    ]
