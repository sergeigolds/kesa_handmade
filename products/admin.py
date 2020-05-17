from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Product, Category, Images

admin.site.site_title = 'Natalia Kesa Handmade'
admin.site.site_header = 'Natalia Kesa Handmade'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'url')
    list_display_links = ('name',)


class InlineImage(admin.TabularInline):
    model = Images


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'get_image', 'category', 'url',)
    list_filter = ('category',)
    list_display_links = ('get_image', 'title',)
    readonly_fields = ('get_image',)
    # search_fields = ('title', 'category__name',)
    inlines = [InlineImage]

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.main_photo.url} width="150" height="150"')

    get_image.short_description = 'Изображение'


# class ProductAdmin(admin.ModelAdmin):
#     list_display = ['name', 'slug', 'category', 'price', 'stock', 'available', 'created', 'updated']
#     list_filter = ['available', 'created', 'updated', 'category']
#     list_editable = ['price', 'stock', 'available']
#     prepopulated_fields = {'slug': ('name',)}
#




