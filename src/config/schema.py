# third party
import strawberry

from strawberry.django import field, auth
from strawberry_django import mutations
# first party
from users.queries import User, UserInput

from bookings.schema.mutations import BookingMutation
from bookings.schema.queries import AppointmentType, make_a_booking


@strawberry.type
class Query:
    users: list[User] = field()
    me: User = auth.current_user()
    bookings: list[AppointmentType] = strawberry.field(resolver=make_a_booking)


@strawberry.type
class Mutation(BookingMutation):
    login: User = auth.login()
    logout = auth.logout()
    register: User = auth.register(UserInput)


schema = strawberry.Schema(
    query=Query,
    mutation=Mutation,
)
