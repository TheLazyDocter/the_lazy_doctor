# third party
import strawberry

from strawberry.django import field

# first party
from users.queries import Users


@strawberry.type
class Query:
    users: list[Users] = field()    


schema = strawberry.Schema(query=Query)