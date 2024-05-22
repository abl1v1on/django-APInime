# Generated by Django 5.0.6 on 2024-05-22 04:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anime', '0005_remove_anime_likes_like'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnimeSeries',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('series_file', models.FileField(upload_to='anime_series/%Y/%m', verbose_name='Серии')),
                ('anime_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='anime_series', to='anime.anime', verbose_name='Аниме')),
            ],
            options={
                'verbose_name': 'Серия',
                'verbose_name_plural': 'Серии',
            },
        ),
    ]
