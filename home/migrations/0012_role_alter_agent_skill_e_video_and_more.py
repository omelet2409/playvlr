# Generated by Django 4.1.7 on 2023-03-23 12:18

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_rename_specs_spec'),
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=500)),
                ('img', cloudinary.models.CloudinaryField(max_length=255, verbose_name='img')),
                ('slug', models.SlugField()),
            ],
            options={
                'verbose_name': 'role',
                'verbose_name_plural': 'roles',
            },
        ),
        migrations.AlterField(
            model_name='agent',
            name='skill_e_video',
            field=cloudinary.models.CloudinaryField(max_length=255),
        ),
        migrations.AlterField(
            model_name='agent',
            name='skill_q_video',
            field=cloudinary.models.CloudinaryField(max_length=255),
        ),
    ]
