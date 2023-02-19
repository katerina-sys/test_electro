from django.db import models

# Create your models here.


class Trader(models.Model):
    class Meta:
        verbose_name = "Индивидуальный предприниматель"
        verbose_name_plural = "Индивидуальные предприниматели"

    first_name = models.CharField(verbose_name="Имя", max_length=50)
    last_name = models.CharField(verbose_name="Фамилия", max_length=100)
    email = models.EmailField(verbose_name="Email", unique=True)
    phone = models.CharField(verbose_name="Номер телефона", max_length=20)
    country = models.CharField(verbose_name="Страна", max_length=100)
    city = models.CharField(verbose_name="Город", max_length=50)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

