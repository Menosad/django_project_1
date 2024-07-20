# Generated by Django 5.0.6 on 2024-07-20 11:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0014_alter_product_options_product_is_published"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="blog",
            options={
                "permissions": [
                    ("set_published", "Может редактировать статус публикации")
                ],
                "verbose_name": "блог",
                "verbose_name_plural": "блоги",
            },
        ),
        migrations.AlterModelOptions(
            name="product",
            options={
                "ordering": ("name", "category"),
                "permissions": [
                    ("set_published", "Может редактировать статус публикации")
                ],
                "verbose_name": "продукт",
                "verbose_name_plural": "продукты",
            },
        ),
    ]
