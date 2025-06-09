from django.urls import path
from . import views
from .orders import views as order_views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('logout/', views.logout_user, name = 'logout'),
    path('register/', views.register_user, name='register'),
    path('customer/<int:id>', views.customer_record, name='customer-record'),
    path('customer/<int:id>/delete', views.delete_customer, name='delete-customer'),
    path('customer/create', views.create_customer, name='create-customer'),
    path('customer/<int:id>/update', views.update_customer, name='update-customer'),

    # Customer Orders
    path('customer/<int:id>/orders', views.customer_orders, name='customer-orders'),

    # Order URLs
    path('order/', order_views.order_list, name='order-list'),
    path('order/<int:id>', order_views.order_record, name='order-record'),
    path('order/<int:id>/delete', order_views.delete_order, name='delete-order'),
    path('order/<int:id>/edit', order_views.edit_order, name='edit-order'),
    path('order/<int:id>/update', order_views.update_order, name='update-order'),
]
