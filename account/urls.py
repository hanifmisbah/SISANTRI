from django.urls import path
from . import views
urlpatterns = [
    path('', views.login_user),
    path('register/', views.regis),
    path('logout/', views.logout_user),
]