from django.db import models
from cloudinary.models import CloudinaryField
from django.urls import reverse
# Create your models here.

class Signup(models.Model):
    
    #tutorials
    img1 = CloudinaryField('img')
    img2 = CloudinaryField('img')
    img3 = CloudinaryField('img')
    img4 = CloudinaryField('img')
    img5 = CloudinaryField('img')
    img6 = CloudinaryField('img')
    img7 = CloudinaryField('img')


    class Meta:
        verbose_name = "signup"
        verbose_name_plural = "signups"
    
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)



    
    



