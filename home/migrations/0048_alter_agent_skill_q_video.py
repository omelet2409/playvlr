# Generated by Django 4.1.7 on 2023-04-04 10:47

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0047_alter_agent_skill_q_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agent',
            name='skill_q_video',
            field=cloudinary.models.CloudinaryField(max_length=255),
        ),
    ]
