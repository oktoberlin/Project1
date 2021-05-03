from django.urls import path
from . import views
app_name = 'user'
urlpatterns = [
   path('logout/', views.logoutUser, name="logout"),
   path('activate/<uidb64>/<token>/',views.activate, name='activate'),
]
