# Generated by Django 4.2.3 on 2023-12-05 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("zohoapp", "0007_loan_user"),
    ]

    operations = [
        migrations.AddField(
            model_name="loan",
            name="bank_id",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]