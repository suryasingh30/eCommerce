from django.db import models
from users.models import User
from products.models import Product

# Create your models here.
class Wishlist(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE, related_name='wishlist')
    products=models.ManyToManyField(Product, related_name='wishlisted_by')

    def __str__(self):
        return f"{self.user.username}'s Wishlist"