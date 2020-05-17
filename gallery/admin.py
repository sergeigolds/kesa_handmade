from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Gallery, Images


class InlineImage(admin.TabularInline):
    model = Images


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('title', 'get_image', 'url',)
    list_display_links = ('get_image', 'title',)
    # readonly_fields = ('get_image',)
    # # search_fields = ('title', 'category__name',)
    inlines = [InlineImage]

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.main_photo.url} width="150" height="150"')

    get_image.short_description = 'Изображение'

