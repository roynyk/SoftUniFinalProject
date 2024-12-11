from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.perfume_list, name='perfume_list'),
    path('add_perfume/', views.add_perfume, name='add_perfume'),
    path('edit_perfume/<int:perfume_id>/', views.edit_perfume, name='edit_perfume'),
    path('delete_perfume/<int:perfume_id>/', views.delete_perfume, name='delete_perfume'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
