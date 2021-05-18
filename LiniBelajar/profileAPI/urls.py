from django.urls import path
from .views import ProfileCreate, ProfileList, ProfileDetail, ProfileUpdate, ProfileDelete


urlpatterns = [
    path('create/', ProfileCreate.as_view(), name='create-profile'),
    path('', ProfileList.as_view()),
    path('<int:pk>/', ProfileDetail.as_view(), name='retrieve-profile'),
    path('update/<int:pk>/', ProfileUpdate.as_view(), name='update-profile'),
    path('delete/<int:pk>/', ProfileDelete.as_view(), name='delete-profile')
]