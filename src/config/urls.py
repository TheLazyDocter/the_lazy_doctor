# django
from django.contrib import admin
from django.http import HttpResponse
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

# third party
import strawberry

from strawberry.django.views import GraphQLView

# local
from . import __version__

from users.queries import Users
from users.models import User, UserKind

@strawberry.type
class Book:
    title: str

    @strawberry.field
    def hello() -> str:
        return "world"


@strawberry.type
class Query:
    
    @strawberry.django.field
    def users(self, info) -> list[Users]: 
        return User.objects.filter(kind=UserKind.ADMIN)
    
    @strawberry.field
    def books() -> list[Book]:
        return [
            Book(title='The Great Gatsby',),
        ]


schema = strawberry.Schema(query=Query)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("graphql/", GraphQLView.as_view(schema=schema)),
    path("version/", lambda r: HttpResponse(__version__)),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
