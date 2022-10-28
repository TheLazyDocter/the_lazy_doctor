import typing

from strawberry.types import Info

from strawberry.permission import BasePermission


class IsAuthenticated(BasePermission):
    message = "User is not authenticated sir"

    # This method can also be async!
    def has_permission(self, source: typing.Any, info: Info, **kwargs) -> bool:
        return False
