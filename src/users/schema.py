from typing import Any

import strawberry

from strawberry import ID

from django.shortcuts import get_object_or_404

from .models import User as mUser


@strawberry.type
class User:
    username: str


def f(id) -> Any:
    return get_object_or_404(mUser, id=id)

@strawberry.type
class Query:
    @strawberry.field
    def user(self, id: ID) -> User:
        return f(id)