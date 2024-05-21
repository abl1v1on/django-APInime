from django.contrib.auth import get_user_model
from django.db.models.signals import post_save

from .models import Profile


def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


post_save.connect(create_user_profile, sender=get_user_model())
post_save.connect(save_user_profile, sender=get_user_model())