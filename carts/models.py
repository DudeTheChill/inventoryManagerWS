from django.db import models
from django.urls import reverse

from vendors.models import Vendor
from inventory.models import Inventory


class Cart(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    product = models.ForeignKey(Inventory, on_delete=models.CASCADE)
    count = models.IntegerField(default=1)


    def __str__(self):
        return "Cart Item with count: " + str(self.count) + " product: " + self.product.name



    # def get_absolute_url(self):
    #     return reverse('view-cart', kwargs={'pk': self.pk})

# Create your models here.
