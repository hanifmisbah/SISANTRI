from django.contrib import admin
from django.urls import path

from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('profil/', views.profil),
    path('datasantri/', views.datasantri),
    path('datapengajar/', views.datapengajar),
    path('datakitab/', views.datakitab),
    path('quran/', views.quran),
    path('kitabkuning/', views.kitabkuning),
]