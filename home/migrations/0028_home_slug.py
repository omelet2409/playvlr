# Generated by Django 4.1.7 on 2023-03-24 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0027_rename_img_home_img_agent_remove_home_agenttitle_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='home',
            name='slug',
            field=models.SlugField(default=1),
            preserve_default=False,
        ),
    ]
