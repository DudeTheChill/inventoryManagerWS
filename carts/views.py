#views for cart app are located here

from django.shortcuts import render, redirect
from vendors.models import Vendor
from .forms import NewCartForm
from .models import Cart
from orders import views as order_views
from django.contrib.auth.decorators import login_required
from django.contrib import messages


@login_required
def NewCart(request, vendor_id):
    """ This function creates a new cart model based on a vendor id """

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
            # check whether the amounts are valid:
            if new_cart.count > new_cart.product.stock:
                messages.error(request, "count for " + new_cart.product.name + "must be lower than " + str(
                    new_cart.product.stock))
            else:
                new_cart.save()
                messages.success(request, new_cart.product.name + "successfully added to cart")
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
    """ This function is used to delete all cart items for a vendor """

    Cart.objects.filter(vendor__pk=vendor_id).delete()
    messages.success(request, "Pre-Order successfully deleted")
    return redirect('cart-list')


@login_required
def DeleteCart(request, pk):
    """ This function deletes a single item with argument pk """

    cart = Cart.objects.get(pk=pk)
    vendor = cart.vendor
    cart.delete()
    messages.success(request, "item successfully deleted")
    return redirect('cart-form', vendor_id=vendor.pk)


@login_required
def CartList(request):
    """ This function lists all the carts """

    vendor_ids = Cart.objects.all().values_list('vendor__id')
    vendors = Vendor.objects.filter(pk=vendor_ids)
    context = {
        'vendor': vendors,
    }
    return render(request, 'carts/cart_list.html', context=context)


@login_required
def FinalizeCart(request, vendor_id):
    """ This view is used to handle finalize url """

    order = order_views.CreateOrder(vendor_id)
    messages.success(request, "Order successfully created")
    return redirect('order-details', pk=order.pk)
