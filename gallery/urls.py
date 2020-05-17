from django.urls import path
from . import views

urlpatterns = [
    path('', views.GalleryView.as_view()),
    path('<slug:slug>/', views.GalleryDetailView.as_view(), name='gallery_details'),
    ]
