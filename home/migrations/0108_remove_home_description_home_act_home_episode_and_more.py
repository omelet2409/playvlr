# Generated by Django 4.1.13 on 2024-03-26 03:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0107_home_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='home',
            name='description',
        ),
        migrations.AddField(
            model_name='home',
            name='act',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='home',
            name='episode',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='home',
            name='year',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
    ]
