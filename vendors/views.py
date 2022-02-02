from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from orders.models import Order
from .models import Vendor
from django.views.generic import (
    ListView,
    CreateView,
)


class VendorCreateView(LoginRequiredMixin, CreateView):
    model = Vendor
    fields = ['name', 'phone']


class VendorListView(LoginRequiredMixin, ListView):
    model = Vendor
    context_object_name = 'vendors'


@login_required
def VendorDetailView(request, pk):
    vendor = Vendor.objects.get(pk=pk)
    orders = Order.objects.filter(vendor__pk=pk)
    context = {
        'object': vendor,
        'orders': orders,
    }
    return render(request, 'vendors/vendor_detail.html', context=context)
