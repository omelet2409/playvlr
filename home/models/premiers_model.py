from django.db import models
from cloudinary.models import CloudinaryField
from django.urls import reverse
# Create your models here.

class Premier(models.Model):
    
    #FAQ
    question = models.CharField(max_length=500)
    answer = models.CharField(max_length=500)
    #

    class Meta:
        verbose_name = "premier"
        verbose_name_plural = "premiers"
    
    def __str__(self):
        return self.question
    
    def get_absolute_url(self):
        return reverse('newss', kwargs={'slug': self.slug})
