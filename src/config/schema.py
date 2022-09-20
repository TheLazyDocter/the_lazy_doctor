# third party
import strawberry

from strawberry.django import field, auth
from strawberry_django import mutations
# first party
from users.queries import User, UserInput

from bookings.mutations import AppointmentInput, AppointmentType

@strawberry.type
class Query:
    users: list[User] = field()
    me: User = auth.current_user()


@strawberry.type
class Mutation:
    login: User = auth.login()
    logout = auth.logout()
    register: User = auth.register(UserInput)
    book: AppointmentType = mutations.create(AppointmentInput)


schema = strawberry.Schema(
    query=Query,
    mutation=Mutation,
)
