from django.contrib import admin
from .models import Perfume

class PerfumeAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand', 'price', 'stock')  # Sesuaikan dengan field pada model Perfume

# Daftarkan model bersama class admin-nya
admin.site.register(Perfume, PerfumeAdmin)
