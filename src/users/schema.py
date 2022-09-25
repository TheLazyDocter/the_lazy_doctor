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
    

@gql.django.input(mUser)
class UserInput:
    username: str
    password: str


@gql.django.partial(mUser)
class UserInputPartial(gql.NodeInput):
    username: str
    first_name: str
    last_name: str
    email: str


@strawberry.type
class Query:
    user: User = gql.django.field()
    users: list[User] = gql.django.field()


@strawberry.type
class Mutation:
    create_user: User = gql.django.create_mutation(UserInput)
    create_user2: User = strawberry.django.mutations.create(UserInput)
    # update_model: User = gql.django.update_mutation(SomeModelInputPartial)
    # delete_model: User = gql.django.delete_mutation(gql.NodeInput)