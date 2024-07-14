from django.db import models
from django.contrib.auth.models import AbstractUser

NULLABLE = {"null": True, "blank": True}


class Category(models.Model):
    name = models.CharField(
        max_length=100, verbose_name="категория", help_text="укажите категорию"
    )
    description = models.TextField(verbose_name="описание")

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "категории"
        ordering = ("name",)


class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name="название")
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="products"
    )
    avatar = models.ImageField(
        **NULLABLE, verbose_name="картинка", upload_to="products"
    )
    price = models.IntegerField(verbose_name="цена")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="дата создания")
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name="Дата последнего изменения"
    )

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "продукт"
        verbose_name_plural = "продукты"
        ordering = (
            "name",
            "category",
        )


class Blog(models.Model):
    title = models.CharField(max_length=150, verbose_name="название")
    slug = models.CharField(max_length=100, verbose_name="slug", **NULLABLE)
    content = models.TextField(verbose_name="содежрание")
    preview = models.ImageField(upload_to="blogs", **NULLABLE, verbose_name="превью")
    created_at = models.DateTimeField(auto_now=True, verbose_name="дата создания")
    update_at = models.DateTimeField(
        auto_now_add=True, verbose_name="дата редактирования"
    )
    is_published = models.BooleanField(verbose_name="опубликовано", default=True)
    views = models.IntegerField(verbose_name="просмотры", default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "блог"
        verbose_name_plural = "блоги"


class Version(models.Model):
    name = models.CharField(max_length=150, verbose_name='название')
    number = models.PositiveIntegerField(verbose_name='номер', **NULLABLE, default=0,)
    is_current = models.BooleanField(default=True, verbose_name='действующая')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='versions')

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = 'версия'
        verbose_name_plural = 'версии'
