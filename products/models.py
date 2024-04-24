from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):  
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    ingredients = models.TextField()
    nutrition = models.TextField()
    weight = models.TextField()    
    price = models.DecimalField(max_digits=6, decimal_places=2)   
    image = models.ImageField(null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)

    def __str__(self):
        return self.name

class Review(models.Model):    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    title = models.TextField(max_length=300)
    review = models.TextField(max_length=300)

    def __str__(self):
        return str(self.product.name)





