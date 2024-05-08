from django.db import models
from cloudinary.models import CloudinaryField
from django.urls import reverse
from django.utils.text import slugify
from django.contrib.auth.models import User

# Create your models here.

class Home(models.Model):
    
    name = models.CharField(max_length=100)
    link = models.CharField(max_length=200)
    episode =  models.CharField(max_length=10)
    act = models.CharField(max_length=10)
    year = models.CharField(max_length=10)
    img = CloudinaryField('img')
    #data
    
    agent = models.CharField(max_length=50)
    maps = models.CharField(max_length=50)
    arresnals = models.CharField(max_length=50)
    specs = models.CharField(max_length=50)
    news = models.CharField(max_length=50)
    battlepass = models.CharField(max_length=50)
    premieres = models.CharField(max_length=50)
    tutorials = models.CharField(max_length=50)

    class Meta:
        verbose_name = ("home")
        verbose_name_plural = ("homes")
        
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('homes', kwargs={'slug': self.slug})
