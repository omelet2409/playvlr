from django.db import models
from cloudinary.models import CloudinaryField
from django.urls import reverse
from django.utils.text import slugify
# Create your models here.

class Weapon(models.Model):
    
    #Weapons
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=500)
    money = models.CharField(max_length= 10)
    dmg_h = models.CharField(max_length=500)
    dmg_b = models.CharField(max_length=500)
    dmg_l = models.CharField(max_length=500)
    
    #weapon - distance
    
    dmg_h_far = models.CharField(max_length=50)
    dmg_b_far = models.CharField(max_length=50)
    dmg_l_far = models.CharField(max_length=50)
    
    
    img = CloudinaryField('img')
    slug = models.SlugField()
    description = models.CharField(max_length=500)
    bio = models.CharField(max_length=200)
    
    

    

    class Meta:
        verbose_name = ("weapon")
        verbose_name_plural = ("weapons")

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name, allow_unicode = True)
        super(Weapon, self).save(*args, **kwargs)
    
    
    def get_absolute_url(self):
        return reverse('home:weapon_detail', kwargs={'slug': self.slug})


    
