from .models import Anime, AnimeSeries, Like, models
from django.core.mail import send_mail
from config import settings


class Utils:
    def __init__(self, model: models.Model) -> None:
        self.model = model

    def get_objects(self):
        return self.model.objects.all()
    
    def is_exist(self, **kwargs):
        return self.model.objects.filter(**kwargs).exists()


def call_in_new_anime_episodes(anime, user_email):
    send_mail(
        f'Вышла новая серия {anime.title}',
        f'Новая серия {anime.title}!',
        settings.EMAIL_HOST_USER,
        [user_email],
        fail_silently=False
    )


anime_utils = Utils(model=Anime)
anime_series_urils = Utils(model=AnimeSeries)
likes_utils = Utils(model=Like)
