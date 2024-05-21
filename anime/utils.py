from .models import Anime, models


class AnimeUtils:
    def __init__(self, model: models.Model) -> None:
        self.model = model

    def get_anime(self):
        return self.model.objects.all()


utils = AnimeUtils(model=Anime)