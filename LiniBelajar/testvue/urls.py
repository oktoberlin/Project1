from django.urls import path

from testvue import views as myapp_views

urlpatterns = [
    path('vue-test/', myapp_views.vue_test),
]
