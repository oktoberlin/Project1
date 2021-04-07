from django.urls import path
from . import views

urlpatterns = [
    path('', views.daftar_kelas, name="daftar_kelas"),
    path('pre_toefl/', views.pre_toefl_add, name="pre_toefl"),
    path('english_todler/', views.english_todler_add, name="english_todler"),
    path('pre_ielts/', views.pre_ielts_add, name="pre_ielts"),
    path('thanks/', views.thanks, name="thanks"),
]
