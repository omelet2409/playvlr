# Generated by Django 4.1.7 on 2023-04-24 05:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0089_remove_signup_img2_remove_signup_img3_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Signup',
            new_name='Tutorial',
        ),
        migrations.AlterModelOptions(
            name='tutorial',
            options={'verbose_name': 'tutorial', 'verbose_name_plural': 'tutorials'},
        ),
    ]
