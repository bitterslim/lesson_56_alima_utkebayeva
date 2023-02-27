from django import forms
from django.core.exceptions import ValidationError

from webapp.models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'description', 'image', 'category', 'leftover', 'price')
        labels = {
            'name': 'Name',
            'description': 'Description',
            'image': 'Image',
            'category': 'Category',
            'leftover': 'Leftover',
            'price': 'Price'
        }

    def clean_user(self):
        name = self.cleaned_data.get('name')
        if len(name) < 2:
            raise ValidationError('Product name is short')
        return name


