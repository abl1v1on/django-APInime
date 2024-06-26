# Generated by Django 5.0.6 on 2024-05-23 22:34

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anime', '0007_like_like'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='anime',
            name='likes',
            field=models.ManyToManyField(related_name='anime_likes', through='anime.Like', to=settings.AUTH_USER_MODEL),
        ),
    ]
