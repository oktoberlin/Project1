from . import views
from django.urls import path
from .views import *
app_name = 'community'
urlpatterns = [
    path('', PostListView.as_view(), name="community"),
    path('user/<str:username>/', UserProfileView.as_view(), name="user-profile"),
    path('post/<int:pk>/', PostDetailView.as_view(), name="post-detail"),
    path('post/new/', PostCreateView.as_view(), name="post-create"),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name="post-update"),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name="post-delete"),

]
