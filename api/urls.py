from django.urls import path
from .views import ClientsView, ProductsView, BillsView,Bills_ProductsView

urlpatterns = [
    path('clients/',ClientsView.as_view(), name= 'clients_list'),
    path('clients/<int:id>',ClientsView.as_view(), name= 'clients_process'),
    path('products/',ProductsView.as_view(), name= 'products_list'),
    path('products/<int:id>',ProductsView.as_view(), name= 'products_process'),
    path('bills/',BillsView.as_view(), name= 'bills_list'),
    path('bills/<int:id>',BillsView.as_view(), name= 'bills_process'),
    path('bills_products/',Bills_ProductsView.as_view(), name= 'bills_products'),
    path('bills_products/<int:id>',Bills_ProductsView.as_view(), name= 'bills_products'),

]