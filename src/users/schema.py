from typing import cast

import strawberry
import strawberry.django

from strawberry.types import Info
from strawberry_django_plus import gql

from core.permissions import IsAuthenticated

from .models import User
from .types import UserType, UserInput


@strawberry.type
class Query:
    users: list[UserType] = gql.django.field(permission_classes=[IsAuthenticated])
    user: UserType = gql.django.field(permission_classes=[IsAuthenticated])
    
    
    @gql.django.field(permission_classes=[IsAuthenticated])
    def me(self, info: Info) -> UserType:
        return info.context.request.user
    
@strawberry.type
class Mutation:

    @strawberry.mutation
    def on_boarding(self, token: str) -> UserType:
        # TODO valid the token 
        
        try:
            user = User.objects.get(pk=1)
        except User.DoesNotExist:
            # TODO get the user form firebase
            user = User.objects.create_user(
                username='ivin',
                password='Notpassword',
                email='ivin@email.com',
            )

        return user
        
