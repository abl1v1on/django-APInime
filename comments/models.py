from django.db import models
from django.contrib.auth import get_user_model

from anime.models import Anime


class Comment(models.Model):
    comment_text = models.CharField(max_length=2000, verbose_name='Текст')
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    anime = models.ForeignKey(
        Anime, 
        on_delete=models.CASCADE, 
        verbose_name='Аниме', 
        related_name='comment_anime'
    )
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name='Пользователь')

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self) -> str:
        return self.comment_text
    