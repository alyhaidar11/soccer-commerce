import uuid
from django.db import models

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('cloth', 'Cloth'),
        ('shoe', 'Shoe'),
        ('tools', 'Tools'),
    ]

    name = models.CharField(max_length=255)
    price = models.IntegerField()
    quantity = models.IntegerField()
    description = models.TextField()
    thumbnail = models.URLField(blank=True, null=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='update')
    is_featured = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
    
    @property
    def is_hot(self):
        """Contoh: produk dianggap 'hot' kalau quantity < 5"""
        return self.quantity < 5
    
   