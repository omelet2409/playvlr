from django.db import models
from cloudinary.models import CloudinaryField
from django.urls import reverse
from django.utils.text import slugify
# Create your models here.

class Home(models.Model):
    
    name = models.CharField(max_length=100)
    link = models.CharField(max_length=200)
    episode =  models.CharField(max_length=10)
    act = models.CharField(max_length=10)
    year = models.CharField(max_length=10)
    img = CloudinaryField('img')
    
    
    class Meta:
        verbose_name = ("home")
        verbose_name_plural = ("homes")
        
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('homes', kwargs={'slug': self.slug})