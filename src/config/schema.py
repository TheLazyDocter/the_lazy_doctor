# third party
import strawberry

from strawberry_django_plus.directives import SchemaDirectiveExtension

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
    extensions=[SchemaDirectiveExtension,]
)
