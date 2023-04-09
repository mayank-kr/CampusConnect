# Generated by Django 4.1.7 on 2023-04-09 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("CampusConnectApp", "0008_cabsharing"),
    ]

    operations = [
        migrations.CreateModel(
            name="Mess",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "day",
                    models.CharField(
                        choices=[
                            ("Monday", "Monday"),
                            ("Tuesday", "Tuesday"),
                            ("Wednesday", "Wednesday"),
                            ("Thursday", "Thursday"),
                            ("Friday", "Friday"),
                            ("Saturday", "Saturday"),
                            ("Sunday", "Sunday"),
                        ],
                        max_length=10,
                    ),
                ),
                (
                    "meal",
                    models.CharField(
                        choices=[
                            ("Breakfast", "Breakfast"),
                            ("Lunch", "Lunch"),
                            ("Dinner", "Dinner"),
                        ],
                        max_length=10,
                    ),
                ),
                ("items", models.TextField(max_length=1000)),
            ],
        ),
    ]