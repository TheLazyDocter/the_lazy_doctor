# django
from django.contrib import admin
from django.http import HttpResponse
from django.urls import path

# third party
import strawberry

from strawberry.django.views import GraphQLView

# local
from . import __version__


@strawberry.type
class Book:
    title: str

    @strawberry.field
    def hello() -> str:
        return "world"


def get_books():
    return [
        Book(title='The Great Gatsby',),
    ]


@strawberry.type
class Query:
    books: list[Book] = strawberry.field(resolver=get_books)


schema = strawberry.Schema(query=Query)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("graphql/", GraphQLView.as_view(schema=schema)),
    path("version/", lambda r: HttpResponse(__version__)),
]
