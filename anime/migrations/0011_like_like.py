# Generated by Django 5.0.6 on 2024-05-26 00:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anime', '0010_remove_like_like'),
    ]

    operations = [
        migrations.AddField(
            model_name='like',
            name='like',
            field=models.BooleanField(default=True),
        ),
    ]
