from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    # ========= Q U R A N ===========
    path('input_quran/', views.input_quran),
    path('pengajar_input_quran/<id>/deletequran', views.deletequran),
    # ========== S O R O G A N =========
    path('input_sorogan/', views.input_sorogan),
    path('pengajar_input_sorogan/<id>/deletesorogan', views.deletesorogan),
    # ============ M A T A N ============
    path('input_matan/', views.input_matan),
    path('pengajar_input_matan/<id>/deletematan', views.deletematan),
    # ========== B A N D O N G A N ===============
    path('input_bandongan/', views.input_bandongan),
    path('pengajar_input_bandongan/<id>/deletebandongan', views.deletebandongan),
    # ============= N A D Z O M =================
    path('input_nadzom/', views.input_nadzom),
    path('pengajar_input_nadzom/<id>/deletenadzom', views.deletenadzom),
    # ========== P E N G U M U M A N ===============
    path('pengumuman/', views.pengumuman),
    path('pngm/', views.pengumuman),
    path('input', views.input),

]
