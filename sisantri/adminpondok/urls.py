from django.contrib import admin
from django.urls import path

from . import views
urlpatterns = [
    path('', views.index),
<<<<<<< HEAD
    # PENGAJAR =========================================================================
=======
    path('profil/', views.profil),
>>>>>>> e588cbc8343ee373a921fbbdf7ba00935e2af48f
    path('datapengajar/', views.datapengajar),
    path('datapengajar/<id>/deletepengajar/', views.deletepengajar),
    path('datapengajar/<id>/editpengajar', views.editpengajar),
<<<<<<< HEAD
    # SANTRI ===========================================================================
    path('datasantri/<id>/deletesantri', views.deletesantri),
    # path('<id>/update/', views.update),
    # path('<id>/detail/', views.detail),
    # DASHBOARD =========================================================================
    path('profil/', views.profil),
=======
>>>>>>> e588cbc8343ee373a921fbbdf7ba00935e2af48f
    path('datasantri/', views.datasantri),
    path('datasantri/<id>/deletesantri/', views.deletesantri),
    path('datakitab/', views.datakitab),
    path('quran/', views.quran),
    path('kitabkuning/', views.kitabkuning),
<<<<<<< HEAD

=======
    # path('<id>/update/', views.update),
    # path('<id>/detail/', views.detail),
>>>>>>> e588cbc8343ee373a921fbbdf7ba00935e2af48f
]
