# third party
import strawberry

from users.schema import Query as UserQuery, Mutation as UserMutation

@strawberry.type
class Query(UserQuery):
    pass

@strawberry.type
class Mutation(UserMutation):
    pass


schema = strawberry.Schema(
    query=Query,
    mutation=Mutation,
)
