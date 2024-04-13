from django.db import models

# Create your models here.

class Contact(models.Model):    
    name = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(max_length=300, null=False, blank=False)
    message = models.CharField(max_length=500, null=False, blank=False)
    
