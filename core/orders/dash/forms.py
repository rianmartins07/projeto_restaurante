from django import forms
from django.core.exceptions import ValidationError
from pycpfcnpj import cpfcnpj


from orders.models import Orders



class OrdersForm(forms.ModelForm):
    
    quantity = forms.IntegerField(
        required=True,
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control'
            }
        )
    )
    
    quantity = forms.IntegerField(
        required=True,
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control'
            }
        )
    )
    
    class Meta:
        model = Orders
        fields = '__all__'
