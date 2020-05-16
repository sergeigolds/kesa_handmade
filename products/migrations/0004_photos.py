# Generated by Django 3.0.6 on 2020-05-16 16:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20200516_1907'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
                ('additional_photo', models.ImageField(upload_to='products_additional/', verbose_name='Дополнительное фото')),
                ('url', models.SlugField(max_length=160, unique=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Product', verbose_name='Продукт')),
            ],
            options={
                'verbose_name': 'Дополнительная фотография',
                'verbose_name_plural': 'Дополнительные фотографии',
            },
        ),
    ]
