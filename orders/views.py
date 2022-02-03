# views for order app are located in this file

from django.shortcuts import render
from carts.models import Cart
from inventory.models import Inventory
from vendors.models import Vendor
from .models import OrderItem, Order
from datetime import date, timedelta
from django.contrib.auth.decorators import login_required
import csv
from django.http import HttpResponse


def CreateOrder(vendor_id):
    """ This function creates an order based on a vendor, it takes vendor_id as an input argument and returns the
    created order object """

    carts = Cart.objects.filter(vendor__pk=vendor_id)
    vendor = Vendor.objects.get(pk=vendor_id)
    order = Order(vendor=vendor)
    order.save()
    for cart in carts:
        new_item = OrderItem(order=order, product=cart.product, count=cart.count)
        product = Inventory.objects.get(pk=new_item.product.pk)
        # check whether the counts are consistent
        if product.stock > new_item.count:
            product.stock = product.stock - new_item.count
            product.save()
        else:
            product.count = 0
            product.save()
        new_item.save()
    # deletes all the previous cart items (now ordr items)
    carts.delete()
    return order


@login_required
def OrderDetails(request, pk):
    """ This function views order details and its items """

    order = Order.objects.get(pk=pk)
    items = OrderItem.objects.filter(order=order)

    context = {
        'order': order,
        'items': items
    }
    return render(request, 'orders/order_detail.html', context=context)


@login_required
def OrderList(request):
    """ This functions views order list """

    orders = Order.objects.all()
    return render(request, 'orders/order_list.html', context={'orders': orders})


@login_required
def About(request):
    return render(request, 'orders/about.html')


# while start_date <= end_date:
#     orders = Order.objects.filter(date_created=start_date)
#     start_date += delta

@login_required
def DownloadInvoice(request, pk):
    """ This function takes primary key of an order as an input arguement and then prints its information in a .CSV
    file for user to download """

    order = Order.objects.get(pk=pk)
    items = OrderItem.objects.filter(order__pk=pk)
    response = HttpResponse(
        content_type='text/csv',
        headers={'Content-Disposition': 'attachment; filename="invoice.csv"'},
    )
    totalSP = 0
    totalCount = 0
    writer = csv.writer(response)
    writer.writerow(['Order Number', 'Vendor', 'Date'])
    writer.writerow([str(order.pk), order.vendor.name, order.date_created.strftime("%m/%d/%Y")])
    writer.writerow(['Items', '', ''])
    writer.writerow(['Product Name', 'Count', 'Price'])
    for item in items:
        price = item.product.sp * item.count
        totalSP = totalSP + price
        totalCount = totalCount + item.count
        writer.writerow([item.product.name, str(item.count), str(price)])
    writer.writerow(['Total:', str(totalCount), str(totalSP)])
    return response
