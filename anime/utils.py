from .models import Anime, AnimeSeries, Like, models


class Utils:
    def __init__(self, model: models.Model) -> None:
        self.model = model

    def get_objects(self):
        return self.model.objects.all()
    
    def is_exist(self, **kwargs):
        return self.model.objects.filter(**kwargs).exists()


anime_utils = Utils(model=Anime)
anime_series_urils = Utils(model=AnimeSeries)
likes_utils = Utils(model=Like)
