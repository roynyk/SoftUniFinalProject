from django import forms
from .models import TransactionHistory

class TransactionHistoryForm(forms.ModelForm):
    class Meta:
        model = TransactionHistory
        fields = ['perfume', 'quantity', 'total_price']
        widgets = {
            'perfume': forms.Select(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
            'total_price': forms.NumberInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
        }
