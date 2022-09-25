# third party
import strawberry

from users.schema import Query as UserQuery

@strawberry.type
class Query(UserQuery):
    pass

@strawberry.type
class Mutation:
    pass


schema = strawberry.Schema(
    query=Query,
    # mutation=Mutation,
)
