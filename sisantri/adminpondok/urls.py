from django.contrib import admin
from django.urls import path

from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('datapengajar/', views.datapengajar),
    path('datapengajar/<id>/deletepengajar', views.deletepengajar),
    path('datapengajar/<id>/editpengajar', views.editpengajar),
    path('profil/', views.profil),
    path('datasantri/', views.datasantri),
    path('datakitab/', views.datakitab),
    path('quran/', views.quran),
    path('kitabkuning/', views.kitabkuning),
    path('<id>/delete/', views.delete),
    # path('<id>/update/', views.update),
    # path('<id>/detail/', views.detail),
]
