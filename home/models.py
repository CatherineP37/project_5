from django.db import models

# Create your models here.

class Contact(models.Model):    
    name = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(max_length=300, null=False, blank=False)
    message = models.TextField(null=False, blank=False, default='')

class Event(models.Model):    
    time = models.DateTimeField()
    title = models.TextField(null=False, blank=False, default='')
    location = models.TextField(null=False, blank=False, default='')
    description = models.TextField(null=False, blank=False, default='')

class Attendance(models.Model): 
    name = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(max_length=300, null=False, blank=False)
    event = models.TextField(null=False, blank=False, default='') 
     
    
    
    
