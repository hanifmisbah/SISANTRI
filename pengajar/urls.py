from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('input_quran/', views.input_quran),
    path('pngm/', views.pengumuman),
]
