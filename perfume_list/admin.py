from django.contrib import admin
from .models import Perfume

class PerfumeAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand', 'price', 'stock')
    list_filter = ('brand', 'price') 
    search_fields = ('name', 'brand') 

admin.site.register(Perfume, PerfumeAdmin)
