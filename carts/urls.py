from django.urls import path
from . import views

urlpatterns = [
     path('new/<int:vendor_id>', views.NewCart, name='cart-form'),
     path('deleteall/<int:vendor_id>/', views.DeleteAllCart, name='cart-delete-all'),
     path('list/', views.CartList, name='cart-list'),
     path('delete/<int:pk>/', views.DeleteCart, name='cart-delete'),
     path('finalize/<int:vendor_id>/', views.FinalizeCart, name='create-order')
]