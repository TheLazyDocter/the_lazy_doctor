# third party
import strawberry

from strawberry.django import field, auth

# first party
from users.queries import User, UserInput


@strawberry.type
class Query:
    users: list[User] = field()
    me: User = auth.current_user()


@strawberry.type
class Mutation:
    login: User = auth.login()
    logout = auth.logout()
    register: User = auth.register(UserInput)


schema = strawberry.Schema(
    query=Query,
    mutation=Mutation,
)
