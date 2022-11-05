# builtins
import typing

# third party
from strawberry.permission import BasePermission
from strawberry.types import Info


class IsAuthenticated(BasePermission):
    message = "User is not authenticated"

    # This method can also be async!
    def has_permission(self, source: typing.Any, info: Info, **kwargs) -> bool:
        user = info.context.request.user
        return user.is_authenticated and user.is_active
