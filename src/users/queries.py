# third party
from strawberry import django

# local
from . import models


@django.type(models.User)
class Users:
    username: str