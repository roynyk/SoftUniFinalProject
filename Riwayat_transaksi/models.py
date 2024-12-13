from django.db import models
from django.contrib.auth.models import User
from perfume_list.models import Perfume
from django.utils.timezone import now

class TransactionHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    perfume = models.ForeignKey(Perfume, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(default=now)

    def __str__(self):
        return f"Transaction by {self.user.username} on {self.created_at}"
