from django.db import models


class Category(models.Model):
    """Category"""
    name = models.CharField('Категория', max_length=150)
    description = models.TextField('Описание')
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Product(models.Model):
    """Product"""
    title = models.CharField('Название', max_length=150)
    description = models.TextField('Описание')
    price = models.PositiveIntegerField('Цена', default=0)
    image = models.ImageField('Изображение', upload_to='products/')
    url = models.SlugField(max_length=160, unique=True)
    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
