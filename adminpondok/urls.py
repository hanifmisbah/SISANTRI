from django.urls import path

from . import views
urlpatterns = [
    path('coba/', views.coba),
    path('', views.index),
    path('<id>/delete', views.deletepngm),
    path('profil/', views.profil),
    # ============= santri ====================
    path('datasantri/', views.datasantri),
    path('datasantri/<id>/delete', views.deletesantri),
    path('datasantri/<id>/update', views.editsantri),
    path('datasantri/<id>/detail', views.detailsantri),
    # ============= kitab ====================
    path('datakitab/', views.datakitab),
    path('datakitab/level', views.level),
    path('datakitab/kategori', views.kategori),
]
