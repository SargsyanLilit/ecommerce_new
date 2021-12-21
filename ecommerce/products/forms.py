from django import forms
from django.core.exceptions import ValidationError
from products.models import Product, ProductReviews


class ProductQuantityForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('quantity',)


class QuantityForm(forms.Form):
    quantity = forms.IntegerField(min_value=1)


class AddReview(forms.ModelForm):
    class Meta:
        model = ProductReviews
        fields = ['review_text']