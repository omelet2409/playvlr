# Generated by Django 4.1.7 on 2023-04-06 01:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0071_remove_agent_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='agent',
            name='skill_c_video',
        ),
        migrations.RemoveField(
            model_name='agent',
            name='skill_e_video',
        ),
        migrations.RemoveField(
            model_name='agent',
            name='skill_q_video',
        ),
        migrations.RemoveField(
            model_name='agent',
            name='skill_x_video',
        ),
    ]
