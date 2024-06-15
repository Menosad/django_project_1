from django.db import models

NULLABLE = {'null': True, 'blank': True}


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='категория',
                            help_text='укажите категорию')
    description = models.TextField(verbose_name='описание')

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = ('name',)


class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name='название')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='Category')
    avatar = models.ImageField(**NULLABLE, verbose_name='картинка', upload_to='products')
    price = models.IntegerField(verbose_name='цена')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата последнего изменения')
    #manufactured_at = models.DateTimeField(verbose_name='Дата производства продукта', **NULLABLE)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        ordering = ('name', 'category',)
