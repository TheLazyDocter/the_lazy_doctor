import typing
import strawberry
import strawberry.django

from strawberry import ID
from strawberry.types.info import Info
from strawberry_django_plus import gql
from strawberry_django_plus.permissions import IsAuthenticated
from strawberry.permission import BasePermission

from .types import User, UserInput

from strawberry.types import Info

class IsAuth(BasePermission):
    message = "User is not authenticated sir"

    # This method can also be async!
    def has_permission(self, source: typing.Any, info: Info, **kwargs) -> bool:
        return False

@strawberry.type
class Query:
    # details
    user: User = strawberry.django.field()
    user_plus: User = gql.django.field(directives=[IsAuthenticated()])
    
    # list
    users: list[User] = strawberry.django.field()
    users_plus: list[User] = gql.django.field()

    @gql.django.field(directives=[IsAuthenticated()])
    def me(self, info: Info) -> User:
        return info.context.request.user
    
    @gql.django.field(permission_classes=[IsAuth])
    def mee(self, info: Info) -> User:
        return info.context.request.user
    
@strawberry.type
class Mutation:
    create_user_plus: User = gql.django.create_mutation(UserInput)
    create_user: User = strawberry.django.mutations.create(UserInput)
    # update_model: User = gql.django.update_mutation(SomeModelInputPartial)
    # delete_model: User = gql.django.delete_mutation(gql.NodeInput)

