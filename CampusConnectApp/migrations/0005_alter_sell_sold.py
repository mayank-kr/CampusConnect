# Generated by Django 4.1.7 on 2023-03-30 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("CampusConnectApp", "0004_buy"),
    ]

    operations = [
        migrations.AlterField(
            model_name="sell",
            name="sold",
            field=models.BooleanField(default=False),
        ),
    ]
