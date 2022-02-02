from django import forms

from .models import Cart


class NewCartForm(forms.ModelForm):
    class Meta:
        model = Cart
        fields = ['product', 'count']