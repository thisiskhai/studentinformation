# Generated by Django 4.1 on 2022-11-19 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Forming",
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
                ("name", models.CharField(max_length=120)),
                ("phoneNumber", models.CharField(max_length=10)),
                ("className", models.CharField(max_length=20)),
                ("email", models.EmailField(max_length=254)),
                ("note", models.CharField(max_length=200)),
            ],
        ),
    ]
