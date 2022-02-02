import datetime
from django.db import models
from vendors.models import Vendor
from inventory.models import Inventory

class Order(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    date_created = models.DateTimeField(default=datetime.date.today)

    def __str__(self):
        return "order for: " + self.vendor.name

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Inventory, on_delete=models.CASCADE)
    count = models.IntegerField()

    def __str__(self):
        return "order item for order: " + self.order.pk