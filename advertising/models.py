from django.db import models
from datetime import timedelta


NULLABLE = {'null': True, 'blank': True}

class Advertising(models.Model):
    name = models.CharField(max_length=100, verbose_name='название')
    description = models.TextField(verbose_name='описание')
    duration = models.DurationField(default=timedelta(days=7))
    avatar = models.ImageField(upload_to='advertisings', **NULLABLE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'реклама'
