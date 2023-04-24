from django.db import models
from cloudinary.models import CloudinaryField
from django.urls import reverse
# Create your models here.

class Tutorial(models.Model):
    
    #tutorials
    img1 = CloudinaryField('img')
    description = models.CharField(max_length=1000)


    class Meta:
        verbose_name = "tutorial"
        verbose_name_plural = "tutorials"
    
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)



    
    



