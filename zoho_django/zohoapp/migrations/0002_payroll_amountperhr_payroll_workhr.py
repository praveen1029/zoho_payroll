# Generated by Django 4.2.3 on 2023-12-01 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("zohoapp", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="payroll",
            name="amountperhr",
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="payroll",
            name="workhr",
            field=models.CharField(max_length=100, null=True),
        ),
    ]