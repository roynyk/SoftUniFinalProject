from django.contrib import admin
from .models import UserProfile

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'profile_picture', 'bio', 'birth_date', 'address', 'phone_number') 
    list_filter = ('birth_date', 'address')
    search_fields = ('user__username', 'bio', 'address', 'phone_number') 
