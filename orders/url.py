from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/', views.OrderDetails, name='order-details'),
    path('list/', views.OrderList, name='order-list'),
#    path('home/', views.HomeView, name='home')

]
