from django.db import models


# Create your models here.
from retail.models import Contractor


class DatesModelMixin(models.Model):
    class Meta:
        abstract = True  # Помечаем класс как абстрактный – для него не будет таблички в БД

    created = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    updated = models.DateTimeField(verbose_name='Дата последнего обновления', auto_now=True)


class Factory(models.Model):
    class Meta:
        verbose_name_plural = "Завод"

    title = models.CharField(verbose_name="Название", max_length=250, unique=True)
    email = models.EmailField(verbose_name="email", unique=True)
    country = models.CharField(verbose_name="Страна", max_length=100)
    city = models.CharField(verbose_name="Город", max_length=50)
    street = models.CharField(verbose_name="Улица", max_length=70)
    house_number = models.IntegerField(verbose_name="Номер дома")
    debt = models.FloatField(verbose_name="Задолженность перед поставщиком", blank=True, null=True)
    contractor_id = models.ForeignKey(Contractor, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.title


class Products(DatesModelMixin):
    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

    factory_id = models.ForeignKey(Factory, on_delete=models.CASCADE)
    title = models.CharField(verbose_name="Название", max_length=150, unique=True)
    description = models.CharField(verbose_name="Описание", blank=True, null=True, max_length=250)
    model = models.IntegerField(verbose_name="Номер модели", unique=True)
    price = models.PositiveIntegerField()
    contractor_id = models.ForeignKey(Contractor, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
