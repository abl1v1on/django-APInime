# Generated by Django 5.0.6 on 2024-05-21 18:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anime', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anime',
            name='studio',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='anime.studio', verbose_name='Студия'),
        ),
    ]
