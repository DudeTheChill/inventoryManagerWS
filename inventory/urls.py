from django.urls import path
from . import views

urlpatterns = [
    path('add/<str:name>/<int:stock>/<int:cp>/<int:sp>/<str:vendor>/<str:vendor_phone>/<int:pid>/', views.addToInventory,
         name='add-to-inventory'),
    path('new/', views.InventoryCreateView.as_view(), name='add-to-inventory-form'),
    path('view/<int:pk>/', views.InventoryDetailView.as_view(), name='view-inventory'),
    path('list/', views.InventoryListView.as_view(), name='inventory-list')
]
