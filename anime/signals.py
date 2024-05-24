from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import AnimeSeries
from .utils import call_in_new_anime_episodes


@receiver(post_save, sender=AnimeSeries)
def send_notification_on_new_episode(sender, instance, created, **kwargs):
    if created:
        anime_likes = instance.anime_id.likes_anime.all()
        for like in anime_likes:
            user = like.user
            if user.is_subscribed:
                user_email = user.email
                call_in_new_anime_episodes(instance.anime_id, user_email)
