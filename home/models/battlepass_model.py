from django.db import models
from cloudinary.models import CloudinaryField
from django.urls import reverse
# Create your models here.

class Battlepass(models.Model):
    name = models.CharField(max_length=200)
    datetime = models.DateTimeField(auto_now=False)
    bio =  models.CharField( max_length=1000)
    
    
    class Meta: 
        verbose_name = ("battlepass")
        verbose_name_plural = ("battlepasss")
        
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('battlepasss', kwargs={'slug: self.slug'})
    