# Generated by Django 4.1.7 on 2023-04-24 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0090_rename_signup_tutorial_alter_tutorial_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='weapon',
            name='bio',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
