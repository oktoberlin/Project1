from django.urls import path

from . import views

app_name = 'store'

urlpatterns = [
    path('', views.store, name='store'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('get_order_total/', views.getOrderTotal, name='get_order_total'),
    path('process_order/', views.processOrder, name='process_order'),
    path('show_detail/', views.showDetail, name='show_detail'),
    path('update_item/', views.updateItem, name='update_item'),
]
'''
path('login/', views.loginView, name='login'),
    path('logout/', views.logoutView, name='logout'),
     path('register/', views.registerView, name='register'),
'''