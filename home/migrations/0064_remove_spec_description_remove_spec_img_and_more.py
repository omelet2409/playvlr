# Generated by Django 4.1.7 on 2023-04-04 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0063_map_img1_map_img2_map_img3_map_img4_map_img5_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='spec',
            name='description',
        ),
        migrations.RemoveField(
            model_name='spec',
            name='img',
        ),
        migrations.RemoveField(
            model_name='spec',
            name='name',
        ),
        migrations.RemoveField(
            model_name='spec',
            name='slug',
        ),
        migrations.AddField(
            model_name='spec',
            name='cpu_1',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='spec',
            name='cpu_2',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='spec',
            name='cpu_3',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='spec',
            name='gpu_1',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='spec',
            name='gpu_2',
            field=models.CharField(default=11, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='spec',
            name='gpu_3',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='spec',
            name='highend',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='spec',
            name='minimum',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='spec',
            name='ram',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='spec',
            name='recommended',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='spec',
            name='vram',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='spec',
            name='windows',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
