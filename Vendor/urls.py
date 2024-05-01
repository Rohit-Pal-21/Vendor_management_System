from django.contrib import admin
from django.urls import path, include
from .views import *


urlpatterns = [
    path('signup', Signup.as_view(), name='signup'),
    path('login', Login.as_view(), name='login'),
    path('vendors', VendorAPI.as_view(), name='Vendors'),
    path('vendors/<str:id>', VendorDataAPI.as_view(), name='VendorsData'),
    path('vendors/<str:id>/performance', PerformanceAPI.as_view(), name='VendorsPerformance'),
    path('purchase_orders', PurchaseOrderAPI.as_view(), name='PurchaseOrders'),
    path('purchase_orders/<str:id>', PurchaseOrderDataAPI.as_view(), name='PurchaseOrdersData'),
    path('purchase_orders/<str:id>/acknowledge', OrderAcknowledge.as_view(), name='PurchaseOrderAcknowledged'),
]
