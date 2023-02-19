# Generated by Django 4.1.2 on 2023-02-19 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("factory", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="factory",
            name="debt",
            field=models.FloatField(
                blank=True, null=True, verbose_name="Задолженность перед поставщиком"
            ),
        ),
    ]