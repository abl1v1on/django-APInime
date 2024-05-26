from django.db import models
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError


ANIME_TYPE_CHOISES = [
    ('tv_series', 'Сериал'),
    ('movie', 'Фильм')
]

ANIME_STATUS_CHOISES = [
    ('it_continues', 'Выходит'),
    ('completed', 'Завершен')
]

VIEWING_STATUS_CHOISES = [
    ('watching', 'Смотрю'),
    ('viewed', 'Просмотрено'),
    ('abandoned', 'Заброшено')
]

MAX_COVER_SIZE = 2 * 1024 * 1024  # ~2 MB


def validate_cover_size(value):
        if value.size > MAX_COVER_SIZE:
            raise ValidationError('Максимальный вес обложки 2мб')


class Anime(models.Model):
    title = models.CharField('Название', max_length=255)
    alt_title = models.CharField('Альтернативное название', max_length=255, blank=True)
    description = models.TextField('Описание', max_length=1000)
    type = models.CharField('Тип',max_length=10, choices=ANIME_TYPE_CHOISES)
    studio = models.ForeignKey('Studio', on_delete=models.CASCADE, blank=True, verbose_name='Студия')

    date_aired = models.DateField('Дата выхода в эфир')
    status = models.CharField('Статус', max_length=15, choices=ANIME_STATUS_CHOISES)
    genres = models.ManyToManyField('Genre', related_name='anime_genres', verbose_name='Жанры')
    rating = models.FloatField('Рейтинг', blank=True, default=0)
    duration = models.CharField('Продолжительность', max_length=50)
    views = models.PositiveIntegerField('Просмотры', blank=True, default=0)
    cover = models.ImageField(
        'Обложка', 
        upload_to='anime_covers/%Y/%m', 
        blank=True,
        validators=[validate_cover_size]
    )
    slug = models.SlugField('URL', max_length=255, db_index=True, unique=True)
    likes = models.ManyToManyField(get_user_model(), related_name='anime_likes', through='Like')

    class Meta:
        verbose_name = 'Аниме'
        verbose_name_plural = 'Аниме'
    
    def __str__(self) -> str:
        return self.title

    def total_likes(self):
        return self.likes.count()


class AnimeSeries(models.Model):
    anime_id = models.ForeignKey(
        'Anime', 
        related_name='anime_series', 
        on_delete=models.CASCADE, 
        verbose_name='Аниме'
    )
    series_file = models.FileField(upload_to='anime_series/%Y/%m', verbose_name='Серии')
    series_number = models.PositiveIntegerField('Номер серии', blank=True, null=True)

    class Meta:
        verbose_name = 'Серия'
        verbose_name_plural = 'Серии'



class Studio(models.Model):
    name = models.CharField('Название', max_length=100)
    slug = models.SlugField('URL', max_length=100, db_index=True, unique=True)

    class Meta:
        verbose_name = 'Студия'
        verbose_name_plural = 'Студии'

    def __str__(self) -> str:
        return self.name


class Genre(models.Model):
    name = models.CharField('Название', max_length=100)
    slug = models.SlugField('URL', max_length=100, db_index=True, unique=True)
    
    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'
    
    def __str__(self) -> str:
        return self.name


class ViewingStatus(models.Model):
    name = models.CharField(
        max_length=15, 
        choices=VIEWING_STATUS_CHOISES, 
        verbose_name='Название'
    )
    slug = models.SlugField(
        'URL', 
        max_length=15, 
        db_index=True, 
        unique=True
    )

    class Meta:
        verbose_name = 'Статус просмотра'
        verbose_name_plural = 'Статусы просмотов'
    
    def __str__(self) -> str:
        return self.name


class Like(models.Model):
    user = models.ForeignKey(
        get_user_model(), 
        on_delete=models.CASCADE,
        verbose_name='Пользователь'
    )
    anime = models.ForeignKey(
        Anime,
        on_delete=models.CASCADE,
        verbose_name='Аниме',
        related_name='likes_anime'
    )
    like = models.BooleanField(default=True)
    
    def __str__(self) -> str:
        return self.user.email
    