import strawberry
import strawberry.django

from strawberry.types import Info
from strawberry_django_plus import gql

from core.permissions import IsAuthenticated

from .types import User, UserInput


@strawberry.type
class Query:
    users: list[User] = gql.django.field(permission_classes=[IsAuthenticated])
    user: User = gql.django.field(permission_classes=[IsAuthenticated])
    
    
    @gql.django.field(permission_classes=[IsAuthenticated])
    def me(self, info: Info) -> User:
        return info.context.request.user
    
@strawberry.type
class Mutation:
    create_user_plus: User = gql.django.create_mutation(UserInput)
    create_user: User = strawberry.django.mutations.create(UserInput)
    # update_model: User = gql.django.update_mutation(SomeModelInputPartial)
    # delete_model: User = gql.django.delete_mutation(gql.NodeInput)

