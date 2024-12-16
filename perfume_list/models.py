from django.db import models

class Perfume(models.Model):
    # Pilihan ukuran parfum
    SIZE_CHOICES = [
        ('30ml', '30ml'),
        ('60ml', '60ml'),
        ('90ml', '90ml'),
    ]

    name = models.CharField(max_length=255, default='Unnamed Perfume')  
    brand = models.CharField(max_length=100)
    stock = models.PositiveIntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2) 
    size = models.CharField(max_length=10, choices=SIZE_CHOICES) 
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='media/perfume_images/', blank=True, null=True) 
    is_available = models.BooleanField(default=True) 

    def __str__(self):
        return f"{self.name} ({self.size}) - {self.brand}"

    def save(self, *args, **kwargs):
       
        if self.stock > 0:
            self.is_available = True
        else:
            self.is_available = False
        super().save(*args, **kwargs)

