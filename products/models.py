from django.db import models
from django.urls import reverse


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
    main_photo = models.ImageField('Главное фото', upload_to='products/')
    url = models.SlugField(max_length=160, unique=True)
    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('product_details', kwargs={'slug': self.url})

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class Photos(models.Model):
    """Test"""
    title = models.CharField('Название', max_length=150)
    description = models.TextField('Описание')
    additional_photo = models.ImageField('Дополнительное фото', upload_to='products_additional/')
    url = models.SlugField(max_length=160, unique=True)
    product = models.ForeignKey(Product, verbose_name='Продукт', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Дополнительная фотография'
        verbose_name_plural = 'Дополнительные фотографии'
