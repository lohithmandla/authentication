# Generated by Django 5.0.2 on 2024-02-24 13:28

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("authapp", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="company",
            field=models.CharField(blank=True, default="aptsol", max_length=255),
        ),
    ]