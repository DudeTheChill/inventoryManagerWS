from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from vendors.models import Vendor
from .forms import NewCartForm
from .models import Cart
from orders import views as order_views
from django.contrib.auth.decorators import login_required


@login_required
def NewCart(request, vendor_id):
    vendor = Vendor.objects.get(pk=vendor_id)
    carts = Cart.objects.filter(vendor__pk=vendor_id)
    cart = Cart(vendor=vendor)
    message = ""
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        add_cart_form = NewCartForm(request.POST, instance=cart)
        # check whether it's valid:
        if add_cart_form.is_valid():
            new_cart = add_cart_form.save(commit=False)
            if new_cart.count > new_cart.product.stock:
                message = "count is more than stock"
            else:
                new_cart.save()
            return redirect('cart-form', vendor_id=vendor_id)

        # if a GET (or any other method) we'll create a blank form
    else:
        add_cart_form = NewCartForm(instance=cart)
    context = {
        'form': add_cart_form,
        'vendor': vendor,
        'carts': carts,
        'message': message,
    }

    return render(request, 'carts/cart_form.html', context=context)


@login_required
def DeleteAllCart(request, vendor_id):
    Cart.objects.filter(vendor__pk=vendor_id).delete()
    return redirect('cart-list')


@login_required
def DeleteCart(request, pk):
    cart = Cart.objects.get(pk=pk)
    vendor = cart.vendor
    cart.delete()
    return redirect('cart-form', vendor_id=vendor.pk)


@login_required
def CartList(request):
    vendor_ids = Cart.objects.all().values_list('vendor__id')
    vendors = Vendor.objects.filter(pk=vendor_ids)
    context = {
        'vendor': vendors,
    }
    return render(request, 'carts/cart_list.html', context=context)


@login_required
def FinalizeCart(request, vendor_id):
    order = order_views.CreateOrder(vendor_id)
    return redirect('order-details', pk=order.pk)
