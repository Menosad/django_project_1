# Generated by Django 5.0.6 on 2024-07-11 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0010_version"),
    ]

    operations = [
        migrations.AlterField(
            model_name="version",
            name="number",
            field=models.PositiveIntegerField(
                blank=True, default=0, null=True, verbose_name="номер"
            ),
        ),
    ]
