# third party
from graphql import GraphQLResolveInfo
from strawberry.extensions import Extension
from strawberry.utils.await_maybe import AwaitableOrValue

from django.http.request import HttpRequest


from django.contrib.auth import get_user_model

User = get_user_model()

class AuthenticateExtension(Extension):
    keyword: str = 'Bearer'
    auth_header_key: str = 'Authorization'

    def resolve(self, _next, root, info: GraphQLResolveInfo, *args, **kwargs) -> AwaitableOrValue[object]:
        request: HttpRequest = info.context.request

        val = request.headers.get(self.auth_header_key)

        if val is not None:
            key, val = val.split(sep=' ')

            if key == self.keyword: 
                info.context.request.user =  User.objects.get(pk=int(val))
        
        return _next(root, info, *args, **kwargs)

