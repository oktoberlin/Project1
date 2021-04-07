from django.urls import path
from . import views

urlpatterns = [
    path('', views.daftar_kelas, name="daftar_kelas"),
]
