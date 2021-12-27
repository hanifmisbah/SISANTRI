from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('<id>/detail', views.index),
    path('hasil_quran/', views.hasil_quran),
    path('hasil_bandongan/', views.hasil_bandongan),
    path('hasil_matan/', views.hasil_matan),
    path('hasil_nadzom/', views.hasil_nadzom),
    path('hasil_sorogan/', views.hasil_sorogan),
    path('hasil/', views.hasil)
]
