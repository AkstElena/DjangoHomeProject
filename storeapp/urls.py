"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .views import index,  get_clients, get_products, get_orders, \
    get_client_on_id, get_orders_on_client_id, delete_client_on_id, get_products_in_orders_on_client_id_sort, \
    add_product, add_client, update_product, update_client, get_product_on_id, add_order, get_order_on_id

urlpatterns = [
    path('', index, name='index'),
    # path('fake_clients/', create_fake_clients, name='create_fake_clients'),
    # path('fake_products/', create_fake_products, name='create_fake_products'),
    # path('fake_order/', create_fake_order, name='create_fake_order'),
    path('clients/', get_clients, name='get_clients'),
    path('clients/<int:client_id>/', get_client_on_id, name='get_client_on_id'),
    path('clients/update/<int:client_id>/', update_client, name='update_client'),
    path('delete_client/<int:client_id>/', delete_client_on_id, name='delete_client_on_id'),
    path('clients/create', add_client, name='add_client'),
    path('products/', get_products, name='get_products'),
    path('products/<int:product_id>/', get_product_on_id, name='get_product_on_id'),
    path('products/update/<int:product_id>/', update_product, name='update_product'),
    path('products/create', add_product, name='add_product'),
    path('orders/', get_orders, name='get_orders'),
    path('orders/<int:order_id>', get_order_on_id, name='get_order_on_id'),
    path('orders/create', add_order, name='add_order'),
    path('orders/<int:client_id>/', get_orders_on_client_id, name='get_orders_on_client_id'),
    path('orders/<int:client_id>/<int:days>', get_products_in_orders_on_client_id_sort,
         name='get_products_in_orders_on_client_id_sort'),
]
