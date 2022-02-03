# Views for inventory app are located here

from django.http import HttpResponse
from .models import Inventory
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
)
from django.contrib.auth.mixins import LoginRequiredMixin


def addToInventory(request, name, stock, cp, sp, vendor, vendor_phone, pid):
    newInventory = Inventory(name=name, stock=stock, cp=cp, sp=sp, vendor=vendor, vendor_phon_no=vendor_phone, pid=pid)
    newInventory.save()
    return HttpResponse(status=200)


class InventoryCreateView(LoginRequiredMixin, CreateView):
    """ This function creates a model of type Inventory """

    model = Inventory
    fields = ['name', 'stock', 'cp', 'sp', 'vendor', 'pid']


class InventoryDetailView(LoginRequiredMixin, DetailView):
    """ This Class is for viewing Inventory Details """

    model = Inventory


class InventoryListView(LoginRequiredMixin, ListView):
    """ This Class is for viewing list of Inventories """

    model = Inventory
    context_object_name = 'stocks'
