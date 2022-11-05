# core
from core.extensions import AuthenticateExtension

# third party
import strawberry

# first party
from users.schema import Mutation as UserMutation, Query as UserQuery


@strawberry.type
class Query(UserQuery):
    pass

@strawberry.type
class Mutation(UserMutation):
    pass


schema = strawberry.Schema(
    query=Query,
    mutation=Mutation,
    extensions=[AuthenticateExtension]
)
