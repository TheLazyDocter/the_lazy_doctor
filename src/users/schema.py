import strawberry
import strawberry.django

from strawberry.types import Info
from strawberry_django_plus import gql

from core.permissions import IsAuthenticated

from .types import User, UserInput


@strawberry.type
class Query:
    # details
    user: User = strawberry.django.field()
    user_plus: User = gql.django.field(permission_classes=[IsAuthenticated])
    
    # list
    users: list[User] = strawberry.django.field()
    users_plus: list[User] = gql.django.field(permission_classes=[IsAuthenticated])

    @gql.django.field()
    def me(self, info: Info) -> User:
        return info.context.request.user
    
    @gql.django.field(permission_classes=[IsAuthenticated])
    def mee(self, info: Info) -> User:
        return info.context.request.user
    
@strawberry.type
class Mutation:
    create_user_plus: User = gql.django.create_mutation(UserInput)
    create_user: User = strawberry.django.mutations.create(UserInput)
    # update_model: User = gql.django.update_mutation(SomeModelInputPartial)
    # delete_model: User = gql.django.delete_mutation(gql.NodeInput)

