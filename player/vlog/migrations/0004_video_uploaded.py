# Generated by Django 3.1.7 on 2021-03-31 07:46

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('vlog', '0003_remove_video_video_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='uploaded',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата загрузки'),
        ),
    ]
