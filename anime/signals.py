from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import AnimeSeries
from .tasks import send_mail_task


@receiver(post_save, sender=AnimeSeries)
def send_notification_on_new_episode(sender, instance, created, **kwargs):
    if created:
        anime_likes = instance.anime_id.likes_anime.all()
        for like in anime_likes:
            user = like.user
            if user.is_subscribed:
                user_email = user.email
                send_mail_task.delay(
                    f'НОВАЯ СЕРИЯ {instance.anime_id.title}',
                    '',
                    [user_email],
                    html_template='anime/new_episode_message.html',
                    context={
                        'logo': instance.anime_id.cover.url,
                        'title': instance.anime_id.title,
                        'desc': instance.anime_id.description
                    }
                )
