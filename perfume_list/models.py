from django.db import models

class Perfume(models.Model):
    SIZE_CHOICES = [
        ('30ml', '30ml'),
        ('60ml', '60ml'),
        ('90ml', '90ml'),
    ]
    brand = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=1000, decimal_places=2)
    size = models.CharField(max_length=10, choices=SIZE_CHOICES)
    description = models.TextField()
    image = models.ImageField(upload_to='media/perfume_images/', blank=True, null=True)

    def __str__(self):
        return self.brand
