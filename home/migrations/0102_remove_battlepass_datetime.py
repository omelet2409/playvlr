# Generated by Django 4.1.7 on 2023-05-30 06:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0101_battlepass_img'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='battlepass',
            name='datetime',
        ),
    ]
