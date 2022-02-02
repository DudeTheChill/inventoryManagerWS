from django import forms

from inventory.models import Inventory


class NewInventoryForm(forms.ModelForm):
    class Meta:
        model = Inventory
        fields = '__all__'