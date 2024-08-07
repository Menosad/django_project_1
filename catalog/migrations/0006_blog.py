# Generated by Django 5.0.6 on 2024-06-28 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0005_alter_product_category"),
    ]

    operations = [
        migrations.CreateModel(
            name="Blog",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=150, verbose_name="название")),
                ("slug", models.CharField(max_length=100, verbose_name="slug")),
                ("content", models.TextField(verbose_name="содежрание")),
                (
                    "created_at",
                    models.DateTimeField(auto_now=True, verbose_name="дата создания"),
                ),
                (
                    "update_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="дата редактирования"
                    ),
                ),
                (
                    "is_published",
                    models.BooleanField(default=False, verbose_name="опубликовано"),
                ),
                ("views", models.IntegerField(default=0, verbose_name="просмотры")),
            ],
            options={
                "verbose_name": "блог",
                "verbose_name_plural": "блоги",
            },
        ),
    ]
