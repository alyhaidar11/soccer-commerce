import uuid
from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('cloth', 'Cloth'),
        ('shoe', 'Shoe'),
        ('tools', 'Tools'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    sold = models.PositiveIntegerField(default=0)

    name = models.CharField(max_length=255)
    price = models.IntegerField()
    quantity = models.IntegerField()
    description = models.TextField()
    thumbnail = models.URLField(blank=True, null=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='update')
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True) 

class Employee(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    Persona = models.TextField()

class Book(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)

class Author(models.Model):
    bio = models.TextField()
    books = models.ManyToManyField(Book)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)



    def __str__(self):
        return self.name
    
    
    # @property
    # def is_hot(self):
    #     """Contoh: produk dianggap 'hot' kalau quantity < 5"""
    #     return self.quantity < 5
    
   