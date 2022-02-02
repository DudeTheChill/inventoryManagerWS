from django.db import models
from django.urls import reverse

from vendors.models import Vendor


class Inventory(models.Model):
    name = models.CharField(max_length=30)
    stock = models.IntegerField()
    cp = models.IntegerField()
    sp = models.IntegerField()
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    pid = models.IntegerField()

    def __str__(self):
        return "product id: " + str(self.pid) + " and name: " + self.name

    def get_absolute_url(self):
        return reverse('view-inventory', kwargs={'pk': self.pk})
