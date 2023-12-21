from django.db import models


class ItemModel(models.Model):
    name = models.CharField('Название', max_length=50, help_text='Название продукта', unique=True)
    description = models.TextField('Описание', help_text='Описание продукта')
    price = models.PositiveIntegerField('Цена', help_text='Цена продукта', default=100)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name
