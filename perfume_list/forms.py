from django import forms
from .models import Perfume

class PerfumeForm(forms.ModelForm):
    class Meta:
        model = Perfume
        fields = ['name', 'stock', 'brand', 'price', 'size', 'description', 'image']  # Field yang ingin ditampilkan di form
