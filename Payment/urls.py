from django.urls import path
from . import views
from .views import decrease_quantity

urlpatterns = [
    path('payment/', views.payment_list, name='payment_list'),
    path('delete_payment/<int:payment_id>/', views.delete_payment, name='delete_payment'),
    path('payment/<int:payment_id>/decrease/', decrease_quantity, name='decrease_quantity'),
    path('payment-order/', views.payment_order, name='payment_order'),
]
