from django.core.exceptions import ValidationError

MAX_COVER_SIZE = 2 * 1024 * 1024  # ~2 MB


def validate_cover_size(value):
        if value.size > MAX_COVER_SIZE:
            raise ValidationError('Максимальный вес обложки 2мб')
