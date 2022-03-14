import factory
from factory.django import DjangoModelFactory

from StudentConnectApp.models import Student, Answer

class StudentFactory(DjangoModelFactory):
    class Meta:
        model = Student
    
    forename = factory.Faker("first_name")
    surname = factory.Faker("last_name")
    date_of_birth = factory.Faker("date_of_birth")

    