# Generated by Django 4.1.2 on 2023-02-19 08:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Retail",
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
                    "title",
                    models.CharField(
                        max_length=250, unique=True, verbose_name="Название"
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        max_length=254, unique=True, verbose_name="email"
                    ),
                ),
                ("country", models.CharField(max_length=100, verbose_name="Страна")),
                ("city", models.CharField(max_length=50, verbose_name="Город")),
                ("street", models.CharField(max_length=70, verbose_name="Улица")),
                ("house_number", models.IntegerField(verbose_name="Номер дома")),
            ],
            options={
                "verbose_name": "Магазин",
                "verbose_name_plural": "Магазины",
            },
        ),
        migrations.CreateModel(
            name="Seller",
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
                ("first_name", models.CharField(max_length=50, verbose_name="Имя")),
                ("last_name", models.CharField(max_length=100, verbose_name="Фамилия")),
                (
                    "phone",
                    models.CharField(max_length=20, verbose_name="Номер телефона"),
                ),
                (
                    "email",
                    models.EmailField(
                        max_length=254, unique=True, verbose_name="Email"
                    ),
                ),
                ("is_active", models.BooleanField(default=True)),
                (
                    "retail_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="retail.retail"
                    ),
                ),
            ],
            options={
                "verbose_name": "Сотрудник",
                "verbose_name_plural": "Сотрудники",
            },
        ),
        migrations.CreateModel(
            name="Contractor",
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
                ("first_name", models.CharField(max_length=50, verbose_name="Имя")),
                ("last_name", models.CharField(max_length=100, verbose_name="Фамилия")),
                (
                    "email",
                    models.EmailField(
                        max_length=254, unique=True, verbose_name="Email"
                    ),
                ),
                (
                    "phone",
                    models.CharField(max_length=20, verbose_name="Номер телефона"),
                ),
                (
                    "retail_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="retail.retail"
                    ),
                ),
            ],
            options={
                "verbose_name": "Поставщик",
                "verbose_name_plural": "Поставщики",
            },
        ),
    ]