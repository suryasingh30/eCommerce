# products/models.py
from django.db import models
from django.utils.text import slugify

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=120, unique=True, blank=True)

    def save(self, *args, **kwargs):
        # update kardo automatically
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Product(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()
    price=models.DecimalField(max_digits=10, decimal_places=2)
    stock=models.PositiveIntegerField()
    image=models.ImageField(upload_to='product_images/', null=True, blank=True)
    category=models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title