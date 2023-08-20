from django.db import models
from cloudinary.models import CloudinaryField
from django.urls import reverse
from django.utils.text import slugify
# Create your models here.


class Agent(models.Model):

    # Agent
    name = models.CharField(max_length=100)
    bio = models.CharField(max_length=600)
    country = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    role_icon = CloudinaryField('img')
    number = models.CharField(max_length=50)

    img = CloudinaryField('img')
    avatar_icon = CloudinaryField('img')
    slug = models.SlugField()
    #
    # skill q
    skill_q_name = models.CharField(max_length=100)
    skill_q_icon = CloudinaryField('icon', transformation=[
                                   {'width': 180, 'height': 180, 'crop': 'fill'}])
    skill_q_video = CloudinaryField(resource_type='video')
    skill_q_description = models.CharField(max_length=700)

    # skill e
    skill_e_name = models.CharField(max_length=100)
    skill_e_icon = CloudinaryField('icon', transformation=[
                                   {'width': 180, 'height': 180, 'crop': 'fill'}])
    skill_e_video = CloudinaryField(resource_type='video')
    skill_e_description = models.CharField(max_length=700)

    # skill c
    skill_c_name = models.CharField(max_length=100)
    skill_c_icon = CloudinaryField('icon', transformation=[
                                   {'width': 180, 'height': 180, 'crop': 'fill'}])
    skill_c_video = CloudinaryField(resource_type='video')
    skill_c_description = models.CharField(max_length=700)

    # skill x
    skill_x_name = models.CharField(max_length=100)
    skill_x_icon = CloudinaryField('icon', transformation=[
                                   {'width': 180, 'height': 180, 'crop': 'fill'}])
    skill_x_video = CloudinaryField(resource_type='video')
    skill_x_description = models.CharField(max_length=700)

    class Meta:
        verbose_name = ("agent")
        verbose_name_plural = ("agents")

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name, allow_unicode=True)
        super(Agent, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('home:agent_detail', kwargs={'slug': self.slug})
