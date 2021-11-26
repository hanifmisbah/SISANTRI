from django.contrib import admin
from django.urls import path

from . import views
urlpatterns = [
    path('', views.index),
    path('profil/', views.profil),
    path('datapengajar/', views.datapengajar),
    path('datapengajar/<id>/deletepengajar', views.deletepengajar),
    path('datapengajar/<id>/editpengajar', views.editpengajar),
    path('datasantri/', views.datasantri),
    path('datasantri/<id>/delete', views.deletesantri),
    path('quran/', views.alquran),
    path('quran/<id>/delete', views.deletequran),
    path('quran/<id>/detail', views.detailquran),
    path('kitabkuning/', views.kitabkuning),
    # path('<id>/update/', views.update),
    # path('<id>/detail/', views.detail),
]
