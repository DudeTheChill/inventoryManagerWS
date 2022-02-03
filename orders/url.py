from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/', views.OrderDetails, name='order-details'),
    path('list/', views.OrderList, name='order-list'),
    path('about/', views.About, name='about'),
    path('download/<int:pk>/', views.DownloadInvoice, name='download'),
#    path('home/', views.HomeView, name='home')

]
