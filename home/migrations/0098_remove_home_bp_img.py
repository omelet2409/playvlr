# Generated by Django 4.1.7 on 2023-05-09 13:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0097_home_bp_img'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='home',
            name='bp_img',
        ),
    ]
