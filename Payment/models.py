from django.db import models
from django.conf import settings
from django.utils.timezone import now
from perfume_list.models import Perfume

class Payment(models.Model):
    PAYMENT_METHOD_CHOICES = [
        ('Cash', 'Cash'),
        ('Credit', 'Credit'),
        ('Dompet Digital', 'Dompet Digital'),
    ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='user_payments'
    )
    perfume = models.ForeignKey(
        Perfume,
        on_delete=models.CASCADE,
        related_name='perfume_payments'
    )
    quantity = models.PositiveIntegerField(default=1)  # Pastikan nilai positif
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    payment_method = models.CharField(
        max_length=20,
        choices=PAYMENT_METHOD_CHOICES,
        default='Cash'
    )
    date = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if self.perfume and self.perfume.price:
            self.total_price = self.quantity * self.perfume.price
        else:
            self.total_price = 0.00 
        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Payments"
        ordering = ['-date']

    def __str__(self):
        return f'{self.user.username} - {self.perfume.name} - {self.quantity} pcs - {self.payment_method}'
