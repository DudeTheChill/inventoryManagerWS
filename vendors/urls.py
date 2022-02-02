from django.urls import path
from . import views

urlpatterns = [
    path('new/', views.VendorCreateView.as_view(), name='add-vendor'),
    path('view/<int:pk>/', views.VendorDetailView, name='view-vendor'),
    path('list/', views.VendorListView.as_view(), name='list-vendor'),
]