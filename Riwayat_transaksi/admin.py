from django.contrib import admin
from .models import TransactionHistory

@admin.register(TransactionHistory)
class TransactionHistoryAdmin(admin.ModelAdmin):
    list_display = ('user', 'perfume', 'quantity', 'total_price')
    search_fields = ('user__username', 'perfume__name')
