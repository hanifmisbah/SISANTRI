from django.contrib import admin
from django.urls import path

from . import views
urlpatterns = [
    path('', views.index),
    path('profil/', views.profil),
    path('pengumuman/', views.pengumuman),
    # =========== pengajar ===================
    path('datapengajar/', views.datapengajar),
    path('datapengajar/<id>/deletepengajar', views.deletepengajar),
    path('datapengajar/<id>/editpengajar', views.editpengajar),
    # ============= santri ====================
    path('datasantri<id>/editsantri', views.editsantri),
    path('datasantri/', views.datasantri),
    path('datasantri/<id>/delete', views.deletesantri),
    path('datasantri/<id>/update', views.editsantri),
    path('quran/', views.alquran),
    path('quran/<id>/delete', views.deletequran),
    path('quran/<id>/detail', views.detailquran),
    # =============== kitab ====================
    path('datakitab/', views.datakitab),
    path('datakitab/<id>/delete', views.deletekitab)
    # path('datakitab/<id>/editkitab/', views.editkitab),
    # path('<id>/detail/', views.detail),

]
