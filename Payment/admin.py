from django.contrib import admin
from .models import Payment

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('user', 'perfume', 'quantity', 'total_price', 'date') 
    list_filter = ('date', 'perfume')  
    search_fields = ('user__username', 'perfume__name')  
