# Generated by Django 4.0.7 on 2024-04-10 11:09

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("common", "0002_alter_randommodel_id"),
    ]

    operations = [
        migrations.DeleteModel(
            name="RandomModel",
        ),
    ]