from django.shortcuts import render
from carts.models import Cart
from inventory.models import Inventory
from vendors.models import Vendor
from .models import OrderItem, Order
from datetime import date, timedelta
from django.contrib.auth.decorators import login_required


@login_required
def CreateOrder(vendor_id):
    carts = Cart.objects.filter(vendor__pk=vendor_id)
    vendor = Vendor.objects.get(pk=vendor_id)
    order = Order(vendor=vendor)
    order.save()
    for cart in carts:
        new_item = OrderItem(order=order, product=cart.product, count=cart.count)
        product = Inventory.objects.get(pk=new_item.product.pk)
        if product.stock > new_item.count:
            product.stock = product.stock - new_item.count
            product.save()
        else:
            product.count = 0
            product.save()
        new_item.save()
    carts.delete()
    return order


@login_required
def OrderDetails(request, pk):
    order = Order.objects.get(pk=pk)
    items = OrderItem.objects.filter(order=order)

    context = {
        'order': order,
        'items': items
    }
    return render(request, 'orders/order_detail.html', context=context)


@login_required
def OrderList(request):
    orders = Order.objects.all()
    return render(request, 'orders/order_list.html', context={'orders': orders})

@login_required
def About(request):
    return render(request, 'orders/about.html')
# while start_date <= end_date:
#     orders = Order.objects.filter(date_created=start_date)
#     start_date += delta
