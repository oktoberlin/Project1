from django.urls import path, include
from . import views
app_name = 'online_class'
urlpatterns = [
    path('', views.daftar_kelas, name="online_class"),
    path('pre_toefl/', views.pre_toefl_add, name="pre_toefl"),
    path('english_toddler/', views.english_todler_add, name="english_toddler"),
    path('pre_ielts/', views.pre_ielts_add, name="pre_ielts"),
    path('thanks/', views.thanks, name="thanks"),
]
