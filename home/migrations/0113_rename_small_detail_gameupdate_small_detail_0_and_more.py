# Generated by Django 4.1.13 on 2024-03-26 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0112_rename_smail_detail_gameupdate_small_detail'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gameupdate',
            old_name='small_detail',
            new_name='small_detail_0',
        ),
        migrations.AddField(
            model_name='gameupdate',
            name='small_detail_1',
            field=models.CharField(default=1, max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='gameupdate',
            name='small_detail_2',
            field=models.CharField(default=1, max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='gameupdate',
            name='small_detail_3',
            field=models.CharField(default=1, max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='gameupdate',
            name='small_detail_4',
            field=models.CharField(default=11, max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='gameupdate',
            name='small_detail_5',
            field=models.CharField(default=1, max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='gameupdate',
            name='small_detail_6',
            field=models.CharField(default=1, max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='gameupdate',
            name='small_detail_7',
            field=models.CharField(default=1, max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='gameupdate',
            name='small_detail_8',
            field=models.CharField(default=1, max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='gameupdate',
            name='small_detail_9',
            field=models.CharField(default=1, max_length=1000),
            preserve_default=False,
        ),
    ]
