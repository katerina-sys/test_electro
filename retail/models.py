from django.db import models


# Create your models here.
from trader.models import Trader


class Retail(models.Model):
    class Meta:
        verbose_name = "Магазин"
        verbose_name_plural = "Магазины"

    title = models.CharField(verbose_name="Название", max_length=250, unique=True)
    email = models.EmailField(verbose_name="email", unique=True)
    country = models.CharField(verbose_name="Страна", max_length=100)
    city = models.CharField(verbose_name="Город", max_length=50)
    street = models.CharField(verbose_name="Улица", max_length=70)
    house_number = models.IntegerField(verbose_name="Номер дома")
    debt = models.FloatField(verbose_name="Задолженность перед поставщиком", blank=True, null=True)

    def __str__(self):
        return self.title


class Contractor(models.Model):
    class Meta:
        verbose_name = "Поставщик"
        verbose_name_plural = "Поставщики"

    first_name = models.CharField(verbose_name="Имя", max_length=50)
    last_name = models.CharField(verbose_name="Фамилия", max_length=100)
    email = models.EmailField(verbose_name="Email", unique=True)
    phone = models.CharField(verbose_name="Номер телефона", max_length=20)
    retail_id = models.ForeignKey(Retail, on_delete=models.CASCADE)
    trader_id = models.ForeignKey(Trader, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Seller(models.Model):
    class Meta:
        verbose_name = "Сотрудник"
        verbose_name_plural = "Сотрудники"

    first_name = models.CharField(verbose_name="Имя", max_length=50)
    last_name = models.CharField(verbose_name="Фамилия", max_length=100)
    phone = models.CharField(verbose_name="Номер телефона", max_length=20)
    email = models.EmailField(verbose_name="Email", unique=True)
    is_active = models.BooleanField(default=True)
    retail_id = models.ForeignKey(Retail, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"




