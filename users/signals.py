from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Profile
from anime.tasks import send_mail_task


@receiver(post_save, sender=get_user_model())
def send_notification_on_new_episode(sender, instance, created, **kwargs):
    if created:
        if instance.is_subscribed:
            send_mail_task.delay(
                'Добро пожаловать!',
                'Вы подписались на рассылку',
                [instance.email],
                html_template='anime/welcome_email_message.html',
            )


def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


def save_user_profile(sender, instance, **kwargs):
    if not instance.profile_user:
        instance.profile.save()


post_save.connect(create_user_profile, sender=get_user_model())
post_save.connect(save_user_profile, sender=get_user_model())