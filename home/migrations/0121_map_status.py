# Generated by Django 4.1.13 on 2024-05-15 03:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0120_rename_agent_home_agent_tutorial_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='map',
            name='status',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
