import strawberry
import strawberry.django

from strawberry import ID

from django.shortcuts import get_object_or_404

from .models import User as mUser

from strawberry_django_plus import gql


@gql.django.type(mUser)
class User:
    id: ID
    username: str
    

@strawberry.type
class Query:
    user: User = gql.django.field()
    users: list[User] = gql.django.field()