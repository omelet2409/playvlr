from django.db import models
from cloudinary.models import CloudinaryField
from django.urls import reverse
from django.utils.text import slugify
# Create your models here.

class Map(models.Model):
    
    #Maps
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    img = CloudinaryField('img')
    slug = models.SlugField()
    status = models.CharField(max_length=400)
    
    #map detail
    
    map_location = models.CharField(max_length=250)
    
    img1 = CloudinaryField('img')
    img2 = CloudinaryField('img')
    img3 = CloudinaryField('img')
    img4 = CloudinaryField('img')
    img5 = CloudinaryField('img')
    img6 = CloudinaryField('img')
    img7 = CloudinaryField('img')
    img8 = CloudinaryField('img')
    
    

    class Meta:
        verbose_name = ("map")
        verbose_name_plural = ("maps")
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name, allow_unicode=True)
        super(Map, self).save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse('home:map_detail', kwargs={'slug': self.slug})
