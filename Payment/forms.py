from django import forms
from .models import Payment

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['perfume', 'quantity', 'payment_method']  # Hanya field yang dapat diedit
        labels = {
            'perfume': 'Perfume Name',
            'quantity': 'Quantity',
            'payment_method': 'Payment Method',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Customizing the appearance of fields
        self.fields['perfume'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Select Perfume'})
        self.fields['quantity'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter Quantity'})
        self.fields['payment_method'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Select Payment Method'})
