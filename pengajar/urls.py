from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('input_quran/', views.input_quran),
    path('input_sorogan/', views.input_sorogan),
    path('input_matan/', views.input_matan),
    path('input_bandongan/', views.input_bandongan),
    path('input_nadzom/', views.input_nadzom),
    path('pengumuman/', views.pengumuman),
    path('pngm/', views.pengumuman),
    path('input', views.input),
]
