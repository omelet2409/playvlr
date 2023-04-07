from django.db import models
from cloudinary.models import CloudinaryField
from django.urls import reverse
# Create your models here.

class Spec(models.Model):
    
    #specs
    windows = models.CharField(max_length=100)
    ram = models.CharField(max_length=100)
    vram = models.CharField(max_length=100)
    
    cpu_1 = models.CharField(max_length=100)
    cpu_2 = models.CharField(max_length=100)
    cpu_3 = models.CharField(max_length=100)
    gpu_1 = models.CharField(max_length=100)
    gpu_2 = models.CharField(max_length=100)
    gpu_3 = models.CharField(max_length=100)
    #
    
    
    

    class Meta:
        verbose_name = "spec"
        verbose_name_plural = "specs"
    
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)



    
    



