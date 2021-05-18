from django.urls import path
from . import views
from .views import PostView


urlpatterns = [
    path('', views.PostView.as_view(), name= 'posts_list'),
]