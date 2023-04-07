# Generated by Django 4.1.7 on 2023-03-28 18:36

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0031_home_link_home_title'),
    ]

    operations = [
        migrations.RenameField(
            model_name='home',
            old_name='link',
            new_name='description_agents',
        ),
        migrations.RemoveField(
            model_name='home',
            name='title',
        ),
        migrations.AddField(
            model_name='home',
            name='img',
            field=cloudinary.models.CloudinaryField(default=1, max_length=255, verbose_name='gif'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='home',
            name='title_agents',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
