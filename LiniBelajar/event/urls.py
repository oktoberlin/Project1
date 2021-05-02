from django.urls import path
from . import views
app_name = 'event'
urlpatterns = [
    path('', views.talkshow_add, name="talkshow"),
]