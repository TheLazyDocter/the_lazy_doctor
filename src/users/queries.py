# third party
import strawberry
from strawberry import django, auto
# local
from . import models


@django.type(models.User)
class User:
    username: str


@django.input(models.User)
class UserInput:
    username: auto
    password: auto
