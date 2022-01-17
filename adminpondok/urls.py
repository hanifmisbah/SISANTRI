from django.urls import path

from . import views
urlpatterns = [
    path('coba/', views.coba),
    path('', views.index),
    path('<id>/delete', views.deletepngm),
    path('profil/', views.profil),
    # =========== pengajar ===================
    path('datapengajar/', views.datapengajar),
    path('datapengajar/<id>/deletepengajar', views.deletepengajar),
    path('datapengajar/<id>/editpengajar', views.editpengajar),
    path('datapengajar/<id>/update', views.editpengajar),
    # ============= santri ====================
    path('datasantri/', views.datasantri),
    path('datasantri/kategori', views.kategori),
    path('datasantri/level', views.level),
    path('datasantri/<id>/delete', views.deletesantri),
    path('datasantri/<id>/update', views.editsantri),
    path('datasantri/<id>/detail', views.detailsantri),
    # ============= Quran ====================
    path('quran/', views.alquran),
    path('quran/<id>/delete', views.deletequran),
    path('quran/<id>/detail', views.detailquran),
    # =============== Nadzom ====================
    path('datakitab/', views.kitab),
    path('nadzom/', views.nadzom),
    path('nadzom/<id>/delete', views.nadzom),
    # path('datakitab/<id>/editkitab/', views.editkitab),
    # path('<id>/detail/', views.detail),
    #  ============ pengumuman ==============
    path('pengumuman/', views.pengumuman),
    path('pengumuman/<id>/delete', views.deletepngm),
    path('pengumuman/<id>/detail', views.detailpngm),

]
