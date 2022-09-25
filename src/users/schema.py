from typing import Any

import strawberry
import strawberry.django

from strawberry import ID

from django.shortcuts import get_object_or_404

from .models import User as mUser


@strawberry.django.type(mUser)
class User:
    username: str
    

def get_user(pk: ID):
    return get_object_or_404(mUser, id=pk)

@strawberry.type
class Query:
    user: User = strawberry.django.field(resolver=get_user)
    users: list[User] = strawberry.django.field()