# Generated by Django 4.1.7 on 2023-03-28 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0035_rename_title_agents_home_nav_title_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='home',
            name='link',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
