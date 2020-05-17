from django.db import models
from django.urls import reverse


class Gallery(models.Model):
    """Gallery"""
    title = models.CharField('Название', max_length=150)
    main_photo = models.ImageField('Главное фото', upload_to='gallery/')
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('gallery_details', kwargs={'slug': self.url})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Images(models.Model):
    gallery = models.ForeignKey(Gallery, default=None, related_name='images', on_delete=models.PROTECT)
    image = models.ImageField(upload_to='gallery/', blank=True)

    class Meta:
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'
