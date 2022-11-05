# core
from core.permissions import IsAuthenticated

# third party
import strawberry
import strawberry.django

from strawberry.types import Info
from strawberry_django_plus import gql

# local
from .models import User, UserKind
from .types import UserType


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
        """ mutation used to convert firebase user to user 
            also returns the `status` of the user registrations
            - NEW
            - EXISTING
        """

        # TODO valid the token 

        try:
            user = User.objects.get(kind=UserKind.PATIENT, pk=1)
        except User.DoesNotExist:
            # TODO get the user form firebase
            user = User.objects.create_user(
                username='ivin',
                password='Notpassword',
                email='ivin@email.com',
                kind=UserKind.PATIENT
            )

        return user
        
