from rest_framework.exceptions import PermissionDenied


def is_author(instance, request):
    if instance.user != request.user:
        raise PermissionDenied('Access denied')
    return instance