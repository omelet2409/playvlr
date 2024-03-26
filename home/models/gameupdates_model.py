from django.db import models
from cloudinary.models import CloudinaryField
from django.urls import reverse

class Gameupdate(models.Model):
    
    #title
    title = models.CharField(max_length=1000)
    big_title = models.CharField(max_length=500)
    field2 = models.TextField(default=''' ''')  # Thay đổi từ CharField sang TextField

    
    class Meta:
        verbose_name = "gameupdate"
        verbose_name_plural = "gameupdates"
        
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
