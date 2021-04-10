from django.urls import path
from . import views

urlpatterns = [
   #path('', views.login, name="login"),
   path('activate/<uidb64>/<token>/',views.activate, name='activate'),
]
