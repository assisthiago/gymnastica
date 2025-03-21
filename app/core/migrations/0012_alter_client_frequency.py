# Generated by Django 5.1.7 on 2025-03-21 23:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0011_client_frequency"),
    ]

    operations = [
        migrations.AlterField(
            model_name="client",
            name="frequency",
            field=models.CharField(
                choices=[
                    ("1", "1x por semana"),
                    ("2", "2x por semana"),
                    ("3", "3x por semana"),
                    ("5", "5x por semana"),
                ],
                max_length=1,
                verbose_name="frequência",
            ),
        ),
    ]
