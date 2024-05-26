from config import settings
from django.core.mail import EmailMultiAlternatives
from django.db.models import Count, Case, When, Prefetch
from django.template.loader import render_to_string

from .models import Anime, AnimeSeries, Like, models, Genre


class Utils:
    def __init__(self, model: models.Model) -> None:
        self.model = model

    def get_objects(self):
        return self.model.objects.all()
    
    def is_exist(self, **kwargs):
        return self.model.objects.filter(**kwargs).exists()


def call_in_new_anime_episodes(
        subject, 
        message, 
        recipient_list, 
        html_template, 
        context=None
    ):
    msg = EmailMultiAlternatives(
        subject,
        message,
        settings.EMAIL_HOST_USER,
        recipient_list
    )

    html_content = render_to_string(html_template, context)
    msg.attach_alternative(html_content, 'text/html')
    msg.send()


def get_all_anime():
    return Anime.objects.all().annotate(
            likes_count=Count(Case(When(likes_anime__like=True, then=1))),    
        ).prefetch_related('genres', 'studio')


def get_likes():
    return Like.objects.prefetch_related('user', 'anime').all()


anime_utils = Utils(model=Anime)
anime_series_urils = Utils(model=AnimeSeries)
likes_utils = Utils(model=Like)
