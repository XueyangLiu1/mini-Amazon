from django import forms 
from django.forms.fields import NumberInput
from django.core.validators import MinValueValidator


class PurchaseForm(forms.Form):
    productNum = forms.IntegerField(label='Number of products',required=True,validators=[MinValueValidator(1)])
    address_x = forms.IntegerField(label='Address x',required=True)
    address_y = forms.IntegerField(label='Address y',required=True)