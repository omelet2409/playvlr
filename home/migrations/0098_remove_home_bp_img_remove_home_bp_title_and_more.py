# Generated by Django 4.1.7 on 2023-05-09 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0097_remove_home_datetime'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='home',
            name='bp_img',
        ),
        migrations.RemoveField(
            model_name='home',
            name='bp_title',
        ),
        migrations.RemoveField(
            model_name='home',
            name='description',
        ),
        migrations.RemoveField(
            model_name='home',
            name='img',
        ),
        migrations.AlterField(
            model_name='home',
            name='link',
            field=models.CharField(max_length=200),
        ),
    ]