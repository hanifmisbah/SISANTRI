from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('hasil/', views.hasil),
    path('pengasuh_quran/', views.pengasuh_quran),
    path('pengasuh_matan/', views.pengasuh_matan),
    path('pengasuh_nadzom/', views.pengasuh_nadzom),
    path('pengasuh_sorogan/', views.pengasuh_sorogan),
    path('pengasuh_bandongan/', views.pengasuh_bandongan),
]
