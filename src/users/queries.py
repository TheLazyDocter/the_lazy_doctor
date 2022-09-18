import strawberry
from strawberry import auto
from strawberry import django
from . import models


@django.type(models.User)
class Users:
    username: str