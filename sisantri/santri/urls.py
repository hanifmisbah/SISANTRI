from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('quran/', views.quran),
    # path('santri_quran/', views santri_quran)
]