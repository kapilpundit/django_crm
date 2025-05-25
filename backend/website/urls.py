from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    # path('login/', views.login_user, name = 'login'),
    path('logout/', views.logout_user, name = 'logout'),
    path('register/', views.register_user, name='register'),
    path('customer/<int:id>', views.customer_record, name='customer-record'),
    path('customer/<int:id>/delete', views.delete_customer, name='delete-customer'),
    path('customer/create', views.create_customer, name='create-customer'),
]
