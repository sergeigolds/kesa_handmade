from django.shortcuts import render
from django.views.generic.base import View

from .models import Gallery


class GalleryView(View):
    """Products list"""
    def get(self, request):
        gallery = Gallery.objects.all()
        return render(request, 'gallery/gallery.html', {'gallery_list': gallery})


class GalleryDetailView(View):
    """Products list"""
    def get(self, request, slug):
        gallery = Gallery.objects.get(url=slug)
        return render(request, 'gallery/single_gallery.html', {'gallery': gallery})
