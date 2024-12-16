from django.db import models
from django.contrib.auth.models import User
from perfume_list.models import Perfume
from django.utils.timezone import now

class TransactionHistory(models.Model):
    PAYMENT_METHOD_CHOICES = [
        ('Cash', 'Cash'),
        ('Cek', 'Cek'),
        ('Giro', 'Giro'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    payment_method = models.CharField(
        max_length=50, choices=PAYMENT_METHOD_CHOICES, default='Cash')
    perfume = models.ForeignKey(Perfume, on_delete=models.CASCADE)
    brand = models.CharField(max_length=100, default='Unknown Brand')
    quantity = models.PositiveIntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(default=now)

    def __str__(self):
        return f"Transaction by {self.user.username} on {self.date}"
