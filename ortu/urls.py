from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('<id>/detail', views.index),
    path('quran/', views.quran),
    path('bandongan/', views.bandongan),
    path('matan/', views.matan),
    path('nadzom/', views.nadzom),
    path('sorogan/', views.sorogan),
]
