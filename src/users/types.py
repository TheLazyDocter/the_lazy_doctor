from strawberry import ID


from strawberry_django_plus import gql

from . import models



@gql.django.type(models.User)
class User:
    id: ID
    username: str
    patientprofile: 'UserProfile'


@gql.django.type(models.PatientProfile)
class UserProfile:
    address: str
    

@gql.django.input(models.User)
class UserInput:
    username: str
    password: str
    patientprofile: 'UserProfileInput'

@gql.django.input(models.PatientProfile)
class UserProfileInput:
    address: str


@gql.django.partial(models.User)
class UserInputPartial(gql.NodeInput):
    username: str
    first_name: str
    last_name: str
    email: str
